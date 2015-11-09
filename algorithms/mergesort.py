#!/usr/bin/python


def mergesort(_list):
	if len(_list) < 2:
		return _list
	mid = len(_list)/2
	left, right = _list[:mid], _list[mid:]
	mergesort(left)
	mergesort(right)
	merge(left, right, _list)

def merge(left, right, _list):
	nleft = len(left)
	nright = len(right)
	i = j = k = 0
	while i < nleft and j < nright:
		if left[i] <=  right[j]:
			_list[k] = left[i]
			i += 1
		else:
			_list[k] = right[j]
			j +=1
		k += 1
	# Append the remainder of left to the _list
	while i < nleft:
		_list[k] = left[i]
		i += 1
		k += 1
	# Append the remained of right to the _list
	while j < nright:
		_list[k] = right[j]
		j += 1
		k += 1

if __name__ == '__main__':
	print 'Welcome to the implementation of Mergesort algorithm'
	a = [2,3,1,22,5,3]
	b = [1]
	c = []
	d = [30, -2, 4]
	print 'Unsorted Lists \na:{} \nb:{} \nc:{} \nd:{}'.format(a,b,c,d)
	for l in [a,b,c,d]:
		mergesort(l)
	print 'Sorted List \na:{} \nb:{} \nc:{} \nd:{}'.format(a,b,c,d)
