# shellの小技集

### 再帰的にgrepする
```
$ grep -r pattern ./ --include=*.gb
```
- 再帰的に検索するのは -r オプション
- patternの後は検索対象だが *.gb などとワイルドカードを使うとそんなファイルはないと怒られる
- -r を用いた場合、検索対象はディレクトリを指定する
- 各ディレクトリでファイルの種類などを絞り込むときは `--include=`を用いる。
- ファイルの種類を複数指定する場合は`--include={*.gb,*.fasta}`などとする

## 別のユーザーになるあれこれ
### 単純にそのユーザーになる
```
$ su - otherusr
```
- （otherusrの）パスワードが聞かれる
- 別のユーザーを作った時の確認など

### パスワードを訊かれずにそのユーザーになる
```
$ sudo -s -H -u otherusr
```

## shell script

### 条件に合致するファイルでshell script
- 例：*.txt　を *.out.txt　にコピーする
```
$ for nm in *.txt;
    do cp $nm ${nm%txt}out.txt ;
  done
```

### ファイルリストがあって、1行ずつ処理する
```
$ for nm in `cat filelist.txt`;
    do cp $nm ${nm%txt}out.txt ;
  done
```

### lsした結果の一部について処理
```
$ ls
2022-1.re.zip  NBRC107333  NBRC115139  NBRC12953  NBRC14893
2022-1.zip     NBRC113350  NBRC115160  NBRC13169  NBRC15545
NBRC100001     NBRC113783  NBRC12689   NBRC13245  NBRC3776
NBRC100140     NBRC113806  NBRC12708   NBRC13287  NBRC3972
NBRC100498     NBRC114412  NBRC12875   NBRC13315  conv.na.240201-1.txt
$ for nm in `ls | grep NBRC`;
    do ... ;
  done
```
