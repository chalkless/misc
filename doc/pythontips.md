# Python tips

## APIを叩く
```
url_base = "https://www.nite.go.jp/nbrc/dbrp/"
url_search  = "api/strainsearch"

term_search = sys.argv[1]

url_search_q = url_base + url_search
param = {'data_group_SP': term_search }
response = requests.get(url_search_q, params = param)
data = response.json()        # ここの行はデータ形式によって受け方を変える（json()の部分）
```

## if文
```
if response.status_code == 200:
    data = response.json()
    print(data)
elif response.status_code == 404:
    print("Not found")                                                          
else:
    print("Error: ", response.status_code)
```

## データの型を確認する
```
print(type(data))

<class 'dict'>

実際の中身
{'status': {'success': True, 'message': ''}, 'result': {'data': [{'data_id': 'STNB0000000102181', 'data_title': 'Hydrogenobacter thermophilus NBRC 102181の株情 報', 'data_group': '微生物株情報'}]}}
```

## dict型の処理
```
rslt = data['result']

{'data': [{'data_id': 'STNB0000000102181', 'data_title': 'Hydrogenobacter thermophilus NBRC 102181の株情報', 'data_group': '微生物株情報'}]}
```

```
# 連続というか入れ子で書ける
rslt = data['result']['data']

[{'data_id': 'STNB0000000102181', 'data_title': 'Hydrogenobacter thermophilus NBRC 102181の株情報', 'data_group': '微生物株情報'}]
```

## dic型データのarrayの処理
```
for ele in rslt:
    for key, value in ele.items():
        print(key, value)

data_id STNB0000000102181
data_title Hydrogenobacter thermophilus NBRC 102181の株情報
data_group 微生物株情報
```

## arrayへのデータ追加
```
list_strain = []
...
list_strain.append(strain_id)
```

## 引数の処理
```
from argparse 

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str)
parser.add_argument('-i', '--pmid', type=str)
args = parser.parse_args()

file_in = args.file
pmid_in = args.pmid
```

## オブジェクトの中身の確認
```
import pprint

pprint.pprint(obj)
```

## 例外処理
```
try:
    ...
except:
    ...
```

## 正規表現
```
import re

medlinedate = "2019 May-Jun,"
pattern = "\d{4}"

date_matched = re.match(pattern, medlinedate)
year = date_matched.group()
```

## 0埋め
```
pmid = "30123456"
id_pmid = "PMID" + pmid.zfill(13)      # str.zfill(0埋め後の桁数)
# output: PMID0000030123456
```

## 改行の除去
- `rstrip`を用いる。文字列の左側も取り除く`strip`もある。
- `str.rstrip()`のように用いるが、このとき、`str`は書き換えられず、結果をコピーして用いないといけないことに注意
 
```
# ダメな例
with open(file_in) as f:
    for doi in f.readlines():
        doi.strip()           # ここの行
```
```
# ダメな例：結果
10.1002/9781118960608.gbm00513.pub2              # ここに余計な改行が入っている
	10.1002/9781118960608.gbm00513.pub2
```
```
# よい例
with open(file_in) as f:
    for doi in f.readlines():
        doi_strip = doi.strip()           # ここの行
```
```
# よい例（別バージョン）
with open(f_in) as f:
    list = [s.rstrip() for s in f.readlines()]
```

## 「‘str’ object is not callable」エラー
- strは予約語だが、（えてしてstringの略としての）変数として何かを代入してしまったために起きるエラー。`del str`する。
- 特にGoogle Colab内だと1回どこかで変数を消去しないとプログラムを書き換えても変数内に値が残っているので注意
