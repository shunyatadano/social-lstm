import pandas as pd

# CSVファイルの読み込み
# csv_file = '/home/eevee/social-lstm/thor-magni/tm_png_merge/Scenario_1/train/interpolated_data.csv'
# csv_file = '/home/eevee/social-lstm/thor-magni/tm_png_merge/Scenario_1/val/interpolated_data.csv'
csv_file = '/home/eevee/social-lstm/thor-magni/tm_png_merge/Scenario_1/test/test_interpolated.csv'
df = pd.read_csv(csv_file)

# 必要なカラムの抽出と順番の入れ替え
df = df[['frame_id', 'ag_id', 'y', 'x']]  # 'z'が不要な場合は除く

# タブ区切り形式でtxtファイルとして保存
# save_path = '/home/eevee/social-lstm/thor-magni/tm_png_merge/Scenario_1/txt/train/interpolated_data.txt'
# save_path = '/home/eevee/social-lstm/thor-magni/tm_png_merge/Scenario_1/txt/val/interpolated_data.txt'
save_path = '/home/eevee/social-lstm/thor-magni/tm_png_merge/Scenario_1/txt/test/interpolated_data.txt'
df.to_csv(save_path, sep='\t', index=False, header=False)
