# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько составных.
def easy_number(n):
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

i = int(input("Введите число: "))
c_e = 0
c_ne = 0
while i!=0:
    if easy_number(i):
        c_e+=1
    else:
        c_ne+=1
    i = int(input("Введите число: "))
print("Простых чисел: " + str(c_e) + ", Составных чисел: " + str(c_ne))
