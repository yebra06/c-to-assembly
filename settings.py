import re
import sys

# Pre compile regex based on machines platform.
# Note: darwin is Mac and nt is Windows.
BAD_PATTERNS = re.compile({
	'linux2': '^.cfi|^.comm|^.local|^#|^.subsections|^.ident',
	'darwin': '^.macosx',
}.get(sys.platform, 'linux2'))

C_FILE = 'cfile_example.c'
S_FILE = 'asm_main.s'

COMPILER = 'gcc'
SYNTAX = 'intel'
