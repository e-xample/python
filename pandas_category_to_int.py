# coding: utf-8

import pandas as pd
import numpy as np

def main():
	pd_df = pd.read_csv('train.csv',header=0)

	print pd_df.Target1

	if len(pd_df.Target1[ pd_df.Target1.isnull() ])>0:
		pd_df.loc[ pd_df.Target1.isnull(), 'Target1' ] = pd_df.Target1.dropna().mode().values

	Ports = list(enumerate(np.unique(pd_df.Target1)))
	Ports_dict = { name:i for i,name in Ports }
	pd_df.Target1 = pd_df.Target1.map( lambda x: Ports_dict[x] ).astype(int)

	print pd_df.Target1


if __name__ == '__main__':
	main()