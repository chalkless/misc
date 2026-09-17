import csv
import re

def clean_tsv(input_file_path, output_file_path):
    """
    TSVファイルの各列の前後にある「"」を削除し、
    列の内部で連続する複数の「"」を1つの「"」に置換して新しいファイルに保存します。
    """
    # 連続するダブルクォーテーションにマッチする正規表現パターン
    multiple_quotes_pattern = re.compile(r'"+')

    # ファイルの読み込みと書き込み（エンコーディングは環境に合わせて utf-8 としています）
    with open(input_file_path, 'r', encoding='utf-8', newline='') as infile, \
         open(output_file_path, 'w', encoding='utf-8', newline='') as outfile:
        
        # タブ区切り（delimiter='\t'）でリーダーとライターを設定
        # 自動的なクォート処理を無効化するため quoting=csv.QUOTE_NONE を指定
        reader = csv.reader(infile, delimiter='\t', quoting=csv.QUOTE_NONE)
        writer = csv.writer(outfile, delimiter='\t', quoting=csv.QUOTE_NONE)
        
        for row in reader:
            cleaned_row = []
            for cell in row:
                # 1. 各列の先頭と末尾の「"」を削除
                if cell.startswith('"') and cell.endswith('"') and len(cell) >= 2:
                    cell = cell[1:-1]
                
                # 2. 残った文字列内で、複数連続する「"」を1つに置換
                cell = multiple_quotes_pattern.sub('"', cell)
                
                cleaned_row.append(cell)
            
            # 加工した行を書き込み
            writer.writerow(cleaned_row)

# --- 実行例 ---
# 入力ファイル名と出力ファイル名を指定して実行してください
input_file = 'input.tsv'
output_file = 'output.tsv'

# 関数を実行
clean_tsv(input_file, output_file)
print(f"処理が完了しました。出力ファイル: {output_file}")
