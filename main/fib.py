# Числа Фибоначчи — числовой ряд, при котором каждое последующее число равно сумме двух предыдущих


# Получить число Фибоначчи по его номеру
def fib(n):
    a = [1, 1] 
      
    for i in range(2, n): 
        a.append(a[i-1] + a[i-2]) 
      
    for i in range(n): 
        print(a[i]) 
     
    return a[-1]
