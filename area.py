def rectangle(w, h):
    """[calculate rectangle]
    
    Arguments:
        w {[float]} -- [width]
        h {[float]} -- [height]
    
    Returns:
        [float] -- [rectangle]
    """

    area = w * h
    return area

def triangle(w, h):
    return .5 * w * h

print("1. Rectangle")
print("2. Triangle")

n = input("Please select option: ")
w = int(input("Width = "))
h = int(input("Height = "))

if n == "1":
    print(rectangle(w, h))
else:
    print(triangle(w, h))