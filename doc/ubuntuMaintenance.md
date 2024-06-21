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

-　ログイン状態時でのrebootの要不要確認
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
