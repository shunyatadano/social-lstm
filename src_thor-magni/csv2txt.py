import pandas as pd

# CSVファイルの読み込み
# csv_file = '/home/eevee/social-lstm/thor-magni/tm_png_merge/Scenario_1/train/interpolated_data.csv'
# csv_file = '/home/eevee/social-lstm/thor-magni/tm_png_merge/Scenario_1/val/interpolated_data.csv'
# csv_file = '/home/eevee/social-lstm/thor-magni/tm_png_merge/Scenario_1/test/test_interpolated.csv'

csv_file = '/home/eevee/social-lstm/thor-magni/tm_png/Scenario_1/val/20241016_Magni_170522_SC1B_R2.csv'
df = pd.read_csv(csv_file)

# 必要なカラムの抽出と順番の入れ替え
df = df[['frame_id', 'modified_ag_id', 'y', 'x']]  # 'z'が不要な場合は除く
# df = df[['frame_id', 'ag_id', 'y', 'x']]  # 'z'が不要な場合は除く

# ag_idの始まりを1にする
# df['ag_id'] = df['ag_id'] + 1
print(f"xrange: {df['x'].min()} to {df['x'].max()}")
print(f"yrange: {df['y'].min()} to {df['y'].max()}")

# タブ区切り形式でtxtファイルとして保存
# save_path = '/home/eevee/social-lstm/thor-magni/tm_png_merge/Scenario_1/txt/train/Scenario_1.txt'
# save_path = '/home/eevee/social-lstm/thor-magni/tm_png_merge/Scenario_1/txt/val/Scenario_1.txt'
# save_path = '/home/eevee/social-lstm/thor-magni/tm_png_merge/Scenario_1/txt/test/Scenario_1.txt'

save_path = '/home/eevee/social-lstm/data/validation/thor_magni/20241016_Magni_180522_SC1B_R1.txt'

df.to_csv(save_path, sep=' ', index=False, header=False)
# df.to_csv(save_path, sep='\t', index=False, header=False)

print(f"Saved to {save_path}")