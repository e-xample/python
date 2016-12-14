# -*- coding: utf-8 -*-
""" comment """

import random


def random_string(size):
    source_str = 'abcdefghijklmnopqrstuvwxyz'
    random.choice(source_str)  #a〜zでランダムに１文字
    return "".join([random.choice(source_str) for x in xrange(size)])

if __name__ == '__main__':
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

        line = ",".join(map(lambda n: str(n), [empid, empname, deptid, hiredate, deleteflag]))
        print(line)
