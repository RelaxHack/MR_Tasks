import numpy as np
import math as m

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

#Функция нахождения нормы вектора невязки
def residualFunc(solve):
	z = 0
	residual = f - a_noF.dot(solve)
	for i in range(10):
		z += residual[i]**2
	return m.sqrt(z)

#Метод Гаусса
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Деление на ноль!')
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j] 
    x[i] = x[i]/a[i][i]

print('\nРешение методом Гаусса: ')
for i in range(n):
    print('X%d = %f' %(i+1,x[i]), end = '\t')

#Вывод нормы вектора невязки метода Гаусса
print('\n\nНорма вектора невязки метода Гаусса: %g' %residualFunc(x))


#Метод ПВР
def sor_solver(A, b, omega, initial_guess, convergence_criteria):
    phi = initial_guess[:]
    residual = np.linalg.norm(np.matmul(A, phi) - b)
    while residual > convergence_criteria:
        for i in range(A.shape[0]):
            sigma = 0
            for j in range(A.shape[1]):
                if j != i:
                    sigma += A[i][j] * phi[j]
            phi[i] = (1 - omega) * phi[i] + (omega / A[i][i]) * (b[i] - sigma)
        residual = np.linalg.norm(np.matmul(A, phi) - b)
    return phi

residual_convergence = 1e-8
omega = 0.5 
initial_guess = np.zeros(10)

phi = sor_solver(a_noF, f, omega, initial_guess, residual_convergence)
print('\n\nРешение методом ПВР: ')
for i in range(n):
    print('X%d = %f' %(i+1,phi[i]), end = '\t')
    
#Вывод нормы вектора невязки метода ПВР
print('\n\nНорма вектора невязки метода ПВР: %g' %residualFunc(phi))

print('\nОбусловленность матрицы: %f' %(np.linalg.norm(a_noF) * np.linalg.norm(np.linalg.inv(a_noF))))
#print(np.linalg.cond(a_noF, p = 'fro'))

#Собственные значения матрицы коэффициентов
wb, vb = np.linalg.eigh(a_noF)
print('\nВывод собственных значений матрицы коэффициентов')
print('Минимальное собственное значение: %f' %np.min(wb))
print('Максимальное собственное значение: %f' %np.max(wb))

