# come_x = 4
# pay_y = 3
# per_head = 100
# pax = 9
#
# total = (pax // come_x) * (pay_y * per_head) + (pax % come_x * per_head)
# print(total)

def com_x_pay_y(pax, per_head=199, come_x=4, pay_y=3):
    total = (pax // come_x) * (pay_y * per_head) + (pax % come_x * per_head)
    return total

print(com_x_pay_y(9))