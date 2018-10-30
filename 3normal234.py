# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(li):
    print("исходный список",li)
    n = 1 
    while n < len(li):
        for i in range(len(li)-n):
            if li[i] > li[i+1]:
                li[i],li[i+1] = li[i+1],li[i]
        n += 1
    print("отсортированный список",li)
    return li

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
sort_to_max([1, -4, 0.6,3.14, 0.7, 0.61, 7,0.59, 0.62])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func,iter):
    res=[]
    for i in iter:
        if func(i):
            res.append(i)
    return res


print(my_filter(lambda x: x >= 10, [2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
print(list(filter(lambda x: x >= 10, [2, 10, -12, 2.5, 20, -11, 4, 4, 0] )))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def isparallelogramm(a1,a2,a3,a4):
    def centerpoint(a,b):
        return ((a[0]+b[0])/2,(a[1]+b[1])/2)
    if (a1 == a3)or(a1 == a2)or(a1 == a4)or(a2==a3)or(a2==a4)or(a3==a4): return False
    return centerpoint(a1,a3) == centerpoint(a2,a4)