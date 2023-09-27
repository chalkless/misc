# Python tips

* APIを叩く
```
url_base = "https://www.nite.go.jp/nbrc/dbrp/"
url_search  = "api/strainsearch"

term_search = sys.argv[1]

url_search_q = url_base + url_search
param = {'data_group_SP': term_search }
response = requests.get(url_search_q, params = param)
```

* if文
```
if response.status_code == 200:
    data = response.json()
    print(data)                                                                
else:
    print("Error: ", response.status_code)
```

* データの型を確認する
```
print(type(data))

<class 'dict'>

実際の中身
{'status': {'success': True, 'message': ''}, 'result': {'data': [{'data_id': 'STNB0000000102181', 'data_title': 'Hydrogenobacter thermophilus NBRC 102181の株情 報', 'data_group': '微生物株情報'}]}}
```

* dict型の処理
```
rslt = data['result']

{'data': [{'data_id': 'STNB0000000102181', 'data_title': 'Hydrogenobacter thermophilus NBRC 102181の株情報', 'data_group': '微生物株情報'}]}
```

```
# 連続というか入れ子で書ける
rslt = data['result']['data']

[{'data_id': 'STNB0000000102181', 'data_title': 'Hydrogenobacter thermophilus NBRC 102181の株情報', 'data_group': '微生物株情報'}]
```

* dic型データのarrayの処理
```
for ele in rslt:
    for key, value in ele.items():
        print(key, value)

data_id STNB0000000102181
data_title Hydrogenobacter thermophilus NBRC 102181の株情報
data_group 微生物株情報
```

* arrayへのデータ追加
```
list_strain = []
...
list_strain.append(strain_id)
```







