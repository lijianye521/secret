import argparse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn
import warnings
from logic import colicTest,Test_write_back, decode_data
from random_forest import random_forest
from XGBoost import xgboost
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def model_performance(file_path)->None:
    pred1,label1 = colicTest(file_path)
    pred2,label2 = random_forest(file_path)
    pred3,label3 = xgboost(file_path)

    # 混淆矩阵
    confusion_matrix = confusion_matrix(y_test, y_pred)
    print("混淆矩阵：\n", confusion_matrix)
    # 准确率
    accuracy = accuracy_score(y_test, y_pred)
    print("准确率：", accuracy)
    # 精确率
    precision = precision_score(y_test, y_pred)
    print("精确率：", precision)
    # 召回率
    recall = recall_score(y_test, y_pred)
    print("召回率：", recall)
    # F1值
    f1 = f1_score(y_test, y_pred)
    print("F1值：", f1)
    # ROC曲线
    y_score = model.decision_function(x_test)
    fpr, tpr, thresholds = roc_curve(y_test, y_score)
    plt.plot(fpr, tpr, marker='o')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.show()
    # AUC值
    auc = roc_auc_score(y_test, y_score)
    print("AUC值：", auc)
    # 绘制热力图
    sn.heatmap(confusion_matrix, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    plt.title('Confusion Matrix')
    plt.show()
    return None



def register_filepath_command(
    subparsers: argparse._SubParsersAction,
) -> None:
    parser.add_argument(
        '--train_file_path', 
        type=str, 
        default='/home/xyj/Downloads/code/1/input/internet_service_churn.csv',
        help='Training set path')
    parser.add_argument(
        '--test_file_path', 
        type=str, 
        default='/home/xyj/Downloads/code/1/input_test/churn_test.csv',
        help='Testing set path')
    parser.add_argument(
        '--train_file_path', 
        type=str, 
        default='/home/xyj/Downloads/code/1/input/internet_service_churn.csv',
        help='Training set path')

if __name__ == "__main__":

    def setup_parser() -> argparse.ArgumentParser:
            parser = argparse.ArgumentParser(
                description="Select the command to execute"
            )
            subparsers = parser.add_subparsers(dest="command")
            register_filepath_command(subparsers)
            return parser

    def execute_command(
        args: argparse.Namespace,
        parser: argparse.ArgumentParser,
    ) -> None:
        command_functions = {
            "train": colicTest,
            "test_and_encode": Test_write_back,
            "decode": decode_data,
            "model_performance": model_performance,
        }

        if args.command in command_functions:
            command_functions[args.command](args)
        else:
            parser.print_help()

    parser = setup_parser()
    args = parser.parse_args()
    execute_command(args, parser)