import time
from datetime import datetime

time_now= datetime.now()
for N in range(1,100000):                 # N и M это числа, которые мы проверяем на дружественность
    n = 1                                 # n и m это сумма их делителей соответственно
    m = 1
    for i in range(2,N//2 + 1):
        if N%i == 0:
            n+=i
    M = n
    if N>=n:
        continue
    for i in range(2,M//2 + 1):
        if M%i == 0:
            m+=i
    if N == m :
        print('числа ', N, ' и ', M, ' - дружественные')


print(datetime.now() - time_now)
    
