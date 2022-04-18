# LinuxにNGS環境を整える
- そもそもLinuxといってもいろいろあるけれども
    - CentOSで`yum search XXX`しても軒並み見つからない
    - Ubuntuで`apt search XXX`は見つかるっぽい??? (yum でもだけどbowtie2だけ見つかるのか)

    # Miniconda（Bioconda）の導入
- Miniconda経由でツールを導入することとする。
- 「Miniconda install」などでググるとページ ( https://docs.conda.io/en/latest/miniconda.html ) が出てくるので、そこからダウンロードする
```
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ chmod 755 Miniconda3-latest-Linux-x86_64.sh
$ ./Miniconda3-latest-linux-x86_64.sh
...
```
- 途中、インストール先を訊かれる。
    - 通常は`~/miniconda3/`に入る
    - 自分だけならいいのだが、他の人にも使ってもらうなら共用の場所がよいのでは?
- `conda init`：設定ファイルを書き込むかどうか（~/.bashrcに）
- `.bashrc`に設定が書かれるので、`source .bashrc`するか、ログインし直すか
- biocondaのパッケージが使えるようにchannelsに登録する
```
$ conda config --add channels defaults   ← 多分、すでに入っていると怒られる
$ conda config --add channels conda-forge
$ conda config --add channels bioconda
```

- インストールなど
    - `-c`はチャンネル指定なのでなくても動くかとは思う 
```
$ conda install -c bioconda fastqc
$ conda install -c biocond trim_galore
```
    - trinityはそのままだと古いバージョンが入ってしまうのでバージョンも指定
```
$ conda install trinity=2.13.2
```
