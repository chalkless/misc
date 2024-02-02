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
