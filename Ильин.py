import os
import matplotlib.pyplot as plt
import math

# Начальные параметры
Xs = -10
Xf = 10
N = 10000

#Функция
def f(x):
    return math.sin(3*math.pi*x)**3 + ((x-1)**2) * (1 + math.sin(3*math.pi)**2)

#Массив с точками по X
X = [i*(Xf-Xs)/N + Xs for i in range(N)]
#Массив значений функции Y
Y = [f(i) for i in X]
#Проверим наличие папки и создадим её при отсутствии
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'results')
if os.path.exists(filename)==False:
    os.mkdir(filename)
#Сохраним путь к файлу в переменную
filename = os.path.join(filename, 'results.json')
#Пишем файл
with open(filename,'w') as F:
    F.write('{\n\t"data": [\n')
    for i in range(len(X)):
        F.write('\t\t{"x": %6.4f, "y": %6.6f}' % (X[i], Y[i]))
        if i!=(len(X)-1):
            F.write(',')
        F.write('\n')
    F.write('\t]\n}')
#Построим график
plt.plot(X,Y)
plt.show()
    
                        
