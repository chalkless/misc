# 新しくMacを買ったときのSet up
- DRY本（2版）とか見ればいいんじゃ。。。（とも言ってられないので



## コマンドを使う用意
### xcodeのコマンドのインストール
```
$ xcode-select --install
```
- デベロッパーツールを入れるか（GUIな）ポップアップが出るので、同意して進める

### Homebrewのインストール
- Homebrewでググって指示に従う
```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
(次のコマンドを実行しろというメッセージが最後に出る)
$ echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/nakazato/.zprofile
$ eval "$(/opt/homebrew/bin/brew shellenv)"
```



# shellの設定
- 多分、後で独立したページにすると思う
```
[.bashrc]
PS1='\[\e[32m\]\u@\h:\w\$ \[\e[0m\]'
```

```
[.zshrc]
PROMPT='%F{green}%n@%m:%~$ %f'
```

# SSHの設定
- 設定は`~/.ssh/`に作成されるので、ここを見るとどこまで設定されているかわかるはず
- 公開鍵を作成する
```
$ ssh-keygen -t rsa
```
    - 通常は`id_rsa`と`id_rsa.pub`が作成される。変えたい時は上のコマンドの途中で名称を指定できる
    - Permissionは各々600と644っぽい。
- 接続の設定
    - どうにかしてサーバー側に接続する（これまで使っていた機器でなど）
    - サーバー側の`~/.ssh/authorized_keys`にクライアント側（今回、作った側）の`id_rsa.pub`の中身を追記する
    - サーバー側にクライアント側の`id_rsa.pub`をコピーし、`cat`コマンドなどでファイル連結などしてもよい
- 多段接続の設定
    - `~/.ssh/config`に設定を書く
    - 雑：
    ```
ServerAliveInterval 60
ServerAliveCountMax 3
    ```
    - 多段接続（例）
    ```
    Host target_nickname
    HostName target.server.name
    User username
    ProxyCommand ssh -p 8080 proxy.server.name -W %h:%p
    ```
    
