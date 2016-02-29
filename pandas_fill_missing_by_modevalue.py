# coding: utf-8

import pandas as pd

def main():
	pandas_dataframe = pd.read_csv('train.csv',header=0)

	print
	print 'missing data:(before)',len(pandas_dataframe['Target1'][ pandas_dataframe['Target1'].isnull() ])
	
	if len(pandas_dataframe['Target1'][ pandas_dataframe['Target1'].isnull() ]) > 0:
	    pandas_dataframe['Target1'][ pandas_dataframe['Target1'].isnull() ] = pandas_dataframe['Target1'].dropna().mode().values

	print 'missing data:(after)',len(pandas_dataframe['Target1'][ pandas_dataframe['Target1'].isnull() ])
	print 

if __name__ == '__main__':
	main()