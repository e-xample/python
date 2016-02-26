# coding: utf-8

import pandas as pd

def main():
	filename = 'train.csv'
	headerin = 0
	train_df = pd.read_csv(filename,header=headerin)
	print train_df

if __name__ == '__main__':
	main()