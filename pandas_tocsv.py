# coding: utf-8

import pandas as pd

def main():
	input_filename = 'train.csv'
	headerin = 0
	train_df = pd.read_csv(input_filename,header=headerin)

	output_filename = 'train_.csv'
	train_df.to_csv(output_filename)

if __name__ == '__main__':
	main()