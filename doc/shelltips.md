# shellの小技集

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

### 再帰的にgrepする
```
$ grep -r pattern ./ --include=*.gb
```
- 再帰的に検索するのは -r オプション
- patternの後は検索対象だが *.gb などとワイルドカードを使うとそんなファイルはないと怒られる
- -r を用いた場合、検索対象はディレクトリを指定する
- 各ディレクトリでファイルの種類などを絞り込むときは `--include=`を用いる。
- ファイルの種類を複数指定する場合は`--include={*.gb,*.fasta}`などとする

