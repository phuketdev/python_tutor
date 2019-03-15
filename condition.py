def ticket(age):
    if age <= 5:
        return 0
    else:
        return 100

def ticket2(age):
    if age <= 5 or age >= 60:
        return 0
    else:
        return 100

def ticket2a(age):
    return 0 if age <= 5 or age >= 60 else 100 #ternary (condition อย่างย่อ)

def ticket3(age, is_local):
    if age <= 5 or age >= 60 and is_local:
        return 0
    else:
        return 100

def demo(a):
    if a >= 10 and a <= 20:
        print("ok")
    else:
        print("not ok")

def demo2(a):
    if 10 <= a <= 20:
        print("ok")
    else:
        print("not ok")

demo2(15)