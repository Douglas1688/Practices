"""def numero_par(num):
    if num %2==0:
        return True

numero = [17,24,7,39,8,51,92]
print(list(filter(numero_par,numero)))
"""
lst = [17,24,7,39,8,51,92]
print(list(filter(lambda num_par : num_par %2 ==0 , lst)))
