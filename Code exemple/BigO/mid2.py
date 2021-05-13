def count_money(k, n, w):
    money = n
    for i in range(w):
        money = money - k * (i + 1)
    if money>0:
        print(0)
    else:
        print(abs(money))



k, n, w = map(int, input().split(' '))
count_money(k, n, w)
