def getIdealNums(low, high):
	res = 0 
	i = 1
	while i <= high: 
		j = i 
		while j <= high: 
			if j >= low: 
				res += 1 
			j *= 5
		i *= 3
	return res
        

print(getIdealNums(1, 10))

# Get the max 5^power
# Get the max 3^power