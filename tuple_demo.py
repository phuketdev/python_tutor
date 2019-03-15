##### Tuple ไม่สามารถเปลี่ยนแปลงแก้ไขค่าได้ ######

# point = 1, 7
# print(point[1])
#
# point_b = (2, 10)
# print(point_b[1])

# th = "Thailand", 5, 10, 15
# print(th[1] + th[2] + th[3])
#
# monsters = ("pikuchu", "bulbasaur", "eevee")
# print(monsters[1])

# หาค่าระยะทาง ((x1-y1)**2 - (x2-y2)**2) ** .5

def distance(point_a, point_b):
    return ((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2 ) ** .5

point_a = (1, 7)
point_b = 1, 10

print(distance(point_a, point_b))


