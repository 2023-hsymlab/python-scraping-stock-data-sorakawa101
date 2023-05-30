import streamlit as st
import numpy as np
import datetime
import pandas as pd
import mod


st.title('Virtual Stock Trade System')
st.header('MyPage')


# DF：JPXから取得した銘柄コード一覧
df_stock_code = pd.read_excel("./src/data_j.xls")


# タブごとに表示分け
tab1, tab2, tab3, tab4 = st.tabs(
    ["Buying & Selling", "Confirm & Change", "Result", "Ranking"])


# 情報を見たい銘柄コード・開始日・最終日を入力
with tab1:
    st.write('売買データ入力')
    col_names = ['企業', '売買', '株数量']
    df_list = pd.DataFrame(columns=col_names)

    with st.form("売買データ入力"):

        # 銘柄コード入力
        text_val = st.text_input('銘柄コード', '9984.JP')
        # 売買選択
        radio_val = st.radio("売買選択", ('売', '買'))
        # 株数量入力
        # TODO 銘柄コードと株数量からかかる金額を表示したい
        number_val = st.number_input('株数量', min_value=int(100), step=int(100))

        # TODO ここの入力からInformationのページで情報を確認できるようにしたい。もしくはポップアップ表示したい

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            corp_name = mod.StockCodeStr_to_CorpName(text_val)
            st.write(f'{corp_name}の株を{number_val}株{radio_val}った')
        # TODO フォームの入力をDFとして表に追加したい

    # 今下剤の売買データ
    today = datetime.date.today()
    today = str(today).split('-')
    st.write(f'{today[0]}年{today[1]}月{today[2]}日現在の売買データ')

    st.dataframe(df_list, use_container_width=True)
