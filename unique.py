# unique 3*3 (cannot be generalized)
x = "x"
y = "y"

import initial_state
object00 = initial_state.object00; object01 = initial_state.object01; object02 = initial_state.object02
object10 = initial_state.object10; object11 = initial_state.object11; object12 = initial_state.object12
object20 = initial_state.object20; object21 = initial_state.object21; object22 = initial_state.object22
objects0 = initial_state.objects0; objects1 = initial_state.objects1; objects2 = initial_state.objects2
objects = initial_state.objects
center_point = initial_state.center_point # デフォルト：{x:0, y:0}
center_object = initial_state.center_object # デフォルト：object11

import basic_operation
move = basic_operation.move
rotate_point = basic_operation.rotate_point
be_square = basic_operation.be_square
theta_default = basic_operation.theta_default # デフォルト：pi/1800

import other_methods
p = other_methods.print_readable
write_csv = other_methods.write_csv
write_csv_reverse = other_methods.write_csv_reverse



import math
import os

def delete_csv_files():
    csv_dir = os.path.join(os.getcwd(), "unique_csv")
    for file in os.listdir(csv_dir):
        os.remove(os.path.join(csv_dir, file)
    )



def move_object_connected_with_next2object(objects, row, col, index_next2, index_target):
    next_index_in_row = (col + 1) if col + 1 < 3 else (col - 1)
    next_index_in_col = (row + 1) if row + 1 < 3 else (row - 1)
    next_object_in_row = objects[row][next_index_in_row]
    next_object_in_col = objects[next_index_in_col][col]
    # 縦横と接続している点を移動させる
    if row == col:
        objects[row][col][index_target[0]] = next_object_in_row[index_next2[0]]
        objects[row][col][index_target[1]] = next_object_in_col[index_next2[1]]
    else:
        objects[row][col][index_target[0]] = next_object_in_col[index_next2[0]]
        objects[row][col][index_target[1]] = next_object_in_row[index_next2[1]]
    # 縦横と接続していない点を移動させる
    roop_index = [0, 1, 2, 3]
    roop_index = [elem for elem in roop_index if elem not in index_target]
    for i in roop_index:
        pm = 0
        # rotater:回す人(回転軸)、rotatee:回される人
        if (i+1) % 4 in index_target:
            rotater = (i+1) % 4
            pm = 1
        else:
            rotater = (i-1) % 4
            pm = -1
        rotatee = [elem for elem in index_target if elem != rotater][0]
        # 90度回転。回転方向を場合分け
        rotation_pm = -1 if pm == 1 else 1
        objects[row][col][i] = rotate_point(objects[row][col][rotatee],
                                            objects[row][col][rotater], 
                                            rotation_pm * math.pi/2)


def move_object_connected_with_center(object, index_center, index_target):
    move_value = {
        x: object11[index_center][x] - object[index_target][x],
        y: object11[index_center][y] - object[index_target][y],    
    }
    ## 中心オブジェクトと接続している点を移動させる
    object[index_target] = object11[index_center]
    ## 中心オブジェクトと接続していない点を移動させる
    roop_index = [0, 1, 2, 3]
    roop_index = [elem for elem in roop_index if elem != index_target]
    for i in roop_index:
        object[i] = move(object[i], move_value, object[index_target], -theta_default)


def write_state(objects):
    csv_dir = os.path.join(os.getcwd(), "unique_csv")
    for row in range(3):
        for col in range(3):
            for k in range(4):
                # objects[row][col][k] = {x: round(objects[row][col][k][x], 8), y: round(objects[row][col][k][y], 8)}
                file_name = f"object_{row}{col}_{k}.csv"
                write_csv(os.path.join(csv_dir, file_name), objects[row][col][k])
                # print(file_name, objects[row][col][k])
                # write_csv( os.path.join(csv_dir, f"object{row}{col}.csv"), objects[row][col] )


def advance_time():
    # 中心のobject11を [0,0]中心に pi/1800回転 させる
    for i in range(len(object11)):
        object11[i] = rotate_point(object11[i], center_point)

    # その影響で、11と繋がっている01,12,21,10が移動する
    move_object_connected_with_center(objects[0][1], 0, 2)
    move_object_connected_with_center(objects[1][2], 1, 3)
    move_object_connected_with_center(objects[2][1], 2, 0)
    move_object_connected_with_center(objects[1][0], 3, 1)

    # その影響で、00,02,22,20が移動する
    move_object_connected_with_next2object(objects, 0, 0, [3, 0], [1, 2])
    move_object_connected_with_next2object(objects, 0, 2, [0, 1], [2, 3])
    move_object_connected_with_next2object(objects, 2, 2, [1, 2], [3, 0])
    move_object_connected_with_next2object(objects, 2, 0, [2, 3], [0, 1])




def main_loop():
    delete_csv_files()
    write_state(objects)

    pi_4 = 450
    for _ in range(pi_4):
        advance_time()
        write_state(objects)

    for i in range(3):
        for j in range(3):
            for k in range(4):
                file_name = f"object_{i}{j}_{k}.csv"
                file_path = os.path.join('unique_csv', file_name)
                write_csv_reverse(file_path, file_path)

    print("New simulation is done!")
    print("rotation radian:", pi_4 * theta_default)
main_loop()
