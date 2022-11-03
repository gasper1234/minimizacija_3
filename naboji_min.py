from funkcije import *

N=10

init_guess = [np.random.random()*2*np.pi for _ in range(N)] + [np.arccos((np.random.random()-1/2)*2) for _ in range(N)]

print(multipot(init_guess, N))
res = opt.minimize(multipot, init_guess, args=(N))
print(multipot(res.x, N))


res_cart = to_cart(res.x, N)
init_guess_cart = to_cart(init_guess, N)

#povezave in ploti
res_cart = to_cart(res.x, N)
init_guess_cart = to_cart(init_guess, N)

H = hull(res_cart)
skupaj = H.simplices

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_ylim(-1.1, 1.1)
ax.set_xlim(-1.1, 1.1)
ax.set_zlim(-1.1, 1.1)

ax.scatter(res_cart[:, 0], res_cart[:, 1], res_cart[:, 2], color='red')
#ax.scatter(init_guess_cart[:, 0], init_guess_cart[:, 1], init_guess_cart[:, 2], color='blue')
for i in skupaj:
	for j in range(len(i)):
		for k in range(j+1, len(i)):
			x_l = [res_cart[i[j]][0], res_cart[i[k]][0]]
			y_l = [res_cart[i[j]][1], res_cart[i[k]][1]]
			z_l = [res_cart[i[j]][2], res_cart[i[k]][2]]
			ax.plot(x_l, y_l, z_l, color='k')


plt.show()
