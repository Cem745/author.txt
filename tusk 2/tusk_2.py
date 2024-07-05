from math import sqrt

if __name__ == '__main__':
    with open(cirle) as f:
        xc, yc = f.readline().split()
        xc, yc = float(xc), float(yc)
        r = int(f.readline(2))
    with open(dot) as f:
        points = f.readlines()
    for point in points:
        x = float(point.split()[0])
        y = float(point.split()[1])
        s = sqrt((xc - x) ** 2 + (yc - y) ** 2)
        if s == r:
            print(0)
        elif s < r:
            print(1)
        else:
            print(2)
