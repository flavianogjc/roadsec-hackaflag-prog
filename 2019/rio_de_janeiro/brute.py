def brute(arr, cota):
	maior = -1
	a, b = None, None
	for i in xrange(len(arr)):
		for j in xrange(i, len(arr)):
			s = sum(arr[i:j+1])
			p = j-i+1
			if(s>p*cota and p>maior):
				maior = p
				a = i
				b = j
	if(a==None or b==None):
		return 0
	else:
		return abs(b-a)+1, a, b

cota = 10
if __name__=='__main__':
	print brute(A, cota)
	
