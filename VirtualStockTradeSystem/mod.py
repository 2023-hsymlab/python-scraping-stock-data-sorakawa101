import streamlit as st
from sqlalchemy import text
import numpy as np
import pandas as pd
import datetime

df_stock_code = pd.read_excel("./src/data_j.xls")


# 銘柄コードの数字（文字列）を企業名に変換する関数
def StockCodeStr_to_CorpName(s):

    # 銘柄コードに一致する企業名
    # コードが一致する行のみを抽出したDF
    df_corp = df_stock_code[df_stock_code['コード']
                            == int(s.split('.JP')[0])]

    # DFから銘柄名の絡むだけを抽出したseries（DFの最小単位）
    series_corp = df_corp['銘柄名']

    # seriesから企業名の値だけを抽出
    corp_name = series_corp.iloc[-1]

    return corp_name


# MySQLから指定したテーブルをDFとして取得する関数
def ConnectMySQL_and_GetTable(table):
    # MySQLと接続
    # Initialize connection.
    connection = st.experimental_connection('mysql', type='sql')

    df_stock_code_list = connection.query(
        f'SELECT * from {table};', ttl=600)

    return df_stock_code_list



# MySQLにクエリとデータを渡して、クエリを実行する関数
def ConnectMySQL_and_ExecuteData(query):
    # MySQLと接続
    # Initialize connection.
    connection = st.experimental_connection('mysql', type='sql')

    with connection.session as s:
        s.execute(query)
        s.commit()