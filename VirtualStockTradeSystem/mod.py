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

    # DFから銘柄名のカラムだけを抽出したseries（DFの最小単位）
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
        f'SELECT * from {table};')

    return df_stock_code_list



# MySQLにクエリとデータを渡して、クエリを実行する関数
def ConnectMySQL_and_ExecuteQuery(query):
    # MySQLと接続
    # Initialize connection.
    connection = st.experimental_connection('mysql', type='sql')

    with connection.session as s:
        s.execute(query)
        s.commit()


def Reset_ConnectionMySQL():
    connection = st.experimental_connection('mysql', type='sql')
    connection.reset()


# 非表示にしたい日付（＝株式市場が閉場している日付）リストを取得する関数
def Get_Unnecessary_DateList(df):
    #日付一覧を取得
    d_all = pd.date_range(start=df.index[0],end=df.index[-1])

    #株価データの日付リストを取得
    d_obs = [d.strftime("%Y-%m-%d") for d in df.index]

    # 株価データの日付データに含まれていない日付を抽出
    d_breaks = [d for d in d_all.strftime("%Y-%m-%d").tolist() if not d in d_obs]

    return d_breaks


def Get_SimpleMovingAverage(df):
    # SMAを計算
    df["SMA20"] = df["Close"].rolling(window=20).mean() 
    df["SMA50"] = df["Close"].rolling(window=50).mean()
    df["SMA200"] = df["Close"].rolling(window=200).mean()
    df.tail()
