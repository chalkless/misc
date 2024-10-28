# SQL関連の使い方（ほぼPostgreSQL）

## ログインログオフ関連

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

## データ閲覧関連

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

## データの設計確認
### データの型確認
```
PROMPT => \d SCHEMA.TABLE
                       テーブル"SCHEMA.TABLE"
             列             |        タイプ         | 照合順序 | Null 値を許容 | デフォルト
----------------------------+-----------------------+----------+---------------+------------
 id                         | character varying(30) |          | not null      |
 scientific_name            | text                  |          | not null      |
 strain_no                  | text                  |          | not null      |
 taxonomy_id                | integer               |          | not null      |
 gtdb_id                    | text                  |          |               |
 history                    | text                  |          |               |
 country_CODE               | character varying(2)  |          | not null      |
 is_type_strain             | boolean               |          | not null      |
インデックス:
    "table_pkc" PRIMARY KEY, btree (id)
```

## dump

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
```
PROMPT=> \COPY schema.table TO '/home/user/filename' WITH CSV HEADER delimiter '  '；
```
- copyの前に\をつけただけ。


### SQLの外からテーブル内容をファイルに吐く
```
$ psql -p 5432 -U username -d database -c "\COPY schema.table TO '/home/user/filename' WITH CSV HEADER delimiter '  '；"
```
- 前項のやりかたをSQLの外から実行しただけ。copyの前に\がついている点に注意


## データを更新する
- 安全運転

```
PROMPT => CREATE TABLE schema.table_new (LIKE schema.table_original including all);      ← テーブル定義をそのままに空のテーブルを作る
PROMPT => \COPY schema.table_new from '/home/path/table.tab' WITH CSV DELIMITER '  '     ← タブ区切りファイルを取り込む。最後の ' 'の間はタブ。E'\t' と書いてもよい。ヘッダ行がある場合はHEADERも記述する
PROMPT => ALTER TABLE schema.table_original RENAME TO table_backup;      ← table_original → table_backup。なぜかリネーム先にschemaをつけるとエラーになる
PROMPT => ALTER TALBE schema.table_new RENAME TO table_original;         ← table_new → table_original
```

