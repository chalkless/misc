# Minicondaのセットアップ

- Anacondaというものがありました。しかし、これは有料になったので（2024年現在）、今はminicondaを使います

## apt/yum/brewとconda
- システム全体はapt（Ubuntuの場合）、yum（RedHat系の場合。CentOSも含む）、brew（Macの場合）でパッケージを管理します。
- 一方でcondaはその場その場で仮想環境を作ってその環境で作業をするイメージです。
- なので、システム全体とconda環境を混在させる（特に同じ場所にインストールする）といずれ環境を破壊するので絶対にやめるべきです
- 理想は自分のホームディレクトリの下にインストールすることでしょう。逆に共用マシンで共通部分を触る権限がないときはcondaで自身の環境を作ることができます。
- どうしても共用の場所にインストールしたいならばシステム全体が触らない場所にインストールします。
- たとえば、Macの場合、Homebrewは/opt/brew/以下にパッケージをインストールしますが、同様に/opt/miniconda/以下にインストールすると管理的にもきれいに見えるかと思います。
- 一つの例として、aptで入るものはなるべくaptで入れる、あるいは一連の解析（たとえばNGS解析）はcondaの1つの環境で実現できるようにその環境でインストールする、などという使い方もあるかと思います

## Minicondaのインストール
- ここに書いてもいずれは変わるかもしれないから、一次情報である公式サイトで確認すること！
- Minicondaでググると公式ページが出てきた → Minicondaのページ：https://docs.anaconda.com/miniconda/
- 読む →　Anacondaと同じダウロードページらしい。行くと登録しろとでかでかと書いてあるが、そこに小さくskipと書いてある。リンク先で自分のプラットフォームのファイルをダウンロードしてくる。
- 2024年現在、「Python 3.12用の (for Python 3.12)」と書いてあるが、これはインストールされるpythonのバージョンのこと。インストール先のpythonのバージョンがどんなかは関係ない
- 別バージョンのpythonをインストールしたい場合は、公式ページにこれまでのインストーラのレポジトリサイトがあるからそれを見ろと書いてある：https://repo.anaconda.com/miniconda

```
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ chmod 755 Miniconda3-latest-Linux-x86_64.sh
$ ./Miniconda3-latest-linux-x86_64.sh
...
```
- 途中、インストール先を訊かれる。
    - 通常は`~/miniconda3/`に入る
- `conda init`：設定ファイルを書き込むかどうか（~/.bashrcに）→ とりあえずnoのままでよい。
```
...
Do you wish to update your shell profile to automatically initialize conda?
This will activate conda on startup and change the command prompt when activated.
If you'd prefer that conda's base environment not be activated on startup,
   run the following command when conda is activated:

conda config --set auto_activate_base false

You can undo this by running `conda init --reverse $SHELL`? [yes|no]
[no] >>> no

You have chosen to not have conda modify your shell scripts at all.
To activate conda's base environment in your current shell session:

eval "$(/home/tkr_nak/miniconda3/bin/conda shell.YOUR_SHELL_NAME hook)" 

To install conda's shell functions for easier access, first activate, then:

conda init

Thank you for installing Miniconda3!
```

- `conda init`をnoにしたので、自分で.bashrcの末尾に書き込むと書かれているものがある
```
(.bashrc)
export PATH=~/miniconda3/bin:$PATH
source ~/miniconda3/etc/profile.d/conda.sh
```

- `source .bashrc`するか、ログインし直すかするとcondaの設定が効く。

- インストール時の指示に従えば以下のコマンドを打つことになるんだろうか
```
$ eval "$(/home/tkr_nak/miniconda3/bin/conda shell.YOUR_SHELL_NAME hook)" 
(YOUR_SHELL_NAMEは自分のシェルの名前に書き換える。bashなど)
$ conda init
```
- するとcondaのbase環境に入ったモードになる（プロンプトの最初に(base)が付く）
- 以下のようにすると元のモードに戻れる
```
$ conda deactivate
```
- .bashrcに以下が書き込まれている
```
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/tknakazato/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/tknakazato/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/tknakazato/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/tknakazato/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```
- 自動でconda環境にならないようには以下のように設定しておく
```
$ conda config --set auto_activate_base false
```




## mambaのインストール
- 結局これを使うべきなのか、今後 オワコンなのかがわからない
- mambaはconda用のパッケージマネージャー
- https://mamba.readthedocs.io/en/latest/
- https://github.com/mamba-org/mamba

- 上を見るとこう書いてあるんだけどね：We recommend that you start with the Miniforge distribution >= Miniforge3-23.3.1-0. 
```
$ conda install -c conda-forge mamba
# 別のやり方
$ conda install conda-forge::mamba
```
- とりあえず、conda-forge channelから持ってこい、と指定している。

## 仮想環境の作成
```
$ mamba create -n envname
```

- 設定した仮想環境は以下で確認できる
```
$ mamba env list
  Name  Active  Path                    
──────────────────────────────────────────
  base  *       /home/chalkless/miniconda3
```

- 仮想環境の削除
```
$ mamba remove -n envname
```

- 仮想環境に入る/仮想環境から出る
```
$ mamba activate envname
$ mamba deactivate envname
```

### troubleshooting
- 自分の場合は以下のように怒られたのだが
```
warning  libmamba You have not set the root prefix environment variable.
    To permanently modify the root prefix location, either:
      - set the 'MAMBA_ROOT_PREFIX' environment variable
      - use the '-r,--root-prefix' CLI option
      - use 'mamba shell init ...' to initialize your shell
        (then restart or source the contents of the shell init script)
    Continuing with default value: "/home/tkr_nak/miniconda3"
```
- `mamba shell init`すると以下が`.bashrc`に書き込まれたので、再読み込みすれば怒られないようになる
```
# >>> mamba initialize >>>
# !! Contents within this block are managed by 'mamba shell init' !!
export MAMBA_EXE='/home/tkr_nak/miniconda3/bin/mamba';
export MAMBA_ROOT_PREFIX='/home/tkr_nak/miniconda3';
__mamba_setup="$("$MAMBA_EXE" shell hook --shell bash --root-prefix "$MAMBA_ROOT_PREFIX" 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__mamba_setup"
else
    alias mamba="$MAMBA_EXE"  # Fallback on help from mamba activate
fi
unset __mamba_setup
# <<< mamba initialize <<<
```
