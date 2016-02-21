# -+- coding: utf-8 -*-

###
# numpy 線形補間 
###

import matplotlib.pylab as plt
import numpy as np
 
def plot_sin():
	xp = np.linspace(0, 2*np.pi, 10)
	fp = np.sin(xp)
	plt.plot(xp, fp, 'o', label='sin')
	return xp,fp

def plot_interpolation(xp,fp):
	x = np.linspace(0, 2*np.pi, 50)

	### 線形補間 ###
	# x: array_like. The x-coordinates of the interpolated values.
	# xp: 1-D sequence of floats. The x-coordinates of the data points, must be increasing if argument period is not specified. 
	# fp: 1-D sequence of floats. The y-coordinates of the data points, same length as xp.
	# yinterp: Returns the one-dimensional piecewise linear interpolant to a function with given values at discrete data-points.
	yinterp = np.interp(x, xp,fp)
	### 線形補間 ###
	
	plt.plot(x, yinterp, 'r-x', label='interpolation')

def plot_show(xp,fp):
	plt.grid()
	plt.xlabel('xaxis')
	plt.ylabel('yaxis')
	plt.legend(loc='upper right')
	plt.xlim((np.min(xp),np.max(xp)))
	plt.show()

def main():
	xp,fp = plot_sin()
	plot_interpolation(xp,fp)
	plot_show(xp,fp)

if __name__ == '__main__':
	main()
