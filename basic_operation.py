import math
theta_default = math.pi / 1800
x = "x"
y = "y"

# 正方形を保つように点を並行移動してから、点を回転させる
def move(point, move_value, rotation_center, theta=theta_default):
    # dic_after = be_square(point, move)
    # dic_after = rotate_point(dic_after, theta)
    # return dic_after
    moved_point = {
        x: point[x] + move_value[x],
        y: point[y] + move_value[y],
    }
    rotated_point = {
        x: rotation_center[x] + 
            ( (moved_point[x]-rotation_center[x]) * math.cos(theta) - (moved_point[y]-rotation_center[y]) * math.sin(theta) ),
        y: rotation_center[y] +
            ( (moved_point[x]-rotation_center[x]) * math.sin(theta) + (moved_point[y]-rotation_center[y]) * math.cos(theta) ),
    }
    return rotated_point


def be_square(point, move_value):
    moved_point = {
        x: point[x] + move_value[x],
        y: point[y] + move_value[y],
    }
    return moved_point

def rotate_point(point, rotation_center, theta=theta_default):
    rotated_point = {
        x: rotation_center[x] +
            ( (point[x]-rotation_center[x]) * math.cos(theta) - (point[y]-rotation_center[y]) * math.sin(theta) ),
        y: rotation_center[y] +
            ( (point[x]-rotation_center[x]) * math.sin(theta) + (point[y]-rotation_center[y]) * math.cos(theta) ),
    }
    return rotated_point

