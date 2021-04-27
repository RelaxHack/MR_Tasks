import numpy as np
import time
import math
start_time = time.time()

# show_x - показывать корни(1 - да, 0 - нет)
# выбор условия (1 - ограничение итерациями, 2 - точность корней)
# iter_stop - макс.количество итераций(если switch = 1)
# n - размерность (10 - случай билета)
# В конце кода возможность отобразить конкретный
n = 10
show_x = 1
switch = 1
iter_stop = 5
eps = 0.001

# Переменные
#b - вектор свободных членов, s - временная переменная суммы
#A - определенная строчка матрицы(нулевой элемент не брать)
#iteration - итерации, eps - точность
b = np.zeros(n+1)
x = np.zeros(n+1)
x_k = np.zeros(n+1)
a_ii = 1
iteration = 0


#Подготавливаем данные
for i in range(1,n+1):
	b[i] = 1/i

def line_A(i):
	A = np.zeros(n+1)
	for j in range(n+1):
		if i == j:
			A[j] = a_ii
		else:
			A[j] = 1/(i+j)
	return A

def x_k1(x_number):
	s = b[x_number]
	A_x = line_A(x_number)
	for i in range(1,n+1):
		if x_number==i:
			continue
		else:
			s -= A_x[i]*x[i]
	x_k[x_number] = s
x1 = 5


while True:
	for j in range(1,n+1):
		x_k1(j)	
	iteration += 1
	x2 = x[1]
	if switch == 2:
		if abs(x2-x1) < eps:
			break
	x1 = x[1]
	x = x_k
	if switch == 1:
		if iteration == iter_stop:
			break

print('Итераций: %d' %iteration)
print("--- %s секунд ---" % (time.time() - start_time))

if show_x == 1:
	for i in range(1,n+1):
		print('X%d = %f' %(i,x[i]), end = '\t')


#Функция нахождения нормы вектора невязки
x_solve = x[1:]
residual = np.zeros(n)
#Для первой строчки

for i in range(1,n):
    first_lineTest = line_A(i)
    first_line = first_lineTest[1:]
    residual[i] = (first_line.dot(x_solve) - b[i])
z = 0
for j in range(n):
    z += residual[i]**2
print('\nНорма вектора невязки %g' %math.sqrt(z))

#Вывести определенный корень, начиная с 1
#certain_x(0 не выводить)
certain_x = 0
if certain_x > n:
    print("\nКорней меньше, чем отображение желаемого корня")
else:
    if certain_x > 0:
        print('X%d = %f' %(certain_x, x[certain_x]))
        