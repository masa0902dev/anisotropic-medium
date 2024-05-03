def print_readable(item):
    print()
    print(item)
    print()


import csv
import os
def write_csv(file_path, coordinates):
    mode = 'a' if os.path.exists(file_path) else 'w'
    with open(file_path, mode, newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['x', 'y'])
        writer.writerow(coordinates)
        # for coordinate in coordinates:
        #     writer.writerow(coordinate)



def write_csv_reverse(input_file, output_file):
    # CSVファイルを逆順で読み取り、行をリストに格納する
    with open(input_file, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # 出力ファイルを逆順に書き込む
    with open(output_file, 'a', newline='') as f:
        writer = csv.writer(f)
        for row in reversed(rows):
            writer.writerow(row)
