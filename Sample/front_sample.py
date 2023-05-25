import streamlit as st
import numpy as np
import pandas as pd
import datetime

# SoftBank Stock data from Stooq.com
# reference https://seanmemo.com/234/

from pandas_datareader import data


st.title('Streamlit Sample')


"""
Run Command is:
```
streamlit run front_sample.py
```
\b
"""


# 企業コードを入力
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


"\b"


# データフレーム作成
df = data.DataReader(stock_code, 'stooq', start, end)

# 図の描画
st.line_chart(df.loc[:, 'Volume'])


# 表の生成
st.table(df)
# st.line_chart(df.loc[:, 'Volume'])
# st.area_chart(df.loc[:, ['Open', 'High', 'Low', 'Close']])
# st.bar_chart(df)
