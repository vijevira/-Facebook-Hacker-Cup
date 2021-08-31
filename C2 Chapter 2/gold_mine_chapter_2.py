
import numpy as np
import copy

def solve():
	n, k = [*map(int,input().split())]
	a = [*map(int,input().split())]
	E = [[] for _ in range(n)]
	for _ in range(n-1):
		u, v = [*map(int,input().split())]
		u -= 1
		v -= 1
		E[u].append(v)
		E[v].append(u)

	inf = int(1e20)

	def BP(a, b):
		c = [-inf] * (len(a) + len(b) - 1)
		for i in range(len(a)):
			for j in range(len(b)):
				c[i+j] = max(c[i+j],a[i]+b[j])
		return np.array(c)

	def arrmax(a, b):
		a, b = list(a), list(b)
		if len(a) < len(b):
			a += [0] * (len(b) - len(a))
		if len(b) < len(a):
			b += [0] * (len(a) - len(b))
		return np.maximum(a, b)

	f = [0] * n
	g = [0] * n
	h = [0] * n

	def dfs(u, F):
		son = [*filter(lambda x: x!=F, E[u])]
		for v in son:
			dfs(v, u)

		h[u] = np.array([0])
		f[u] = np.array([-inf, a[u]])
		g[u] = np.array([-inf, a[u]])

		for v in son:
			hfg_v = arrmax(arrmax(f[v],g[v]),h[v])
			h_new = BP(h[u], hfg_v)
			f_new = BP(f[u], hfg_v)
			g_new = BP(g[u], hfg_v)
			f_new_2 = BP(h[u], f[v])
			f_new_2 = f_new_2 + a[u]
			f_new_3 = BP(g[u], f[v])
			g_new_2 = BP(f[u], f[v])
			g_new_2 = g_new_2[1:]

			h[u] = h_new
			f[u] = arrmax(f_new, arrmax(f_new_2,f_new_3))
			g[u] = arrmax(g_new, g_new_2)

	dfs(0, -1)

	if k == 0:
		return a[0]

	F = arrmax(f[0],g[0])
	k = min(len(F)-1,k)
	return F[k]




if __name__ == '__main__':
	cas = int(input())
	for ca in range(cas):
		print(f"Case #{ca + 1}: {solve()}")
