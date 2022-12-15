def chinh_phuong(n):
    check = 0
    for i in range(1, n//2+1):
        if i**2 == n :
            check=1
            break
    if check == 1:
        print(n, 'là số chính phương')
    else:
        print(n,'không là số chính phương')

n= int(input("n= "))
chinh_phuong(n)