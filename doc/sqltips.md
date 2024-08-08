### DBサーバーへのログイン
```
# PostgreSQL
$ psql -p 5432 -U username -d database
（パスワードを訊かれる）
```

### DBサーバーからのログオフ
```
# PostgreSQL
prompt=> \q      # 入力するのは \q　だけである
```

### データを見る
```
PROMPT=> select * from SCHEMA.TABLE;
```
- PostgreSQLはスキーマ名を入れないと得てして動かない。
- 先頭10件だけなどはlimit 10をつける

### データベースのリストを取得
```
# PostgreSQL
PROMPT=> \l
```

### テーブルのリストを取得
```
# PostgreSQL
PROMPT=> \dt SCHEMA.*
```


### テーブルのdump





