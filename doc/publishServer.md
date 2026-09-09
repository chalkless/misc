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

## ngrokによる外部からのアクセス
- あとで書く
