from funkcije import *
import time

methods = ['Powell']

val_ss = []

N_s = [4, 6, 8, 10, 12]
E_true = np.array([3.674234614, 9.985281374, 19.675287861, 32.716949460, 49.165253058])

for meth in methods:

	val_s = []

	print(meth)
	for N in N_s:
		val_s = []
		comp_time = 1000000
		min_E_val = 1000000
		for i in range(5):
			print(N)
			init_guess = [np.random.random()*2*np.pi for _ in range(N)] + [np.arccos((np.random.random()-1/2)*2) for _ in range(N)]

			start = time.time()
			res = opt.minimize(multipot, init_guess, args=(N), method=meth, tol=10**(-4))
			end = time.time()

			val_s.append(multipot(res.x, N))

		val_ss.append(val_s)

val_ss = np.array(val_ss)

for i in range(5):
	plt.plot(N_s, (val_ss[:, i]-E_true)/E_true, 'x:', label=str(i))

plt.xlabel('N')
plt.legend()
plt.ylabel(r"$(E-E_{min})/E_{min}$")
plt.show()