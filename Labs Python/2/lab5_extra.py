import numpy as np

# a - матрица с f для метода Гаусса
n = 10
m1 = np.zeros((11,11))
f_start = np.zeros(11)
a = np.zeros((10,11))
x = np.zeros(10)
f = np.zeros(10)

#a_noF - матрица без f
a_noF = np.zeros((10,10))

#Создание матрицы
for i in range(1,n+1):
	f_start[i] = 1/i
	for j in range(1,n+1):
		if i == j:
			m1[i][j] = 1
		else:
			m1[i][j] = 1/(i+j) 

for i in range(n):
	f[i] = f_start[i+1]
	for j in range(n):
		a[i][j] = m1[i+1][j+1]
		a_noF[i][j] = m1[i+1][j+1]
	a[i][10] = f_start[i+1]


#Собственные значения матрицы коэффициентов встроенной функцией
wb, vb = np.linalg.eigh(a_noF)
print('\nВывод собственных значений матрицы коэффициентов')
print('Максимальное собственное значение: %f' %np.max(wb))

#a_noF_inv - обратная матрица к матрицы коэффициентов a_noF
a_noF_inv = np.linalg.inv(a_noF)
wb, vb = np.linalg.eigh(a_noF_inv)
print('Минимальное собственное значение: %f' %np.max(wb))

#Дальше реализация нахождения собственных значений
def eigenvalue(A, v):
    Av = A.dot(v)
    return v.dot(Av)

def power_iteration(A):
    n, d = A.shape
    v = np.ones(d) / np.sqrt(d)
    ev = eigenvalue(A, v)
    while True:
        Av = A.dot(v)
        v_new = Av / np.linalg.norm(Av)
        ev_new = eigenvalue(A, v_new)
        if np.abs(ev - ev_new) < 0.01:
            break
        v = v_new
        ev = ev_new
    return ev_new
print('\nМаксимальное значение реализованное ручным способом: %f' %power_iteration(a_noF))
print('Минимальное значение реализованное ручным способом: %f' %power_iteration(a_noF_inv))