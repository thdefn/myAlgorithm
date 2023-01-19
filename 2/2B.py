# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def is_ordered(data, n):
	fwd = 0
	for i in range(n):
		if(fwd>data[i]):
			return False
		fwd = data[i]
	return True


if __name__ == "__main__":
	n = int(input())
	data = [ int(w) for w in input().split() ]
	result = is_ordered(data, n)
	if result : # True
		print("YES")
	else:
		print("NO") # False