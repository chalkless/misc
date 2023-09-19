# Ubuntuの日々の管理

## パッケージのアップデート
```
$ sudo apt update
$ sudo apt upgrade
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
