import streamlit as st


st.title('Virtual Stock Trade System')
st.header('Home')

"""
Run Command is:
```
streamlit run home.py
```
"""


# Initialize connection.
conn = st.experimental_connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from mytable;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
