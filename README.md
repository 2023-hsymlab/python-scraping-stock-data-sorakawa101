# Virtual Stock Trade System

株価情報の閲覧と（仮想の）株売買を行えるMPA。

#### 実行方法
`./VirtualStockTradeSystem`で以下のコマンドを叩くと、`localhost:8501`で開く。
```
streamlit run home.py
```

#### ディレクトリ構成
```
.
├── README.md
├── Sample（練習用プログラム置き場）
│   ├── Simple-StockData2.ipynb
│   ├── Simple-StockData3.ipynb
│   ├── Simple_Stock.ipynb
│   ├── Simple_Stock1.ipynb
│   ├── db_sample
│   ├── front_sample.py
│   ├── get_stock_code_list.ipynb
│   └── ranking.ipynb
├── VirtualStockTradeSystem（システム本体）
│   ├── __pycache__
│   │   ├── home.cpython-39.pyc
│   │   ├── mod.cpython-39.pyc
│   │   └── stock_code_list_to_mysql.cpython-39.pyc
│   ├── home.py（システムのメインファイル）
│   ├── mod.py（関数をまとめたファイル）
│   ├── pages（MPAの別ページファイル）
│   │   ├── info.py
│   │   └── mypage.py
│   ├── requirements.txt
│   ├── src（データ置き場）
│   │   ├── companieslist_2023v01.pdf
│   │   └── data_j.xls
│   └── stock_code_list_to_mysql.py（JPXから銘柄コードをMySQLに登録）
├── index.html
└── mysql.md（MySQLのメモ）

6 directories, 22 files
```

