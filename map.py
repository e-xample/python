# coding:utf-8
import numpy as np

def square(x):
	return x*x

def main():
	x = np.linspace(0,10,5)
	print 'x vector',str(x)
	print 'square x',str(map(square,x))

if __name__ == '__main__':
	main()