#coding:utf-8 

import multiprocessing 


def dummy(x,y):
	print 'process start',y

	cal_count = 65000000
	# dummy calclation
	i = 0
	for c in xrange(cal_count):
		i += 1
	# end 

	print 'process end',y
	return x*y 

def multi(): 
	process = 4
	p = multiprocessing.Pool(process) 
	data = [(dummy,i*2,i) for i in xrange(process)] 
	return p.map(wrapper, data)

def wrapper(tuple_data): 
	return tuple_data[0](tuple_data[1],tuple_data[2]) 

if __name__ == "__main__": 

	# multiprocessing
	result_multi = multi()

# memo