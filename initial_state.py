x = "x"
y = "y"

# オブジェクトは正方形、一辺の長さはsqrt(2)としている
# 初期状態
object00 = [{x:-2, y:3}, {x:-1, y:2}, {x:-2, y:1}, {x:-3, y:2}]
object01 = [{x:0, y:3}, {x:1, y:2}, {x:0, y:1}, {x:-1, y:2}]
object02 = [{x:2, y:3}, {x:3, y:2}, {x:2, y:1}, {x:1, y:2}]
objects0 = [object00, object01, object02]

object10 = [{x:-2, y:1}, {x:-1, y:0}, {x:-2, y:-1}, {x:-3, y:0}]
object11 = [{x:0, y:1}, {x:1, y:0}, {x:0, y:-1}, {x:-1, y:0}] #---3*3の中心---
object12 = [{x:2, y:1}, {x:3, y:0}, {x:2, y:-1}, {x:1, y:0}]
objects1 = [object10, object11, object12]

object20 = [{x:-2, y:-1}, {x:-1, y:-2}, {x:-2, y:-3}, {x:-3, y:-2}]
object21 = [{x:0, y:-1}, {x:1, y:-2}, {x:0, y:-3}, {x:-1, y:-2}]
object22 = [{x:2, y:-1}, {x:3, y:-2}, {x:2, y:-3}, {x:1, y:-2}]
objects2 = [object20, object21, object22]

objects = [objects0, objects1, objects2]

# 中心オブジェクトはobject11、その中心は{x:0, y:0}
center_object = object11
center_point = {x:0, y:0}
