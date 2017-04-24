#!/usr/bin/python

import subprocess

from settings import C_FILENAME, COMPILER, S_FILENAME, SYNTAX


def main():
	bash = lambda cmd_str: subprocess.call(cmd_str, shell=True)
	bash('{0} -S -masm={1} {2} -o {3}'.format(
		COMPILER, SYNTAX, C_FILENAME, S_FILENAME))


if __name__ == '__main__':
	main()

