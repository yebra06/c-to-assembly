#!/usr/bin/python

import re
import subprocess

from settings import BAD_PATTERNS, C_FILE, COMPILER, S_FILE, SYNTAX


def clean_generated_assembly():
	with open(S_FILE, 'r+') as asm_src:
		lines = [line for line in asm_src.readlines()]
		asm_src.seek(0)
		asm_src.truncate()
		for line in lines:
			if not re.match(BAD_PATTERNS, line.strip()):
				asm_src.write(line)


def main():
	bash = lambda cmd_str: subprocess.call(cmd_str, shell=True)
	bash('{0} -S -masm={1} {2} -o {3}'.format(COMPILER, SYNTAX, C_FILE, S_FILE))
	clean_generated_assembly()


if __name__ == '__main__':
	main()

