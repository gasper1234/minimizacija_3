from scipy import optimize as opt
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

#celoten cas je 1

dt = 0.05

v_0 = 0.5

#v_s_0 = [v_0+i/round(1/dt)*(2-v_0) for i in range(1, round(1/dt))]
v_s_0 = [v_0 for i in range(1, round(1/dt))]

print(v_s_0)

def f_lag(v_s, lamb, dt, beta, v_max):
	trig = 0
	sum_all = 0
	sum_all += (v_s[0] - v_0)**2/dt
	#sum_all += np.exp(beta*((v_0+v_s[0])/2-v_max))*dt
	sum_all -= lamb*(v_0+v_s[0])/2*dt
	sum_way = (v_0+v_s[0])/2*dt
	for i in range(len(v_s)-1):
		sum_all += (v_s[i+1] - v_s[i])**2/dt
		#sum_all += np.exp(beta*((v_s[i+1]+v_s[i])/2-v_max))*dt
		sum_all -= lamb*(v_s[i+1]+v_s[i])/2*dt
		sum_way += (v_s[i+1]+v_s[i])/2*dt
		#radar na pol poti
		if sum_way > 0.5 and trig == 0:
			if ((v_s[i+1]+v_s[i])/2-beta) > 0:
				sum_all += ((v_s[i+1]+v_s[i])/2-beta)*5
			trig = 1
	return sum_all

#recc
def recc(beta):
	lamb_min = 1
	lamb_maks = 100
	while lamb_maks-lamb_min > 10**(-3):
		lamb_mid = (lamb_min+lamb_maks)/2
		res = opt.minimize(f_lag, v_s_0, args=(lamb_mid, dt, beta, 1.1), method='Powell', tol=10**(-5))
		integ = integrate.simpson([v_0]+[i for i in res.x], [dt*i for i in range(len(res.x)+1)])
		print(integ)
		if integ >= 1:
			lamb_maks = lamb_mid
		else:
			lamb_min = lamb_mid
	return res.x, lamb_mid, integ

beta_s = [0.4, 0.8, 1, 1.1]
lamb_s = np.linspace(0.1, 20, 100)

for beta in beta_s:
	res, lamb, integ = recc(beta)
	plt.plot([i*dt for i in range(round(1/dt))], [v_0]+[i for i in res], label=R'$v_{max}$='+str(beta)+r' $\int_0^1 v \mathrm{d}t=$'+str(round(integ, 2)))
plt.ylabel('v(t)')
plt.xlabel('t')
plt.legend()
plt.show()

#plot bisek fo beta_s
'''
for beta in beta_s:
	integ_for_lambs = []
	for lamb in lamb_s:
		res = opt.minimize(f_lag, v_s_0, args=(lamb, dt, beta, 1.1))
		integ = integrate.simpson([v_0]+[i for i in res.x], [dt*i for i in range(len(res.x)+1)])
		integ_for_lambs.append(integ)
	plt.plot(lamb_s, integ_for_lambs, '-', label=r'$v_{max}$'+str(beta))
plt.xlabel(r'$\lambda$')
plt.ylabel(r'$\int_0^1 v \mathrm{d}t$')
plt.hlines(1, 0, 20, 'k')
plt.legend()
plt.show()
'''

'''
plt.plot([i*dt for i in range(1, round(1/dt))], res.x)
plt.show()
'''
