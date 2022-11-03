from scipy import optimize as opt
import numpy as np
import matplotlib.pyplot as plt

#celoten cas je 1

dt = 0.1

v_0 = 0.5

v_s_0 = [v_0+i/round(1/dt)*(2-v_0) for i in range(1, round(1/dt))]
print(v_s_0)


def f_lag(v_s, lamb, dt, beta, v_max):
	sum_all = 0
	sum_all += (v_s[0] - v_0)**2/dt
	sum_all += np.exp(beta*((v_0+v_s[0])/2-v_max))*dt
	sum_all -= lamb*(v_0+v_s[0])/2*dt
	for i in range(len(v_s)-1):
		sum_all += (v_s[i+1] - v_s[i])**2/dt
		sum_all += np.exp(beta*((v_s[i+1]+v_s[i])/2-v_max))*dt
		sum_all -= lamb*(v_s[i+1]+v_s[i])/2*dt
	return sum_all

res = opt.minimize(f_lag, v_s_0, args=(2, dt, 1, 1.1))
print(res.x)
from scipy import integrate
integ = integrate.simpson([v_0]+res.x, [dt*i for i in range(len(res.x)+1)])
print(integ)
plt.plot([i*dt for i in range(1, round(1/dt))], res.x)
plt.show()

#todo naredi bisekicjo prestudirja zadevo