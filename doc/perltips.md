# Perlの小技集

- 頭に0をつけて数字を13桁にする
```
$article_id = sprintf("%013d", $pmid)
```

- 正規表現でメタ文字をメタ文字として処理しない
  - /マッチさせるもの/ とするが、えてしてマッチさせるものを変数でもってforeachするときなど、この中に Na+ のように * や + などが入っていると`Quantifier follows nothing in regex; marked by <-- HERE in m/+ <-- HERE` などと怒られる
  - `quotemeta`関数を使ってエスケープして使う
```
$match = quotemeta($match);
if ($target =~ /$match/) {
  ...
}
```
