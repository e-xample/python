# coding: utf-8

import pandas as pd

def main():
	pd_df = pd.read_csv('train.csv',header=0)

	print
	print 'missing data:(before)',len(pd_df['Target3'][ pd_df['Target3'].isnull() ])
	
	median_value = pd_df['Target3'].dropna().median()
	if len(pd_df['Target3'][ pd_df['Target3'].isnull() ]) > 0:
	    pd_df.loc[ pd_df['Target3'].isnull(), 'Target3' ] = median_value

	print 'missing data:(after)',len(pd_df['Target3'][ pd_df['Target3'].isnull() ])
	print 

if __name__ == '__main__':
	main()