# Ubuntu setup
'23-6-10に作業

## インストールメディアの作成など
- [Ubuntuのサイト](https://jp.ubuntu.com/)
- ヘッダの右の方にあるダウンロードから
- 「Ubuntu Desktop 22.04.2 LTS」をダウンロード。こちらは安定版。LTSのつかない「Ubuntu Desktop 23.04」は開発版
- ダウンロードすると「ubuntu-22.04.2-desktop-amd64.iso」がダウンロードされる。
  - amd64 ?　と思ったのだが、（ようするに今回はIntel CPUなんだが）、ppc64とかarm64しかないし、ubuntuではこう書くとあったので（実際にうまくいったし）気にせずにダウンロード
- https://virment.com/making-installusb-ubuntu-mac/ を参考に形式変換してインストール用USBスティックを作る（８GBあればいいだろうということになっているようだ）

```
$ hdiutil convert -format UDRW -o ubuntu-22.04.2-desktop-amd64.img ubuntu-22.04.2-desktop-amd64.iso     # iso -> img
$ mv ubuntu-22.04.2-desktop-amd64.img.dmg ubuntu-22.04.2-desktop-amd64.img   # .dmg　が付くので削る
$ diskutil list
　　　...　 　 # USBスティックがどこに認識されているか確認（例：/dev/disk1）
$ diskutil unMountDisk /dev/disk1s1      # ディスクをアンマウントする
$ sudo dd if=ubuntu-22.04.2-desktop-amd64.img of=/dev/disk1s1 bs=1m
```

- しばらくかかる。これはコマンドでやるやり方だが、もっと簡便にやるツールもあるらしい。

## インストール（起動まで）
- USBスティック（インストールメディア）を挿してインストーラー起動
  - 起動しないときはBIOS画面に行ってUSB起動するようにするとか、既存システムが起動してしまうときはBIOSでHDD/SSDより先にUSBを見るようにする
- 「Try or Install Ubuntu」 を選択
- 言語が選べるので日本語にする
- 「Ubuntuをインストール」
- キーボードを選択
- 「通常のインストール」 or　「最小のインストール」：今回はサーバーとしての利用なのでどうせモニタとかつながんし最小で
- インストールの種類
  - ここでパーティションの切り方など訊かれる
  - 「ディスクを削除してUbuntuをインストール」が通常。自分で変えたかったら「その他」から選べる
  - 今回は、SSD+HDD×２という構成なので、ここでどうHDDをマウントするかとか選べる
  - /dev/sda1とかをダブルクリックしたりすると設定ができるようだ
  - のだが、SSDを/ねって先に進もうとすると、EFIシステムパーティションを作れとか言われる。そういえばswap領域も指定せねばならない。。。
  - /homeをHDDにマウントしたかったのだが、システムの部分の割り振りはUbuntuにおまかせすることとして今回は通常で
  - CentOSだと試しにこうやってみたよ、とか出るので、それを元に自分でいじれたんだけどね
- 途中で更新分をインストールしていいかとか、タイムゾーンとか訊かれる
- パソコン名とユーザー情報を入れる：「あなたの名前」は空白。ユーザー名とパスワードはLinuxのユーザー名になるのでそれなりに慎重に。
  - rootのパスワード設定はここではされない。逆にいつまでもされないので、後で明示的に指定する
- インストールメディアをはずして一旦再起動（とメッセージが出る）
- オンラインアカウントとの接続がなんとかとか訊かれるが放っておいていい
- 無事に起動してとりあえず使えるように。これから追加のセッティングをする。

## root のパスワード設定
- https://qiita.com/_toki/items/cced337d72103ed4387c を見た

```
$ sudo passwd root
Enter new UNIX password:○○○○○○ ← 設定をしたいrootパスワード
Retype new UNIX password:○○○○○○ ← 設定をしたいrootパスワードを再度入力
passwd: password updated successfully
```

## 増設HDDのマウント
- SSDにシステムを（デフォルトの設定で）入れており、増設したHDDは手つかずなので、フォーマットしてマウントして、という作業が必要
- なんかコマンドでやる方法がうじゃうじゃヒットするんだが、うまくやらないととコケるのでディスクユーティリティを使う（なぜここでひよるw）
- アプリのリストからユーティリティの中のディスクユーティリティだかを起動
- 左にディスクのリストが出ると思うのでクリックすると右側に詳細が出てくる。
- ボリューム欄に歯車マークなどあるので、そこをクリックして、まずは「パーティションを初期化」 → ext4を選択 →　フォーマットされる
- 再びボリューム欄の歯車マークから「マウントオプションを編集」
  - 「起動時にマウント」はチェック
  - 「ユーザーインターフェースに表示」にチェックを入れるとGUIでそのマウント先が画面に表示されるが別にいらないのでチェックを外す
  - nosuid,nodevなどなど書かれているが、そのままでもいいような気もするが、結局、defaults,nofailにする
  - マウントポイントを自分の好きなように編集。今回は /data と /share　（２本あるので）
  - ファイルシステムの種類はautoでよい
- 初期設定だと自分のユーザーの所有権で700のpermissiionでマウントされる
- いろいろ設定しても変わらないのだが、ふと、マウントするときはもともとあるディレクトリにマウントされると気づき、chownとchmodで好きなように設定すればいいのではと変えたらうまく行った。今回はrootの所有で７７７にしてある（７５５でもいいのかもしれなん。/homeなどはそうなっているし）

## 増設HDDに/homeを移動する
- 現状だと /　の下に /home　があるので（当たり前）、SSDだし、容量も足りなくなるかもなのでHDDに移動させたい
- https://www.exceedsystem.net/2020/08/22/how-to-move-the-home-directory-to-another-drive/ を参考に
- リモートアクセスでなく実機で
- シングルユーザーモードにする

```
$ sudo systemctl isolate rescue.target
or
$ sudo systemctl emergency
```

- root になった
- /home　をコピー。日付やpermissionなどなどをうっかり変えられたりして不具合が起きないように cp でなく rsync　を使うのが安全

```
# rsync -auvSAX /home/ /share/home/
```

-　元の /home　をバックアップ（しばらくして不具合が出なかったら消す）

```
# mv /home /home_bak
```

- マウント先のディレクトリを作成

```
# mkdir /home
```

- ディレクトリをディレクトリにマウントというか、強力なシンボリックリンクとしてmountのbindオプションというのがあるらしい。/etc/fstab に記述を追加する
  - これを使うと同じディレクトリに２カ所からアクセスできるそうだ。つまり、今回は　/share/home　を /home にマウントするが、どちらを指定しても同じものが指定されるし、1つ上のディレクトリを指定すれば各々 /share　と /　になる

```
#　fstabに追加
/share/home /home none  bind  0 0
```

- 設定を反映

```
# mount -a
```

- うまくいっているか確認する。lsなりしてみるとか
- 元のモードに戻るなり再起動するなり

```
# 一例
# systemctl isolate graphical.target
```

## リモートで他端末にログインできるようにするための証明書作成
- パスワード認証なら設定は不要。単にSSHすればよろし。
- 証明書を作成する（シンプルバージョン。rsa形式）

```
$ ssh-keygen
（証明書の名前。普通にリターンでよい）
（パスワード）
（パスワード再度）
```

- id_rsa と id_rsa.pub　ができるので、ログイン先に id_rsa.pub　を設置する（authorized_keysに追記する）
- 証明書を作成する（セキュリティが高いバージョン。ecdsa-sha2-nistp256形式）

```
$ ssh-keygen -t ecdsa -b 256
```

- id_ecdsa と id_ecdsa.pub　ができる。
- 普通にsshすれば勝手にどちらの証明書か選んでくれる



## リモートログインを受け付けられるようにする

```
$ systemctl status ssh
# Active (running)　と出れば動いている

# なんかそれっぽいのが出るけどrunningでなかったら起動させる
$ sudo systemctl enable ssh

#　何それみたいに出てきたらopenssh-serverを入れる
$ sudo apt install openssh-server
# これをやれば自動起動も動くと思うが動いてなかったら起動設定をする
```

## インターネット経由でUbuntuマシンにアクセスできるようにする
- Ubuntu側の設定としてIPを固定したい。設定のネットワークでIPを固定にしたのだが、ゲートウェイの設定かDNSの設定かインターネットが疎通せず
- どちらにしろルーターでポートフォワーディングの設定をしないといけない。２２番ポートをUbuntuマシン用に振り出したIPにフォワードするようにしておく
- ついでにルーターのDHCP設定で（今回の場合だが）MACアドレスとIPを指定すれば固定IPとして自動で振ってくれるようなので、UbuntuはDHCPで設定取得することとしてルーター側で固定にすることで解決

## Apacheのインストール
```
$ sudo apt install apache2
```
- これだけでアクセスすると "It works!" ページが出る
- 実体は `/var/www/html/index.html`
- 設定ファイルは　`/etc/apache2/apache2.conf`
- 起動などは `systemctl [start|stop|status] apache2`

### ApacheをSSL化する
- https でアクセスできるようにする
```
# 準備
$ sudo apt install certbot
$ sudo apt install python3-certbot-apache
```
```
#　証明書の作成
$ sudo certbot --apache -d domainname.jp
（メールアドレスや配信の要否について訊かれる）
...
Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/chalk-less.org/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/chalk-less.org/privkey.pem
This certificate expires on 2024-05-19.
These files will be updated when the certificate renews.
Certbot has set up a scheduled task to automatically renew this certificate in the background.

Deploying certificate
Successfully deployed certificate for chalk-less.org to /etc/apache2/sites-available/000-default-le-ssl.conf
Congratulations! You have successfully enabled HTTPS on https://chalk-less.org
...
（証明書が作成される）
```
```
# SSLモジュールの有効化
$ sudo a2enmod ssl
```
```
$ cd /etc/apache2/sites-available/
$ sudo cp 000-default-le-ssl.conf chalk-less.org.conf
$ sudo vi chalk-less.org.conf

$ sudo a2ensite chalk-less.org
$ sudo systemctl reload apache2
```

## vi （vim） の再設定
- インストールしたままのvi　(vim) だと、矢印キーでBとか出たりバックスペースが使えなかったり使いにくい。
- ので、aptでvimを入れ直すとよい
- 参考： https://did2memo.net/2015/12/23/ubuntu-vim-install/

```
$ sudo apt install vim
```
