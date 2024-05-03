import os
import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
plt.rcParams['font.family'] = ['Arial']

import other_methods
p = other_methods.print_readable



def read_csv_file(file_path):
    x_coords = []
    y_coords = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            x_coords.append(round(float(row[0]), 3))
            y_coords.append(round(float(row[1]), 3))
    return x_coords, y_coords



def update_plot_forward(frame):
    plt.cla()
    plt.xlim(-3.5, 3.5)
    plt.ylim(-3.5, 3.5)
    for i in range(3):
        for j in range(3):
            xy = []
            for k in range(4):
                xy.append(data[4*(3*i+j)+k][frame])
            xy.append(xy[0])
            match [i,j]:
                case [0,0]:
                    a = patches.Polygon( xy, edgecolor='black', facecolor='cyan' )
                case [0,1]:
                    a = patches.Polygon( xy, edgecolor='black', facecolor='magenta' )
                case [0,2]:
                    a = patches.Polygon( xy, edgecolor='black', facecolor='cyan' )
                case [1,0]:
                    a = patches.Polygon( xy, edgecolor='black', facecolor='magenta' )
                case [1,1]:
                    a = patches.Polygon( xy, edgecolor='black', facecolor='cyan' )
                case [1,2]:
                    a = patches.Polygon( xy, edgecolor='black', facecolor='magenta' )
                case [2,0]:
                    a = patches.Polygon( xy, edgecolor='black', facecolor='cyan' )
                case [2,1]:
                    a = patches.Polygon( xy, edgecolor='black', facecolor='magenta' )
                case [2,2]:
                    a = patches.Polygon( xy, edgecolor='black', facecolor='cyan' )
            ax.add_patch(a)



# データを読み込む
data = []
for i in range(3):
    for j in range(3):
        for k in range(4):
            file_name = f"object_{i}{j}_{k}.csv"
            file_path = os.path.join('unique_csv', file_name)
            x_coords, y_coords = read_csv_file(file_path)
            data.append(list(zip(x_coords, y_coords)))


# アニメーションを作成する
fig, ax = plt.subplots(figsize=(6, 6))
ani_forward = animation.FuncAnimation(fig, update_plot_forward, frames=len(data[0]), interval=5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('anisotropic-medium')

plt.show()
plt.clf()
plt.close()
