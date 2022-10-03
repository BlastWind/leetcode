nodes = []
representative = list(range(len(nodes)))
size = list(range(len(nodes)))

def find(u):
	if representative[u] == u: return u 
	representative[u] = find(representative[u])
	return representative[u]

def combine(u, v): 
	u = find(u)
	v = find(v)

	if u == v: return 

	if size[u] < size[v]:
		representative[u] = v
		size[u] += size[v] 
	else: 
		representative[v] = u
		size[v] += size[u]
