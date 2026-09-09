# 自宅サーバーに外部からアクセスする
## 概要
- あとで書く

## cloudflareによる外部からのアクセス
### 準備編
#### アカウント作成
- cloudflareのサイト https://cloudflare.com/ に行く
- アカウントを作る。メールアドレスがあればいいし、GoogleとかGitHubのアカウントでログインすることもできる
#### ドメイン登録
- 自分の持っているドメインを登録したり、cloudflareでドメインを取ることもできる
- ポータルサイトから Connect a domain　/ Transfer a domain / Create a domain のどれかを選ぶ。今回はConnectで。
- ドメインの名前を入れる。とりあえず他はそのまま
- プランを選ぶ。とりあえずFreeで
- Review your DNS records：DNS情報をスキャンしてくれて表示される。問題なければContinue to activation
- ネームサーバー（＝IPアドレスがかわったことを知らせるサーバー）の情報を元のところからcloudflareのに変更する。変更内容は画面に表示されている
#### cloudflaredのインストール
- 公開したいサーバーでcloudflaredのツールを入れる（末尾にdがついていることに注意）
```
apt install cloudflared
```
### トンネルの作成
#### トークンの入手
- サーバーとcloudflareのサイトで認証というか対応づけをするためにトークンを得る
```
cloudflared tunnel login
```
- ブラウザが立ち上がるか、もしくはURLが表示されるのでそれをブラウザで開く
- どのドメインを使うかリストが出ているので選択する
- ブラウザではこのウインドウは消していいよ、と出る
- サーバーのターミナル側では`~/cloudflared/cert.pem`が書き込まれる
#### トンネルの作成
```
sudo cloudflared tunnel create <トンネル名>
```
- なんかエラーが出たのだが
```
2026-09-09T14:58:32Z ERR Cannot determine default origin certificate path. No file cert.pem in [~/.cloudflared ~/.cloudflare-warp ~/cloudflare-warp /etc/cloudflared /usr/local/etc/cloudflared]. You need to specify the origin certificate path by specifying the origincert option in the configuration file, or set TUNNEL_ORIGIN_CERT environment variable originCertPath=
failed to create tunnel: couldn't create client to talk to Cloudflare Tunnel backend: Error locating origin cert: client didn't specify origincert path
```
- ということで`originCertPath=`つけて実行 → また怒られた
```
$ sudo cloudflared tunnel create tunnelname originCertPath=~/.cloudflared
"cloudflared tunnel create" requires exactly 1 argument, the name of tunnel to create.
See 'cloudflared tunnel create --help'.
```


## ngrokによる外部からのアクセス
- あとで書く
