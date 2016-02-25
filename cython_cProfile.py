# coding: UTF-8
import numpy as np
import cProfile,datetime

def main():
	print "start",datetime.datetime.today()
	for x in xrange(0,5):
		for y in xrange(4,5):
			v1 = [x,y]
			v2 = [y,x]
			tmp = np.dot(v1,v2)
	print "end",datetime.datetime.today()

if __name__ == "__main__":
    cProfile.run('main()', sort='time')