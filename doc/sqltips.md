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
```
$ pg_dump -p 5432 -U sqluser -E UTF8 --file=/home/user/backup/backup_`date "+%Y_%m_%d_%H_%M_%S"`.dump -Fp dbname
```
- この場合、backupフォルダがないと怒られる
- できるファイルの中身はデータとSQL文と思えば良い

```
# restoreするとき
$ psql -p 5432 -U sqluser -d dbname -f filename
```

### SQLの外からSQLの結果を得る
```
# PostgreSQL
$ psql -p 5432 -U username -d database -c "ここにSQL文"
（パスワードを訊かれる）
```

### SQLの中からテーブル内容をファイルに吐く（がたまに怒られる）
```
PROMPT=> COPY schema.table TO '/home/user/filename' WITH CSV HEADER delimiter '  '；
```
- たまにユーザーに権限がないと怒られるので次を使う

### SQLの外からテーブル内容をファイルに吐く
```
$ psql -p 5432 -U username -d database -c "\COPY schema.table TO '/home/user/filename' WITH CSV HEADER delimiter '  '；"
```
- copyの前に\がついている点に注意


