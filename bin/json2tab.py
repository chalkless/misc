#!/usr/bin/env python3

import json
import csv
import sys
from pathlib import Path

def json_to_tsv(json_path, tsv_path):
    try:
        # ファイル存在チェック
        if not Path(json_path).is_file():
            print(f"Error: JSONファイルが見つかりません: {json_path}")
            return

        # JSON読み込み
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # データ形式チェック（リスト形式を想定）
        if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
            print("Error: JSONは辞書のリスト形式である必要があります。")
            return

        # ヘッダー取得（全キーを網羅）
        headers = sorted({key for row in data for key in row.keys()})

        # TSV書き込み
        with open(tsv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers, delimiter="\t", extrasaction="ignore")
            writer.writeheader()
            for row in data:
                writer.writerow(row)

        print(f"変換完了: {tsv_path}")

    except json.JSONDecodeError as e:
        print(f"JSONの読み込みエラー: {e}")
    except Exception as e:
        print(f"予期しないエラー: {e}")

if __name__ == "__main__":
    # 使い方: python script.py input.json output.tsv
    if len(sys.argv) != 3:
        print("使い方: python script.py 入力.json 出力.tsv")
    else:
        json_to_tsv(sys.argv[1], sys.argv[2])
      
