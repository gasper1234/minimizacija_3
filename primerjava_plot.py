from funkcije import *
import csv
from sta import *

methods = ['Nelder-Mead', 'Powell', 'CG', 'BFGS', 'trust-constr']
methods = ['Powell', 'BFGS', 'trust-constr']

#N_s = [4, 6, 8, 10 ,12 , 15, 20]

N_s = [4, 6, 8, 10 ,12, 14, 16, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44]
N_s_t = [4, 6, 8, 10 ,12, 14, 16, 20, 22, 24, 26, 28, 30, 32, 34, 36]

E_true = np.array([3.674234614, 9.985281374, 19.675287861, 32.716949460, 49.165253058, 80.670244114, 150.881568334])


E_ss = []
t_ss = []

with open('llong_E.txt') as f:
	lines = f.readlines()
	for line in lines:
		line_l = line.split(',')
		E_ss.append([float(i) for i in line_l[1:]])
	f.close()

with open('llong_time.txt') as f:
	lines = f.readlines()
	for line in lines:
		line_l = line.split(',')
		t_ss.append([float(i) for i in line_l[1:]])
	f.close()

E_ss = np.array(E_ss)
t_ss = np.array(t_ss)

fig, ax = plt.subplots()


ax.plot(N_s, np.log(t_ss[1]), 'x', label='BFGS')
ax.plot(N_s, np.log(t_ss[2]), 'x', label='trust-constr')
#ax.plot(N_s[3:], linfit(N_s[3:], np.log(t_ss[1])[3:])(N_s[3:]), '-', label='log(t)=0.19N-2.2')
ax.set_xlabel('N')
ax.set_ylabel('log(t)')
#ax.legend()
#ax.set_yscale('log')
ax.legend()
plt.show()
#plotanje več grafov
'''
fig, ax = plt.subplots(2, 1)

for i in range(len(E_ss)):
	ax[0].plot(N_s, (E_ss[i]-E_true)/E_true, 'x:', label=methods[i]+r' $10^{-3}$')

for i in range(len(E_ss)):
	ax[1].plot(N_s, t_ss[i], 'x:', label=methods[i]+r' $10^{-3}$')


ax[0].set_ylabel(r"$(E-E_{min})/E_{min}$")
ax[0].set_yscale('log')
ax[0].legend()
ax[1].set_ylabel(r"t")
ax[1].set_xlabel("N")
ax[1].legend()
plt.show()
'''