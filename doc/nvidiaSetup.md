# NVIDIAグラボなどの設定
- いまどき、GPUを使っての計算をしようとするとNVIDIAのグラフィックボード（通称：グラボ）を使うのが主流である。なのだがセットアップ関係が（バージョンアップも含めて）意外とトラブるのでここにまとめておく
- 今回はUbuntu 22での例を書いている

## ドライバが認識されているかの確認
- グラボが挿さっているかの確認
```
$ lspci
...
01:00.0 VGA compatible controller: NVIDIA Corporation TU106 [GeForce RTX 2060 Rev. A] (rev a1)
...
```
`lspci`はPCIバスに挿さっている機器をリストするもの

- ドライバが認識されて使える状態かの確認
```
$ nvidia-smi 
Fri Oct  3 17:59:16 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.82.09              Driver Version: 580.82.09      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 2060        Off |   00000000:01:00.0  On |                  N/A |
| 41%   49C    P8              9W /  170W |      53MiB /   6144MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            1181      G   /usr/lib/xorg/Xorg                       36MiB |
|    0   N/A  N/A            1264      G   /usr/bin/gnome-shell                      6MiB |
+-----------------------------------------------------------------------------------------+
```
（簡易版）
```
$ nvidia-smi -L
GPU 0: NVIDIA GeForce RTX 2060 (UUID: GPU-28a96ffb-be7e-7e82-5e9e-3c7b591750fd)
```


## ドライバのインストール
### aptで見に行くレポジトリの追加
```
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
```
### インストールするドライバの選択
```
$ ubuntu-drivers devices
== /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0 ==
modalias : pci:v000010DEd00001F08sv0000103Csd00008557bc03sc00i00
vendor   : NVIDIA Corporation
model    : TU106 [GeForce RTX 2060 Rev. A]
driver   : nvidia-driver-418-server - distro non-free
...
driver   : nvidia-driver-570 - third-party non-free
driver   : nvidia-driver-580 - third-party non-free recommended
driver   : nvidia-driver-580-server-open - distro non-free
driver   : nvidia-driver-580-open - third-party non-free
driver   : nvidia-driver-580-server - distro non-free
driver   : nvidia-driver-470 - distro non-free
...
```
- recommendedのものを入れる
- が、openと書いてあるものを選ぶとトラブっていたことが多いようなのでやめておく
- https://www.nvidia.com/ja-jp/drivers/ ここから情報を入れてバージョンの確認もできる
### 実際のインストール
```
sudo apt install nvidia-driver-580
```
- 終わったらリブートする
- リブートすると、セキュアブートのUEFIブートマネージャーの画面が出ることがある。`Enroll MOK -> Continue -> Yes -> Password -> Reboot`。再度リブートがかかる。
- `nvidia-smi`で確認する

## 画面が出ない時
- SSHで外からログインできればいいんだけどさ
- グラボを挿したらマザボのグラフィック出力（HDMI）が使えなくなってグラボの方の口に挿さないと画面が出なかったので意外と盲点

## Cudaのインストール
- https://developer.nvidia.com/cuda-downloads で環境（OSなど）を選ぶとコマンドが出てくる。
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt update
sudo apt install cuda-toolkit-13-0
```
- .bashrcに追加
```
export PATH="/usr/local/cuda/bin:$PATH"
export LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
```
- 再起動する
- `nvidia-smi`できちんと出るか確認
- nvccでの確認
```
$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2025 NVIDIA Corporation
Built on Wed_Aug_20_01:58:59_PM_PDT_2025
Cuda compilation tools, release 13.0, V13.0.88
Build cuda_13.0.r13.0/compiler.36424714_0
```


## 関連するドライバなどのアンインストール
```
sudo apt --purge remove "nvidia-*"
sudo apt --purge remove "cuda-*"
```
- ダブルクォーテーションで囲うのを忘れないこと
- 場合によっては`sudo apt autoremove`も促される

## トラブル
- その1
```
$ nvidia-smi 
NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.
```
→ ドライバの再インストール
- その2
```
$ nvidia-smi
Failed to initialize NVML: Driver/library version mismatch
NVML library version: 580.95
```
→ 再起動してみる
