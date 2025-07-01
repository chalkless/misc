# Ubuntuの日々の管理

## OSバージョンの確認
```
$ cat /etc/os-release 
PRETTY_NAME="Ubuntu 22.04.3 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.3 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
```

## rebootの指示
- ログインするとrebootせよ、と指示が出る時がある
```
*** System restart required ***
```

- ログイン状態時でのrebootの要不要確認
```
$ cat /var/run/reboot-required
*** System restart required ***
（不要の時はファイルが存在しないようだ）
```

- 対応
```
$ sudo reboot
```

- reboot指示の中身
```
$ cat /var/run/reboot-required.pkgs 
linux-image-6.2.0-32-generic
linux-base

（不要の時はファイルが存在しないようだ）
```


## パッケージのアップデート
```
$ sudo apt update
$ sudo apt upgrade
$ sudo apt autoremove      ← 使われていないパッケージの削除(optional)
```

## ファームウェアのアップデート
- 頻度はごく稀だと思うが、SSHログインするとファームウェアのアップデートの情報が出たりする
```
1 device has a firmware upgrade available.
Run `fwupdmgr get-upgrades` for more information.
```
- 素直にこのコマンドをたたくとより詳しい情報が出る
- 実際に適用するのは以下
```
sudo fwupdmgr update
```
- えてしてこの後にリブートを促される（選択はできるのでリブートをしなくてもいい）

## 外付けHDDをつなげる
- （初回のみ）マウントポイント（マウントした（=つなげた）後のアクセス先）の設定
   - 通常は/mntの下に作ると思う
   - 作る名前は自分の好きなように
```
$ sudo mkdir /mnt/exthdd
```
- つなぐ
- デバイスとしてどう認識されたかの確認
   - HDDなら`/dev/sdb`とか`/dev/sdc`になっているかと思う
```
$ sudo fdisk -l
...
```
- マウントする
```
$ mount /dev/sdc /mnt/exthdd
```
   - HDDのパーティションが分かれている場合など、パーティションの番号まで必要になる場合もある
```
$ mount /dev/sdc1 /mnt/exthdd
```
   - ディクスタイプを明示的に指定してマウントすることもできる：ext3、ntfs、fatなど
```
$ mount -t ext3 /dev/sdc1 /mnt/exthdd
```
- 外すとき（アンマウント）
```
# どちらかをやればいい
$ sudo umount /dev/sdc1
$ sudo umount /mnt/exthdd
```

## sshできるポートの指定
- `/etc/ssh/sshd_config`を編集 (ssh_configもあるので注意)
```
(before)
# Port 22
```

```
(after)
Port 22
Port 9022
```
- 編集後：`$ sudo service ssh restart`
- 確認
```
$ ss -ant4
State   Recv-Q  Send-Q   Local Address:Port        Peer Address:Port   Process
LISTEN  0       128            0.0.0.0:22               0.0.0.0:*
...
LISTEN  0       128            0.0.0.0：9022             0.0.0.0:*
...
```

- 場合によってはファイアーウォールで遮断されているかもしれないので開ける手続きも必要 `ufw allow 9022`
- 参考：自分の場合、無線LANが調子が悪いときのためにバックアップとして有線もしておいて、ルーターでのポートフォワード設定で通常はwi-fi経由22番へ、バックアップとして有線経由別ポートに行くよう設定した。


## Sambaによるファイルサーバー
- Sambaをたてておくとファイルサーバーとしてネットワーク内のサーバーからファイルを閲覧、保管することができる

### Sambaのインストール
```
$ sudo apt install samba
```

### 共有先の作成
```
$ mkdir /shared/all
$ chmod o+rwx /shared/all    ← 全員に共有するディレクトリはpermissionを777にする。（Other userにrwxの権限を付与、の意味）
```
- 特定ユーザーだけがアクセスするようにする場合は、そのユーザーでユーザー名とグループ名を設定する

### Sambaの設定
- 設定ファイルは`/etc/samba/smb.conf`。バックアップをとっておくこと

```
[global]
...
   workgroup = (自分のワークグループに設定。特にWindowsのとき)
...
   interfaces = 127.0.0.0/8 eth0 192.168.0.0/24    ← ローカルネットワークからのみの際は192.168.0.0/24（か自分のネットワークの設定）を追加する
```

#### ゲストユーザーでも読み書きできるようにする設定
```
[shared]
   path = /shared/all
   browsable = yes
   writable  = yes
   guest ok  = yes
   read only = no
```

#### 特定ユーザーのみが読み書きできるようにする設定
```
[specific]
   path = /shared/user_a
   browsable = yes
   writable  = yes
   guest ok  = no
   valid users = user_a
```
```
# アクセスできるユーザーがLinuxシステム上に存在しない場合は新たに作成
$ sudo pdbedit -a user_a
# 特定ユーザーのみがアクセスできるときは、アクセスする際のパスワードも設定
$ sudo smbpasswd -a user_a
（パスワードを入れる）
$ sudo pdbedit -l   ← 確認
```

### Sambaのリスタート
```
$ sudo systemctl restart smbd
```

###  動作確認など
- Macからの場合：Ubuntuでavahiが動いているので、ネットワークの下にサーバー名が出ているはず。そこからアクセスする
- Macからの場合：もしくは、Finderで移動 → サーバーに接続 で smb://（IPアドレス）でアクセスできる
- 見えない場合、UbuntuのファイアーウォールでSambaの使う先のポートをブロックしている可能性もある。以下で許可する
```
$ sudo ufw allow 'Samba'
```
