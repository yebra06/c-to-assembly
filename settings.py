BAD_PATTERNS = '(' + ')|('.join((
	'^.cfi|^.comm|^.local|^#|^.subsections',
	'^.macosx',
)) + ')'

C_FILE = 'cfile_example.c'
S_FILE = 'asm_main.s'

COMPILER = 'gcc'
SYNTAX = 'intel'
