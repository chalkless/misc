# コマンドでGitやGitHubを使う
## そもそもgitコマンドが入っていないなど
- CentOS7とかだとyumで入るのは1.8.3という古いバージョンのgitなので、2系を入れるのは一癖必要
-yumでiusレポジトリが読み込めるようになっていればここに2系が入っている。
```
$ sudo yum install git224
```

## GitHubとの連携（公開鍵登録編）
- こちら側の情報をGitHubサイトに登録する
- パスワード認証は廃止済。ということで公開鍵認証する
- 公開鍵の作成
```
$ ssh-keygen -t rsa
```
  -- 自分の場合はgithub_id_rsa（と〜.pub）を作成
  -- permissionを600にしておく
- GitHubへの登録
  -- 自分のページの右上からSetting
  -- 左メニューから"SSH and GPG keys"
  -- SSH keysに登録する
  -- 参考までにGPGはパスワードの代わりのトークンのはず。SourceTreeとかだとパスワードの代わりにこれを登録する、でいいのかな。これもここから発行する
- 接続確認
```
$ ssh -T git@github.com
```
```
（成功した時）
Hi chalkless! You've successfully authenticated, but GitHub does not provide shell access.
（失敗した時）
git@github.com: Permission denied (publickey).
```
- 失敗した時は
```
$ ssh-add -l
2048 SHA256:ZycnGTDnbgQd4eAuD5iClVrH9jZbe0z1kn+dXrFV/0I github_id_rsa (RSA)
```
  -- 上記のように返ってこない場合は
```
$ ssh-add github_id_rsa
```
  -- このとき以下のように出る場合は失敗している
```
Could not open a connection to your authentication agent.
```
  -- 失敗した場合は以下をまず行う
```
$ eval "$(ssh-agent)"
```

## GitHubとの連携（環境構築編）
```
$ cd ~/git  ←別にここに限らないのだが
$ git config --global user.name "(your name)"
$ git config --global user.email "(your email)"
$ git init
```

## 実際の利用編
- ローカルレポジトリにダウンロードしてくる
  -- レポジトリのページに行って、メイン部分右上の（緑色の）Codeボタンをクリック
  -- CloneでSSHを選んでURLをコピー
```
$ git clone （コピーしたURL）
```
  -- トラブル例
```
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```
     --- SSH公開鍵の設定を見直すこと
- リモートレポジトリに反映
  -- ステージング（リモートに反映させるファイル・ディレクトリを指定）
  ```
  $ git add （反映させたいファイル・ディレクトリ）
  ```
  -- コミット（反映内容をコメントに記述）
  ```
  $ git commit -m "コメント内容"
  ```
  -- リモートに反映
  ```
  $ git push
  ```
