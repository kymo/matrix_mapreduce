# -*- encoding:utf -*-
import sys
import copy
N = 3
def reduce():
	last_key, t = '', dict([(i + 1, 0) for i in range(N)])
	matrix = {'A' : copy.deepcopy(t),\
			'B' : copy.deepcopy(t)}
	for line in sys.stdin:
		key, value = line.strip().split('\t')
		i, k = [int(i) for i in key.split('_')]
		tag, j, val = value.split('_')
		j, val = int(j), float(val)
		if last_key == '':
			matrix[tag][j], last_key = val, key
		else:
			if last_key != key:
				print sum([matrix['A'][k] * matrix['B'][k] for k in t])
				matrix, last_key = {'A' : copy.deepcopy(t), 'B' : copy.deepcopy(t)}, key
			matrix[tag][j] = val
			
	print sum([matrix['A'][k] * matrix['B'][k] for k in t])
	
if __name__ == '__main__':
	reduce()
