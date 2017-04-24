# c-to-assembly
Dump C code into machine generated assembly.

# Development
This program was developed on Linux Ubuntu 16.04

# Instructions
Generate assembly file.
```bash
$ make
```

Use text editor to view assembly file.
```bash
$ vim asm_main.s
```

Nuke generated assembly files.
```bash
$ make clean
```

Update `cfile_example.c` and/or `settings.py` for a different c file and generate new assembly files.
