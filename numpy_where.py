# -*- coding: utf-8 -*- 
import numpy as np

def main():

    y = np.random.rand(10)	# 探索対象
    x = np.where((y>=0.2)&(y<0.8)) # 探索，探索条件
    # 結果を表示
    print(u"all："+str(y))
    print(u"0.2以上0.8未満のデータがある要素番号："+str(x[0]))
    print y[x[0]]

if __name__ == '__main__':
    main()
