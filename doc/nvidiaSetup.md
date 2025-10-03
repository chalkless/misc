# NVIDIAの設定
- いまどき、GPUを使っての計算をしようとするとNVIDIAのグラフィックボード（通称：グラボ）を使うのが主流である。なのだがセットアップ関係が（バージョンアップも含めて）意外とトラブるのでここにまとめておく

## ドライバが認識されているかの確認
- グラボが挿さっているかの確認
```
$ lspci
...
01:00.0 VGA compatible controller: NVIDIA Corporation TU106 [GeForce RTX 2060 Rev. A] (rev a1)
...
```
- `lspci`はPCIバスに挿さっている機器をリストするもの

## 画面が出ない時
- SSHで外からログインできればいいんだけどさ
- グラボを挿したらマザボのグラフィック出力（HDMI）が使えなくなってグラボの方の口に挿さないと画面が出なかったので意外と盲点

## 関連するドライバなどのアンインストール
```
sudo apt --purge remove "nvidia-*"
sudo apt --purge remove "cuda-*"
```
- ダブルクォーテーションで囲うのを忘れないこと
- 場合によっては`sudo apt autoremove`も促される
