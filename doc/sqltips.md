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

- 抽出条件
```
PROMPT=> select * from test.strains where id='ST_0000002209_002';
```

```
PROMPT=> select * from test.strains where id like 'ST_0000002209_002';
```

- シングルクォーテーションにしないと動かない

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

## データ操作
### データ追加
- insert文
- copy文 or \copy文

### シーケンスが対応づいた以外のところにcopyでデータ投入
```
\copy table_name(col2, col3, ...) from '/path/file' with csv delimiter '  ' header
```


### データ削除
```
PROMPT=> DELETE FROM schema.table
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

### テーブルを作る
```
create table schema.table;
```

### シーケンスを作成する
- テーブル中で、行に採番することができて、その番号をシーケンスとして管理する
```
create sequence sequence_name;
```

### データ型の変更
```
PROMPT=> ALTER TABLE schema.table ALTER COLUMN column TYPE type;
（例）alter table schema.genome_info alter column genome_info_id type varchar(30);
```

### ある列にシーケンスを適用
```
alter table table_name alter column_name set default nextval('sequence_name');
```
- すでに別のシーケンスが対応づいていても変更可能

### NOT NULL制約の変更
```
# 制約追加するとき
PROMPT=> ALTER TABLE schema.table ALTER COLUMN column SET NOT NULL;
# 制約削除するとき
PROMPT=> ALTER TABLE schema.table ALTER COLUMN column DROP NOT NULL;
```

### primary keyの変更
```
# 削除する時
alter table table_name drop constraint table_name_pkey;
## unique 属性もついているので以下も（\d tablename したときに一番下に制約が出てくるのでそれを削除する）
alter table table_name drop constraint table_name_id_key;
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
### テーブル名を変える
```
ALTER TABLE schema.table_present RENAME TO table_new;
```

### 前のものをバックアップして新しいデータのテーブルに置き換える例
- 安全運転

```
PROMPT => CREATE TABLE schema.table_new (LIKE schema.table_original including all);      ← テーブル定義をそのままに空のテーブルを作る
PROMPT => \COPY schema.table_new from '/home/path/table.tab' WITH CSV DELIMITER '  '     ← タブ区切りファイルを取り込む。最後の ' 'の間はタブ。E'\t' と書いてもよい。ヘッダ行がある場合はHEADERも記述する
PROMPT => ALTER TABLE schema.table_original RENAME TO table_backup;      ← table_original → table_backup。なぜかリネーム先にschemaをつけるとエラーになる
PROMPT => ALTER TABLE schema.table_new RENAME TO table_original;         ← table_new → table_original
```

