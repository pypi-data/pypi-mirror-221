# -*- encoding: utf-8 -*-
"""
LstmPredictor 预报模型的服务器接口 api。

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@keepsoft.net'
"""
from FloodMaster.forecasters import LstmPredictor
from FloodMaster.utils import CsvLoader
from FloodMaster.utils import DatasetPreprocessor as dp
from configs.settings import logger

from flask_restplus import Resource
from flask import request, jsonify, make_response, abort
import numpy as np
import pandas as pd
import json
import datetime
import matplotlib.pyplot as plt
import io
import os


class LstmConstruction(Resource):
    """构建LSTM模型。
    """

    def post(self):
        post_data = request.get_json()
        lstm_cnfs = post_data['params']
        # 构建并保存lstm模型
        logger.info(f"lstm model({lstm_cnfs['id']}) building")
        model = LstmPredictor(lstm_cnfs['id'])
        model.compile(lstm_cnfs)
        model.save()
        logger.info(f"lstm model({lstm_cnfs['id']}) built")


class LstmTraining(Resource):
    """通过csv数据集文件训练LSTM模型。

    该接口会对数据集作提取和前处理检查。
    """

    def post(self):
        post_data = request.get_json()
        lstm_cnfs = post_data['params']
        # 解析请求
        cnfs_keys = lstm_cnfs.keys()
        time_step = lstm_cnfs['time_step'] if 'time_step' in cnfs_keys else 86400
        date_fmt = lstm_cnfs['date_fmt'] if 'date_fmt' in cnfs_keys else '%Y-%m-%d'
        start_date = lstm_cnfs['start_date'] if 'start_date' in cnfs_keys else None
        end_date = lstm_cnfs['end_date'] if 'end_date' in cnfs_keys else None
        date_col = lstm_cnfs['date_col'] if 'date_col' in cnfs_keys else "Date"
        index_col = lstm_cnfs['index_col'] if 'index_col' in cnfs_keys else None
        indexs = lstm_cnfs['index_selected'] if 'index_selected' in cnfs_keys else None
        load_path = lstm_cnfs['load_path'] if 'load_path' in cnfs_keys else os.getcwd()
        # 加载lstm模型
        logger.info(f"lstm model({lstm_cnfs['id']}) training")
        model = LstmPredictor.load(lstm_cnfs['id'], load_path)
        model_cnfs = model.get_model_confs()
        features = model_cnfs['features']
        labels = model_cnfs['labels']
        n_past = model_cnfs['n_past']
        n_forecast = model_cnfs['n_forecast']
        # 加载并拆分数据集
        df = CsvLoader(lstm_cnfs['data_file'],
                       features,
                       labels,
                       time_step=time_step,
                       date_fmt=date_fmt,
                       start_date=start_date,
                       end_date=end_date,
                       date_col=date_col,
                       index_col=index_col,
                       index_selected=indexs).get_dataset()
        train_df, _ = CsvLoader.train_test_split(df, features, labels, 0., False)
        # 训练lstm模型
        train_features_df, train_labels_df = train_df
        train_features = train_features_df.to_numpy()
        train_labels = train_labels_df.to_numpy()
        if 'time_step' not in model_cnfs.keys():
            lstm_cnfs['time_step'] = time_step
        model.fit(train_features, train_labels, lstm_cnfs)
        # 再次预报, 获取预报结果
        predictions = model.predict(train_features)
        x_arr, pred_dic, real_dic = _reorganize_predictions(predictions, train_labels,
                                                            labels, n_past, n_forecast)
        # 保存lstm模型
        model.save()
        # 绘制预报成果图
        canvas = _plot(x_arr, pred_dic, real_dic)
        buffer = io.BytesIO()
        canvas.print_png(buffer)
        data = buffer.getvalue()
        buffer.close()
        # 生成返回结果
        res = make_response(data)
        res.headers["Content-Type"] = "image/png"
        logger.info(f"lstm model({lstm_cnfs['id']}) trained")
        return make_response(res)


class LstmTrainingByDataset(Resource):
    """通过特征和标签数组训练LSTM模型。
    """

    def post(self):
        post_data = json.loads(request.data)
        lstm_cnfs = post_data['params']
        cnfs_keys = lstm_cnfs.keys()
        # 解析请求
        time_step = lstm_cnfs['time_step'] if 'time_step' in cnfs_keys else 86400
        date_fmt = lstm_cnfs['date_fmt'] if 'date_fmt' in cnfs_keys else '%Y-%m-%d'
        load_path = lstm_cnfs['load_path'] if 'load_path' in cnfs_keys else os.getcwd()
        # 加载lstm模型
        logger.info(f"lstm model({lstm_cnfs['id']}) dataset training")
        model = LstmPredictor.load(lstm_cnfs['id'], load_path)
        model_cnfs = model.get_model_confs()
        features = model_cnfs['features']
        labels = model_cnfs['labels']
        n_past = model_cnfs['n_past']
        n_forecast = model_cnfs['n_forecast']
        if 'time_step' not in model_cnfs.keys():
            lstm_cnfs['time_step'] = time_step
        # 训练数据处理
        features_arr = np.array(lstm_cnfs['feature_data']).reshape(-1, len(features))
        labels_arr = np.array(lstm_cnfs['label_data']).reshape(-1, len(labels))
        timeseries = np.array(lstm_cnfs['data_timeseries'])
        if (features_arr.shape[0] != labels_arr.shape[0]) or (features_arr.shape[0] !=
                                                              timeseries.shape[0]):
            abort(500)
        feat_train_arr = _resample_input_data(features_arr, features, timeseries,
                                              date_fmt, time_step)
        label_train_arr = _resample_input_data(labels_arr, labels, timeseries, date_fmt,
                                               time_step)
        # 训练lstm模型
        model.fit(feat_train_arr, label_train_arr, lstm_cnfs)
        # 再次预报, 获取预报结果
        predictions = model.predict(feat_train_arr)
        x_arr, pred_dic, real_dic = _reorganize_predictions(predictions,
                                                            label_train_arr, labels,
                                                            n_past, n_forecast)
        # 保存lstm模型
        model.save()
        # 绘制预报成果图
        canvas = _plot(x_arr, pred_dic, real_dic)
        buffer = io.BytesIO()
        canvas.print_png(buffer)
        data = buffer.getvalue()
        buffer.close()
        # 生成返回结果
        res = make_response(data)
        res.headers["Content-Type"] = "image/png"
        logger.info(f"lstm model({lstm_cnfs['id']}) trained")
        return make_response(res)


class LstmEvaluation(Resource):
    """评估LSTM模型。
    """

    def post(self):
        post_data = json.loads(request.data)
        lstm_cnfs = post_data['params']
        cnfs_keys = lstm_cnfs.keys()
        # 解析请求
        date_fmt = lstm_cnfs['date_fmt'] if 'date_fmt' in cnfs_keys else '%Y-%m-%d'
        load_path = lstm_cnfs['load_path'] if 'load_path' in cnfs_keys else os.getcwd()
        # 加载lstm模型
        logger.info(f"lstm model({lstm_cnfs['id']}) evaluating")
        model = LstmPredictor.load(lstm_cnfs['id'], load_path)
        model_cnfs = model.get_model_confs()
        features = model_cnfs['features']
        labels = model_cnfs['labels']
        time_step = model_cnfs['time_step']
        # 训练数据处理
        features_arr = np.array(lstm_cnfs['feature_data']).reshape(-1, len(features))
        labels_arr = np.array(lstm_cnfs['label_data']).reshape(-1, len(labels))
        timeseries = np.array(lstm_cnfs['data_timeseries'])
        if (features_arr.shape[0] != labels_arr.shape[0]) or (features_arr.shape[0] !=
                                                              timeseries.shape[0]):
            abort(500)
        feat_train_arr = _resample_input_data(features_arr, features, timeseries,
                                              date_fmt, time_step)
        label_train_arr = _resample_input_data(labels_arr, labels, timeseries, date_fmt,
                                               time_step)
        # 评估lstm模型
        scores = model.evaluate(feat_train_arr, label_train_arr)
        logger.info(f"lstm model({lstm_cnfs['id']}) evaluated")
        return jsonify({"responses": scores})


class LstmPrediction(Resource):
    """调用LSTM模型执行预报。

    一旦输入数据量确定，模型的输出结果(长度)也就确定了。但是，业务上可能会要求输入一定的情况下，
    能输出指定长度的预报结果。

    该接口在处理原始预报长度n_raw与指定预报长度n_spec间不匹配的问题时:
    + 若 n_raw >= n_spec, 则直接截取预报结果返回;
    + 若 n_raw < n_spec, 则向前填充输入数据(如果输入包含输出, 则循环预报), 直到满足输出长度。
    """

    def post(self):
        post_data = json.loads(request.data)
        lstm_cnfs = post_data['params']
        cnfs_keys = lstm_cnfs.keys()
        date_fmt = lstm_cnfs['date_fmt'] if 'date_fmt' in cnfs_keys else '%Y-%m-%d'
        load_path = lstm_cnfs['load_path'] if 'load_path' in cnfs_keys else os.getcwd()
        # 加载lstm模型
        logger.info(f"lstm model({lstm_cnfs['id']}) predicting")
        model = LstmPredictor.load(lstm_cnfs['id'], load_path)
        model_cnfs = model.get_model_confs()
        features = model_cnfs['features']
        labels = model_cnfs['labels']
        time_step = model_cnfs['time_step']
        # 数据集预处理
        # --- 输入数据处理
        features_arr = np.array(lstm_cnfs['feature_data']).reshape(-1, len(features))
        timeseries = np.array(lstm_cnfs['data_timeseries'])
        if features_arr.shape[0] != timeseries.shape[0]:
            abort(500)
        x_arr = _resample_input_data(features_arr, features, timeseries, date_fmt,
                                     time_step)
        # --- 生成预报时间序列
        start_date_str = timeseries[0]
        start_date = datetime.datetime.strptime(start_date_str, date_fmt)
        n_pred = lstm_cnfs['n_prediction']
        n_past = model_cnfs['n_past']
        dates_pred = []
        dt = datetime.timedelta(seconds=time_step)
        for i in range(n_pred):
            curr_date = start_date + (i + n_past) * dt
            dates_pred.append(datetime.datetime.strftime(curr_date, date_fmt))
        # --- 统计特征中包含的标签
        label_contained = [lab for lab in labels if lab in features]
        label_idx_in_labels = [labels.index(lab) for lab in label_contained]
        label_idx_in_features = [features.index(lab) for lab in label_contained]
        # 模型预报
        while (1):
            pred = model.predict(x_arr)
            n_output = pred.shape[0]
            if n_output >= n_pred:
                break
            else:
                x_arr = np.vstack((x_arr, x_arr[-1]))
                # 不断填充输入数据集
                for i in range(len(label_contained)):
                    feat_idx = label_idx_in_features[i]
                    label_idx = label_idx_in_labels[i]
                    x_arr[-1][feat_idx] = pred[-1][label_idx]
        pred = pred[:n_pred]
        # 返回结果
        pred_dict = pd.DataFrame(pred, columns=labels).to_dict(orient='list')
        logger.info(f"lstm model({lstm_cnfs['id']}) predicted")
        return jsonify({'responses': [pred_dict, {'datetimes': dates_pred}]})


class LstmModelDeletion(Resource):
    """删除 LSTM 模型对象。
    """

    def post(self):
        post_data = json.loads(request.data)
        lstm_cnfs = post_data['params']
        cnfs_keys = lstm_cnfs.keys()
        load_path = lstm_cnfs['load_path'] if 'load_path' in cnfs_keys else os.getcwd()
        # 删除lstm模型对象
        model_id = lstm_cnfs['id']
        logger.info(f"lstm model({model_id}) deleting")
        for root, dirs, files in os.walk(os.path.join(load_path, model_id)):
            for f in files:
                if model_id in f:
                    os.remove(os.path.join(root, f))
            for d in dirs:
                if model_id in d:
                    os.rmdir(os.path.join(root, d))
        os.rmdir(os.path.join(load_path, model_id))
        logger.info(f"lstm model({model_id}) deleted")


class LstmModelExistence(Resource):
    """检查 LSTM 模型对象是否存在。
    """

    def get(self):
        model_id = request.args.get('id')
        load_path = request.args.get('load_path') or os.getcwd()
        try:
            LstmPredictor.load(model_id, load_path)
            return jsonify({'code': 200, 'message': f'lstm model({model_id}) existed'})
        except:
            return jsonify({
                'code': 400,
                'message': f'lstm model({model_id}) not existed'
            })


class LstmModelConfs(Resource):
    """获取 LSTM 模型配置。
    """

    def get(self):
        model_id = request.args.get('id')
        load_path = request.args.get('load_path') or os.getcwd()
        confs_keys = request.args.getlist('conf_keys') or None
        model = LstmPredictor.load(model_id, load_path)
        model_confs = model.get_model_confs()
        model_confs_query = model_confs
        if confs_keys:
            model_confs_query = dict(
                (key, val) for key, val in model_confs.items() if key in confs_keys)
        return jsonify({model_id: model_confs_query})


def _resample_input_data(data_arr, data_ids, timeseries, date_fmt, time_step):
    """将接口接收的数据重构和重采样。
    """
    data_df = pd.DataFrame(data_arr, columns=data_ids)
    data_df['TM'] = timeseries
    dp.check_numeric_cols(data_df, True)
    dp.check_nan(data_df, True)
    data_df = dp.check_datetime_continuous(data_df, 'TM', date_fmt, time_step)
    return data_df[data_ids].to_numpy()


def _reorganize_predictions(pred_arr, real_arr, labels, n_past, n_forecast):
    """重新组织预报结果。
    """
    pred_dic, real_dic = {}, {}
    for i in range(len(labels)):
        label = labels[i]
        real_y_i = real_arr[n_past:, i]
        if n_forecast < 2:
            pred_y_i = pred_arr[:, i]
        else:
            pred_y_i = pred_arr[:-n_forecast + 1, i]
        pred_dic[label] = pred_y_i
        real_dic[label] = real_y_i
    x_arr = [i for i in range(0, real_arr.shape[0] - n_past)]
    return x_arr, pred_dic, real_dic


def _plot(x, pred_data_dic, real_data_dic):
    """绘制预报成果图。
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    fig = plt.figure()
    # 划分绘图板
    pic_num = len(pred_data_dic)
    pic_rows = int(np.sqrt(pic_num))
    pic_columns = int(pic_num / pic_rows)
    if pic_rows * pic_columns < pic_num:
        pic_rows += 1

    # 绘图
    pic_idx = 1
    for var in pred_data_dic.keys():
        plt.subplot(pic_rows, pic_columns, pic_idx)
        pic_idx += 1

        plt.plot(x, pred_data_dic[var], label=var + "-pred")
        plt.plot(x, real_data_dic[var], label=var + "-real")
        plt.legend()
        plt.xlabel('X')
        plt.ylabel(var)
        plt.title(var + "-validation")
    return fig.canvas
