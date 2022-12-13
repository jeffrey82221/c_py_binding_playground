# Ctype 

This is the python library that allow C library (.so) to be embedded into python. 

# Compile Step: 

NOTE: currently, I need to compile the .c file on mac mini
and execute it on my macbook air.

```linux
gcc -fPIC -shared -o print.so print.c
```

# TODO:
- [ ] demo of `print.so` and `use_print` calling `print`
- [ ] demo of `add` and `main` calling `add`
- [ ] demo of `sum` and `main` calling `sum`
- [ ] demo of cutomized numpy operation based on numpy array. 