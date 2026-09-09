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
- cloudflareのサイトに行く
- Zero trust → Networks → Tunnels & Mesh
- トンネル名を入れる
- 指示に従って実行
```
sudo cloudflared service install eyJhIjo...
```
- ブラウザに戻って次のページへ
- 情報を入れる。ネットワークを選択する。serviceはssh://localhost:22

### クライアント側の設定
- cloudflaredのインストール（Macの場合）
```
brew install cloudflared
```
- サーバー情報の設定：.ssh/configに以下を書く
```
Host <接続先>
	HostName <ドメイン名>
	ProxyCommand /opt/homebrew/bin/cloudflared access ssh --hostname %h
```

## ngrokによる外部からのアクセス
- あとで書く
