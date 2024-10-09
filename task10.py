# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".
def easy_number(n):
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

c = int(input("Введите кол-во чисел: "))
count = 0
min = 0
max = 0
for delta in range(c):
    i = int(input("Введите число " + str(delta+1) + ": "))
    if(easy_number(i)):
        if(i>max or max == 0):
            max = i
        if(i<min or min == 0):
            min = i
    
if(max==0):
    print("Таких чисел нет")
else:
    print("Минимальное число: " + str(min) + " , максимальное число: "+ str(max))

