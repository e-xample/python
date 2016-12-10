# coding: utf-8

import subprocess as sp

def main():
	sp.run(['git', 'add', '.'])
	sp.run(['git', 'commit', '-m', '\'[add] {}\''.format(__file__)])
	sp.run(['git', 'push', 'origin', 'master'])

if __name__ == '__main__':
	main()