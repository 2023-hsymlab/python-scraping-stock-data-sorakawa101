import streamlit as st
import numpy as np
import pandas as pd
import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# SoftBank Stock data from Stooq.com
# reference https://seanmemo.com/234/

from pandas_datareader import data

import mod


# st.title('Virtual Stock Trade System')
# st.header('Information')


# DF：JPXから取得した銘柄コード一覧をMySQLから取得
df_stock_code = mod.ConnectMySQL_and_GetTable('stock_code_list')
# df_stock_code = pd.read_excel("./src/data_j.xls")

with st.sidebar:
    # 銘柄コードを入力
    stock_code = st.text_input(
        '銘柄コード',
        '9984.JP'
    )

    # データ取得の開始日
    start = st.date_input(
        '開始日',
        # デフォルト値は約3ヶ月前の日付
        datetime.date.today() - datetime.timedelta(weeks=12)
    )

    # データ取得の最終日
    end = st.date_input(
        '終了日',
        # デフォルト値は今日の日付
        datetime.date.today()
    )

    corp = mod.StockCodeStr_to_CorpName(stock_code)

    # 現在洗濯中の情報を表示
    st.info(f'現在、\"{corp}\"\tの\t{start}〜{end}\tにおける株価データを表示中', icon=None)

    # DF：指定した銘柄の株式データ
    df_stock_data = data.DataReader(stock_code, 'stooq', start, end)




# 選択中の企業名を表示
st.subheader(f'{corp}（{start}~{end}）')

# 各データの前日比
st.write(f'前日比')
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


with st.expander("前週・前月比"):
    # 各データの前週比
    st.write(f'前週比')
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Open",     df_stock_data.iat[0, 0], int(
        df_stock_data.iat[0, 0]-df_stock_data.iat[5, 0]))
    col2.metric("High",     df_stock_data.iat[0, 1], int(
        df_stock_data.iat[0, 1]-df_stock_data.iat[5, 1]))
    col3.metric("Low",      df_stock_data.iat[0, 2], int(
        df_stock_data.iat[0, 2]-df_stock_data.iat[5, 2]))
    col4.metric("Close",    df_stock_data.iat[0, 3], int(
        df_stock_data.iat[0, 3]-df_stock_data.iat[5, 3]))
    col5.metric("Volume",   df_stock_data.iat[0, 4], int(
        df_stock_data.iat[0, 4]-df_stock_data.iat[5, 4]))


    # 各データの前月比
    st.write(f'前月比')
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Open",     df_stock_data.iat[0, 0], int(
        df_stock_data.iat[0, 0]-df_stock_data.iat[23, 0]))
    col2.metric("High",     df_stock_data.iat[0, 1], int(
        df_stock_data.iat[0, 1]-df_stock_data.iat[23, 1]))
    col3.metric("Low",      df_stock_data.iat[0, 2], int(
        df_stock_data.iat[0, 2]-df_stock_data.iat[23, 2]))
    col4.metric("Close",    df_stock_data.iat[0, 3], int(
        df_stock_data.iat[0, 3]-df_stock_data.iat[23, 3]))
    col5.metric("Volume",   df_stock_data.iat[0, 4], int(
        df_stock_data.iat[0, 4]-df_stock_data.iat[23, 4]))




# 出来高のエリアチャート

# figを定義
fig = make_subplots(rows=4, cols=1, shared_xaxes=True, vertical_spacing=0.05, row_width=[0.2, 0.2, 0.2, 0.7], x_title="日付")


# ローソク足チャートを表示
fig.add_trace(
    go.Candlestick(x=df_stock_data.index, open=df_stock_data["Open"], high=df_stock_data["High"], low=df_stock_data["Low"], close=df_stock_data["Close"], showlegend=False),
    row=1, col=1
)

# 移動平均線
mod.Get_SimpleMovingAverage(df_stock_data)
fig.add_trace(go.Scatter(x=df_stock_data.index, y=df_stock_data["SMA20"], name="SMA20", mode="lines"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_stock_data.index, y=df_stock_data["SMA50"], name="SMA50", mode="lines"), row=1, col=1)
fig.add_trace(go.Scatter(x=df_stock_data.index, y=df_stock_data["SMA200"], name="SMA200", mode="lines"), row=1, col=1)

# MACD
mod.Get_TechnicalIndex(df_stock_data)
fig.add_trace(go.Scatter(x=df_stock_data.index, y=df_stock_data["MACD"], mode="lines", showlegend=False), row=3, col=1)
fig.add_trace(go.Scatter(x=df_stock_data.index, y=df_stock_data["Signal"], mode="lines", showlegend=False), row=3, col=1)

# RSI
fig.add_trace(go.Scatter(x=df_stock_data.index, y=df_stock_data["RSI"], mode="lines", showlegend=False), row=4, col=1)


# 出来高の棒グラフを表示
fig.add_trace(
    go.Bar(x=df_stock_data.index, y=df_stock_data["Volume"], showlegend=False),
    row=2, col=1
)
# Layout
fig.update_layout(
    # title={
    #     "text": "トヨタ自動車(7203)の日足チャート",
    #     "y":0.9,
    #     "x":0.5,
    # },
    height=700
)

fig.update_xaxes(
    rangebreaks=[dict(values=mod.Get_Unnecessary_DateList(df_stock_data))], # 非営業日を非表示設定
    tickformat='%Y/%m/%d' # 日付のフォーマット変更
)

# 日付のフォーマット変更
fig.update_xaxes(tickformat='%Y/%m/%d')

# ラベル名の設定とフォーマット変更（カンマ区切り）
fig.update_yaxes(separatethousands=True, title_text="株価", row=1, col=1)
fig.update_yaxes(title_text="出来高", row=2, col=1)
fig.update_yaxes(title_text="MACD", row=3, col=1)
fig.update_yaxes(title_text="RSI", row=4, col=1)

# 棒グラフを非表示にする場合は以下を適用
fig.update(layout_xaxis_rangeslider_visible=False)
# 描画
st.plotly_chart(fig, use_container_width=True)




# 取得した株価データの表
# 選択中の企業名を表示
# 表の生成
st.table(df_stock_data)
