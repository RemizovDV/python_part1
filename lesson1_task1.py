#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь. 
x =  int(input('Ввведите трехзначное число: ')) 
  
ed = x % 10 
des = int(((x % 100) - ed)/10) 
sot = x // 100 

print(f'Сумма цифр числа: {ed + des + sot}') 
print(f'Произведение цифр числа: {ed * des * sot}')