# 生物多様性情報学おぼえがき
バイオインフォマティクスが（一応の）専門なのに（いやだからこそか）、生物多様性情報学（biodiversity informatics）とは何かを書き留める試み。

## 生物を記録する

- メタデータ：データを説明するデータ
  - ワインのラベルみたいな
  - 毎年買うよね。1本じゃ足りないよね。
- 台湾ビール：もともと国営企業。台湾ビールしかなかった。最近に解禁されていろいろ飲めるように。多様性が低い
- あのときあったお菓子がいつのまにかなくなっている。
  - おにぎりせんべいは名古屋周辺だけとか



## 魚類とは
DNAバーコーディングのデータをとるのに（DNAバーコーディングが盛んな生物分類なので）魚類のデータを使おうと思ったら生物分類がかなり曖昧だった話。

## 名前問題
- 和名と学名
- 生物分類階層
  - (superkingdom) → (kingdom) → (phylum) → 目 (order) → 科 (family) → 属 (genus) → 種 (species)
  - species subspecies form var.
  - 実際は間にいろいろ挟まっていたりする（特に植物）
- 名前は宗教とも呼ばれている
  - NCBI Taxonomy、Catalogue of Life (GBIF Backbone Taxonomy)、GTDB
- 名前は並立する
- 名前はかぶる：名前がかぶったりする問題。（ミヤマクワガタ、Bacillus）
- 菜っ葉問題
- 名前は変わる：学名の変遷。くっついたり離れたり消えたり生まれたり
- 名前はまだない：形態からの名称とDNAからの名称。とりあえずDNAで種みたいなののくくりをつくって、それに呼びやすい名前をアサインしたらよくね?（別にあれもこれも同じ名前とかでもいいからさ）

カルチャーコレクション管理番号

## 命名法などtips
- sic：原文ママ。名前が違ってたりするのはわかっているけど、そのまま記載していますよ、というようなこと
- " " で囲われた学名：オーソライズされていませんよ、ということ。微生物だと、特定の雑誌に載らないとオーソライズされないので。オーソライズには2つ以上のカルチャーコレクションに登録が必要なので、菌株を出したくない場合にわざと出さずにオーソライズされないままにする、ということもある。
- Candidatus：菌体でなく、DNAから命名された微生物に対してつけておく属名。実際の菌体がとれたときに発見者としての優先権がある（ということでいいのかな）



## 機関ID
- GRSciColl：https://scientific-collections.gbif.org/
  - GBIFなどで使われている機関・コレクションのID
  - じーあーるさいこる
  - もともとはSciCollがあった：https://scicoll.org/
  - どうやって作られているかはこのあたりが役に立つかもしれない：https://biss.pensoft.net/browse_user_collection_documents?collection_id=459
- BioCollections：https://www.ncbi.nlm.nih.gov/biocollections/
  - NCBIがやっている機関・コレクションのID
  - GRSciCollと当初は一緒にやっていたところがあるが、その後は独自にデータ追加がされたりして連携をしているわけではない
- Latimer Core：https://ltc.tdwg.org/
  - 略称：LtC
  - コレクション情報を記述するための標準化規格
- ISIL：https://www.ndl.go.jp/jp/library/isil/
  - 図書館及び関連組織のための国際標準識別子(International standard identifier for libraries and related organizations：ISIL)
  - 図書館をはじめ博物館、文書館などの類縁機関に付与される国際的なIDです。
  - なので、大学の図書館や博物館は入るが、大学そのものや研究室単位ではIDは振られない
- ROR：https://ror.org/
  - The Research Organization Registry
  - あーるおーあーる
  - けっこうスカスカで使えるのかどうか?


## 種とは?　株とは?


## タイプ
タイプ標本は最優先で大事にしなければならない

- ラベル
- 普通種/絶滅危惧種


## 生物多様性情報とは
いつ、どこで、誰が、何を、どういう状態でいるのを、何して、それを誰が確認して、今は誰が持っているか

## 生物多様性情報とバイオインフォマティクス
そもそもバイオインフォマティクスとは


## 生物多様性情報（生物多様性データ）とは
- DarwinCore
- RDFとかオントロジーとか

## 実際にデータをいじってみる
- GBIFのデータをPythonとかRで


## 略語など
- ABS (Access and Benefit-Sharing) 遺伝資源の取得の機会及びその利用から生ずる利益の公正かつ衡平な配分
  - 環境省のABSのページ：http://abs.env.go.jp/index.html
- BBNJ (marine Biological diversity Beyond areas of National Jurisdiction) 国家管轄権外区域の海洋生物多様性
  - 「国家管轄権外の海洋生物多様性（BBNJ）の保全及び持続可能な利用」に関する条約（以下、BBNJ協定）
  - https://cilp.oii.tohoku.ac.jp/bbnj/ （東北大国際法政策センター）
- OBIS (Ocean Biodiversity Information System) https://obis.org/
  - J-OBIS https://www.godac.jamstec.go.jp/j-obis/j/


