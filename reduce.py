# -*- encoding:utf -*-
import sys
import copy
N = 3
def reduce():
	last_key = ''
	t = dict([(i + 1, 0) for i in range(N)])

	matrix = {'A' : copy.deepcopy(t),\
			'B' : copy.deepcopy(t)}

	for line in sys.stdin:
		key, value = line.strip().split('\t')
		i, k = [int(i) for i in key.split('_')]
		tag, j, val = value.split('_')
		j = int(j)
		val = float(val)
		if last_key == '':
			matrix[tag][j] = val
			last_key = key
		else:
			if last_key != key:
				ret_val = 0
				for k in t:
					ret_val += (matrix['A'][k] * matrix['B'][k])
				print ret_val
				matrix = {'A' : copy.deepcopy(t), 'B' : copy.deepcopy(t)}
				last_key = key
			matrix[tag][j] = val
	ret_val = 0
	for k in t:
		ret_val += (matrix['A'][k] * matrix['B'][k])
	print ret_val

if __name__ == '__main__':
	reduce()
