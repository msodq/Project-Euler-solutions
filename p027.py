# 
# Solution to Project Euler problem 27
# by Project Nayuki
# 
# http://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 

import eulerlib, itertools


def compute():
	ans = max(((a, b) for a in range(-999, 1000) for b in range(-999, 1000)), key=count_consecutive_primes)
	return str(ans[0] * ans[1])


isprimecache = list(map(eulerlib.is_prime, range(1000)))

def count_consecutive_primes(ab):
	a, b = ab
	for i in itertools.count():
		n = i * i + i * a + b
		if n <= 1 or (n < len(isprimecache) and not isprimecache[n]) or not eulerlib.is_prime(n):
			return i


if __name__ == "__main__":
	print(compute())