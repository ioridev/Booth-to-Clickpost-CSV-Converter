import pandas as pd

# 元のCSVファイルを読み込む
input_file = 'input.csv'  # 元のCSVファイル名
output_file = 'output.csv'  # 出力するCSVファイル名
df = pd.read_csv(input_file)

# 新しいCSVファイルのデータフレームを作成する
new_df = pd.DataFrame()

# 各列を変換し、新しいデータフレームに追加する
new_df['お届け先郵便番号'] = df['郵便番号']
new_df['お届け先氏名'] = df['氏名']
new_df['お届け先敬称'] = ''  # 敬称情報がないため、空の文字列を使用する
new_df['お届け先住所1行目'] = df['都道府県']
new_df['お届け先住所2行目'] = df['市区町村・丁目・番地']
new_df['お届け先住所3行目'] = df['マンション・建物名・部屋番号']
new_df['お届け先住所4行目'] = ''  # この情報は元のCSVにないため、空の文字列を使用する
new_df['内容品'] = df['商品ID / 数量 / 商品名'].str.extract(r'/\s数量\s:\s\d+\s/\s(.+)$')
new_df.replace({'\uff0d': '-'}, regex=True, inplace=True)

# 新しいCSVファイルを保存する
new_df.to_csv(output_file, index=False, encoding='shift_jis', errors='replace')

