def f(x):
	m = 1 
	for n in range(2, x):
		if not (x % n): 
			m = n 
	return m

print(f(1), f(2), f(3), f(17), f(100), f(169))