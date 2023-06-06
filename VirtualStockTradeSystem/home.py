import streamlit as st


st.title('Virtual Stock Trade System')
st.header('Home')

"""
Run Command is:
```
streamlit run home.py
```
"""

# MySQLと接続
# Initialize connection.
conn = st.experimental_connection('mysql', type='sql')

# DF：JPXから取得した銘柄コード一覧データをMySQLから取得
# Perform query.
df_stock_code_list = conn.query('SELECT * from stock_code_list;', ttl=600)
