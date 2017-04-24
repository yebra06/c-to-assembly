# nasm-dumper
Dump C code into NASM Assembler.

# Instructions
Generate assembly file.
```bash
$ make
```

Use text editor to view assembly file.
```bash
$ vim asm_main.asm
```

Nuke generated assembly files.
```bash
$ make clean
```

Update `cfile_example.c` and/or `settings.py` for a different c file and generate new assembly files.
