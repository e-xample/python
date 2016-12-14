# using: utf-8

import pandas as pd
import random, datetime
from random import randrange
from datetime import timedelta

def main():
	list_empid = []
	list_empname = []
	list_deptid = []
	list_hiredate = []
	list_deleteflag = []

	for x in xrange(2000000):
		empid = x
		empname = '"' + random_string(6) + '"'
		deptid = random.randint(0, 100)
		year = random.randint(1990, 2016)
		month = random.randint(1, 12)
		day = random.randint(1, 31)
		hiredate = "-".join(map(lambda n: str(n), [year, month, day]))
		hiredate = '"' + hiredate + '"'
		deleteflag = random.randint(0, 1)

		list_empid.append(empid)
		list_empname.append(empname)
		list_deptid.append(deptid)
		list_hiredate.append(hiredate)
		list_deleteflag.append(deleteflag)

	csv_out(
		list_empid, 
		list_empname, 
		list_deptid, 
		list_hiredate, 
		list_deleteflag)


def random_string(size):
	source_str = 'abcdefghijklmnopqrstuvwxyz'
	random.choice(source_str)
	return "".join([random.choice(source_str) for x in xrange(size)])

def csv_out(empid, empname, deptid, hiredate, deleteflag):
	df = pd.DataFrame(
		{
			'empid': empid,
			'empname': empname,
			'deptid': deptid,
			'hiredate': hiredate,
			'deleteflag': deleteflag
		},
		columns=['empid', 'empname', 'deptid', 'hiredate', 'deleteflag']
	)
	df.to_csv('sample_emp.csv', index=False)

if __name__ == '__main__':
  main()
