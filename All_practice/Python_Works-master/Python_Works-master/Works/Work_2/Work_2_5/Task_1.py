def ham_dist(num1, num2): return bin(num1 ^ num2).count('1')


print(ham_dist(0b1100, 0b0011))
