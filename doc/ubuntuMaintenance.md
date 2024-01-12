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

