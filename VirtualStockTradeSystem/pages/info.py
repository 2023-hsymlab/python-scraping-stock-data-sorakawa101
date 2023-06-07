import streamlit as st
import numpy as np
import pandas as pd
import datetime

# SoftBank Stock data from Stooq.com
# reference https://seanmemo.com/234/

from pandas_datareader import data

import mod


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


st.title('Virtual Stock Trade System')
st.header('Information')


# DF：JPXから取得した銘柄コード一覧をMySQLから取得
df_stock_code = mod.ConnectMySQL_and_GetTable('stock_code_list')
# df_stock_code = pd.read_excel("./src/data_j.xls")


# タブごとに表示分け
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Select", "Search", "Result(Graph)", "Result(Table)", "Result(Metric)"])

# TODO tabじゃなくてgallery表示にして選択しつつグラフを見れるようにしたい
# TODO グラフは複数日付を同時に見られるようにしたい（柳谷くんの参考に）
# 情報を見たい銘柄コード・開始日・最終日を入力
with tab1:
    # 銘柄コードを入力
    stock_code = st.text_input(
        'Stock Code is: ',
        '9984.JP'
    )

    # データ取得の開始日
    start = st.date_input(
        'Start Date is: ',
        # デフォルト値は約3ヶ月前の日付
        datetime.date.today() - datetime.timedelta(weeks=12)
    )
    st.write('Start Date is: ', start)

    # データ取得の最終日
    end = st.date_input(
        'End Date is: ',
        # デフォルト値は今日の日付
        datetime.date.today()
    )
    st.write('End Date is: ', end)

    corp = mod.StockCodeStr_to_CorpName(stock_code)

    # 現在洗濯中の情報を表示
    st.info(f'現在、\"{corp}\"\tの\t{start}〜{end}\tにおける株価データを表示中', icon=None)

    # DF：指定した銘柄の株式データ
    df_stock_data = data.DataReader(stock_code, 'stooq', start, end)


# 銘柄検索用の表
with tab2:
    # 表の生成
    # ! st.dataframeは通常だと千区切りのコンマが入ってしまうのでフォーマットを変更
    st.dataframe(df_stock_code.style.format(
        thousands=''), use_container_width=False)


# 出来高のエリアチャート
with tab3:
    # 選択中の企業名を表示
    st.subheader(f'Selected Corp is: {corp}')

    # データの選択
    options = st.multiselect(
        'What are your interesting datas?',
        ['Open', 'High', 'Low', 'Close', 'Volume'],
        ['Volume']
    )

    # 図の描画
    st.bar_chart(df_stock_data.loc[:, options])
    st.line_chart(df_stock_data.loc[:, options])


# 取得した株価データの表
with tab4:
    # 選択中の企業名を表示
    st.subheader(f'Selected Corp is: {corp}')
    # 表の生成
    st.table(df_stock_data)


with tab5:
    # 選択中の企業名を表示
    st.subheader(f'Selected Corp is: {corp}')

    # 各データの前日比
    st.write(f'前日比({end})')
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Open",     df_stock_data.iat[0, 0], int(
        df_stock_data.iat[0, 0]-df_stock_data.iat[1, 0]))
    col2.metric("High",     df_stock_data.iat[0, 1], int(
        df_stock_data.iat[0, 1]-df_stock_data.iat[1, 1]))
    col3.metric("Low",      df_stock_data.iat[0, 2], int(
        df_stock_data.iat[0, 2]-df_stock_data.iat[1, 2]))
    col4.metric("Close",    df_stock_data.iat[0, 3], int(
        df_stock_data.iat[0, 3]-df_stock_data.iat[1, 3]))
    col5.metric("Volume",   df_stock_data.iat[0, 4], int(
        df_stock_data.iat[0, 4]-df_stock_data.iat[1, 4]))
