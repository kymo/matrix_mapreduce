# -*- encoding:utf8 -*-
# calculate matrix A(M * N) * B(N * L) 
import sys

M = 4
N = 3
L = 2

def map():
	for line in sys.stdin:
		tag, i, j, v_i_j = line.strip().split('\t')
		# construct L pairs <key, value>
		if tag == 'A':
			for k in range(L):
				key = i + "_" + str(k + 1)
				value = 'A_' + j + '_' + v_i_j
				print key + '\t' + value
		else:
			j, k, v_j_k = i, j, v_i_j
			for i in range(M):
				key = str(i + 1) + "_" + k
				value = 'B_' + j + "_" + v_j_k
				print key + '\t' + value

if __name__ == '__main__':
	map()
