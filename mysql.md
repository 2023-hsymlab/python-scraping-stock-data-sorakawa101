### MySQL基礎

### 用語

![用語早わかり図](https://academy.gmocloud.com/wp/wp-content/uploads/2016/04/160425_DBword_04.png "用語早わかり図")


---
### MySQL操作方法

#### 起動〜終了
- MySQLの起動
```
brew services start mysql
```
※ バックグラウンドですでに起動済みの場合は不要
※ 再起動は `start → restart`

- ログイン
```
mysql --user=root --password
```
もしくは
```
mysql -u root -p
```
コマンド実行後 `Enter password:` と表示されるのでパスワードを入力。
ログインに成功すると `mysql>`という表示に切り替わる。

- ログアウト
```
exit;
```
`Bye` と表示されればログアウト完了。


- MySQLの停止
```
brew services stop mysql
```

---
#### DBの基本操作
**※ クエリ実行時、末尾に`;`を忘れない！**

##### 1. DBの作成
- DBの表示
```
SHOW databases;
```
※ `database` ではなく `databases`

- DBの作成
```
CREATE database (DBの名前);
```

##### 2. テーブルの作成
- DBの選択
```
USE (DBの名前)
```
テーブルを作成したいDBを選択する。

- テーブルの表示
```
SHOW tables;
```
※ `table` ではなくい `tables`



---
#### 【参考】
1. [Progate MySQLの開発環境を用意しよう（macOS）](https://prog-8.com/docs/mysql-env)
2. [Progate MySQLでデータベースを作成しよう](chrome-extension://igiofjhpmpihnifddepnpngfjhkfenbp/loading.html)
3. [パイワーク！ PythonでMySQLを操作する（PyMySQL）](https://python-work.com/pymysql/)
