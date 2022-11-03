from funkcije import *
import time

methods = ['trust-constr']

N_s = [4, 6, 8, 10 ,12, 14, 16, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44]

f_time = open("llong_time.txt", "a")
f_E = open("llong_E.txt", "a")
for meth in methods:

	line_time = meth
	line_E = meth

	print(meth)
	for N in N_s:
		comp_time = 1000000
		min_E_val = 1000000
		for i in range(1):
			print(N)
			init_guess = [np.random.random()*2*np.pi for _ in range(N)] + [np.arccos((np.random.random()-1/2)*2) for _ in range(N)]

			start = time.time()
			res = opt.minimize(multipot, init_guess, args=(N), method=meth, tol=10**(-4))
			end = time.time()

			if multipot(res.x, N) < min_E_val:
				min_E_val = multipot(res.x, N)
				comp_time = end-start

		line_time += ','+str(comp_time)
		line_E += ','+str(min_E_val)

	line_time += '\n'
	line_E += '\n'
	f_time.write(line_time)
	f_E.write(line_E)

f_time.close()
f_E.close()