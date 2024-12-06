# pythonで実践 生命科学データの機械学習 を試してみる
## 第13章 発展編②：機械学習によるマイクロバイオームと昨日未知遺伝子の解析
```
sudo apt install python3-pyqt5
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
wget https://ddbj.nig.ac.jp/public/ddbj_database/dra/fastq/ERA000/ERA000116/ERX004306/ERR011347_1.fastq.bz2
wget https://ddbj.nig.ac.jp/public/ddbj_database/dra/fastq/ERA000/ERA000116/ERX004306/ERR011347_2.fastq.bz2
wget https://ddbj.nig.ac.jp/public/ddbj_database/dra/fastq/ERA000/ERA000116/ERX004307/ERR011348_1.fastq.bz2
wget https://ddbj.nig.ac.jp/public/ddbj_database/dra/fastq/ERA000/ERA000116/ERX004307/ERR011348_2.fastq.bz2
wget https://ddbj.nig.ac.jp/public/ddbj_database/dra/fastq/ERA000/ERA000116/ERX004308/ERR011349_1.fastq.bz2
wget https://ddbj.nig.ac.jp/public/ddbj_database/dra/fastq/ERA000/ERA000116/ERX004308/ERR011349_2.fastq.bz2
bunzip2 ERR011347_1.fastq.bz2
bunzip2 ERR011347_2.fastq.bz2
fastp -i ERR011347_1.fastq -I ERR011347_2.fastq -o ERR011347_trimmed1.fastq.gz -O ERR011347_trimmed2.fastq.gz -f 5 -F 5 --html ERR011347.fastp.html -w 10 
（1分くらい）
mv fastp.json fastp.ERR011347.json 
```
