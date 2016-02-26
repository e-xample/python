# coding: utf-8

import pandas as pd

def main():
	train_df = pd.read_csv('train.csv',header=0)
	newName = 'Gender'
	target = 'Sex'
	class1 = 'female'
	class2 = 'male'
	train_df[newName] = train_df[target].map( {class1: 0, class2: 1} ).astype(int)

	print train_df

if __name__ == '__main__':
	main()