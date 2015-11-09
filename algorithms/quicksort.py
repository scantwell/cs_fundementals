#!/usr/bin/python
from random import randint
from numpy import median

def get_pivot(_list, start, end):
	p0, p1, p2 = randint(start, end), \
					 randint(start, end), \
					 randint(start, end)
	pivot = median([_list[p0], _list[p1], _list[p2]]).astype(int)
	idx = _list.index(pivot)
	end_idx = len(_list[start:end]) + start
	_list[idx], _list[end_idx] = _list[end_idx], _list[idx]
	return pivot

def partition(_list, start, end):
	pivot = get_pivot(_list, start, end)
	wall = start
	currPos = start
	while currPos < end:
		if pivot >= _list[currPos]:
			_list[currPos], _list[wall] = _list[wall], _list[currPos]
			wall += 1
		currPos += 1
	end_idx = len(_list[start:end]) + start
	_list[wall], _list[end_idx] = _list[end_idx], _list[wall]
	return wall
	
def quicksort(_list, start, end):
	if len(_list[start:end]) < 2:
		return _list
	wall = partition(_list, start, end)
	quicksort(_list, start, wall)
	quicksort(_list, wall+1, end)
	
if __name__ == '__main__':
	print 'Welcome to quicksort implementation.'
	a = [2,3,1,22,5,3]
	b = [1]
	c = []
	d = [30, -2, 4]
	print 'Unsorted Lists \na:{} \nb:{} \nc:{} \nd:{}'.format(a,b,c,d)
	for l in [a,b,c,d]:
		quicksort(l, 0, len(l)-1)
	print 'Sorted List \na:{} \nb:{} \nc:{} \nd:{}'.format(a,b,c,d)
