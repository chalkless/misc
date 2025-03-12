# Apacheの設定

## Apacheのインストール


## ファイルの権限の設定
- たとえば `/home/user/public_html` を公開したいというときに、共用機だとapacheユーザーにはアクセスしてくれないと困るが、他のユーザーにはアクセスしてほしくないということがある
  - 蛇足ながら ユーザー名が httpd や www のときもある
- `setfacl` コマンドで権限を設定する
```
$ setfacl -m u:apache:rx /home/user
```
- 確認は`getfacl`コマンド
```
$ getfacl /home/user
# file: user
# owner: user
# group: group
user::rwx
user:apache:r-x
group::---
mask::r-x
other::---
```
- `ls -l`すると何かしらの特殊な権限が付与されているのがわかるように+がついている
```
$ ls -alF /home
...
drwxr-x---+  4 user      group       147  3月 12 16:45 user/
drwxr-x---  4 anotheruser      group       147  3月 11 11:30 anotheruser   ← こちらは何もしていない例
...
```

## ApacheをSSL化する
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
Certificate is saved at: /etc/letsencrypt/live/domainname.jp/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/domainname.jp/privkey.pem
This certificate expires on 2024-05-19.
These files will be updated when the certificate renews.
Certbot has set up a scheduled task to automatically renew this certificate in the background.

Deploying certificate
Successfully deployed certificate for domainname.jp to /etc/apache2/sites-available/000-default-le-ssl.conf
Congratulations! You have successfully enabled HTTPS on https://domainname.jp
...
（証明書が作成される）
```
```
# SSLモジュールの有効化
$ sudo a2enmod ssl
```
```
$ cd /etc/apache2/sites-available/
$ sudo cp 000-default-le-ssl.conf domainname.jp.conf    ... 設定が000-default-le-ssl.confに作られるので自分のドメイン用にコピーして編集（メールアドレスなど）
$ sudo vi domainname.jp.conf

$ sudo a2ensite domainname.jp    ... 自分のドメインの設定を有効化
$ sudo systemctl reload apache2
```
### SSL証明書の更新
- 最近はcronに登録しなくても更新するプログラムがついているのでserviceに登録して定期的にアップデートするようにする
```
# 試しに動くかの確認
$ sudo certbot renew --dry-run
Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Processing /etc/letsencrypt/renewal/domainname.jp.conf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Account registered.
Simulating renewal of an existing certificate for domainname.jp

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Congratulations, all simulated renewals succeeded: 
  /etc/letsencrypt/live/domainname.jp/fullchain.pem (success)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 更新設定を有効化
$ sudo systemctl status certbot.timer
● certbot.timer - Run certbot twice daily
     Loaded: loaded (/lib/systemd/system/certbot.timer; enabled; vendor preset:>
     Active: active (waiting) since Mon 2024-02-19 23:08:00 JST; 1h 19min ago
    Trigger: Tue 2024-02-20 11:08:07 JST; 10h left
   Triggers: ● certbot.service

 2月 19 23:08:00 blenny systemd[1]: Started Run certbot twice daily.
```

