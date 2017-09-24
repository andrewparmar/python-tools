def reverse(x):
	
		
	a = str(x).strip("-")
	b = int(a[::-1])

	if x < 0:
		b *= -1

	if b > 2147483647 or b < -2147483647:
			return 0
	else:
		return b

print(reverse(1534236469))

