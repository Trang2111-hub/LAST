import math
def giaiPTB2(a, b, c):
    # kiểm tra các hệ số
    if (a == 0):
        if (b == 0):
            if (c==0):
                print("Phương trình có vô số nghiệm!")
            else:
                print("Phương trình vô nghiệm!")
        else:
            print("Phương trình có một nghiệm: x = ", + (-c / b))
        return

    # tính delta
    delta = b * b - 4 * a * c
    # tính nghiệm
    if (delta > 0):
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Phương trình có 2 nghiệm là: x1 =", x1, "và x2 =", x2)
    elif (delta == 0):
        x1 = (-b / (2 * a));
        print("Phương trình có nghiệm kép: x1 = x2 =", x1)
    else:
        print("Phương trình vô nghiệm!");
a=int(input("Nhập hệ số a:" ))
b=int(input("Nhập hệ số b:"))
c=int(input("Nhập hệ số c:"))
giaiPTB2(a,b,c)