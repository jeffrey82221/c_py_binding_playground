# Nuitka

This is a package that compile python into C executable. 

# Compile

## Generate main executable: 

### compile 
```
python -m nuitka main.py --lto=no \
    --nofollow-import-to=pytest --python-flag=nosite,-O --prefer-source-code \
    --clang --plugin-enable=anti-bloat,implicit-imports,data-files,pylint-warnings

rm -r main.build
```

```
python -m nuitka main_sum.py --lto=no \
    --nofollow-import-to=pytest --python-flag=nosite,-O --prefer-source-code \
    --clang --plugin-enable=anti-bloat,implicit-imports,data-files,pylint-warnings

rm -r main.build
```

### run:
```
./main.bin
```

## Generate standalone executable: 

### compile 
```
python -m nuitka main.py --standalone --lto=no \
    --nofollow-import-to=pytest --python-flag=nosite,-O --prefer-source-code \
    --clang --plugin-enable=anti-bloat,implicit-imports,data-files,pylint-warnings
```
### run
```
./main.dist/main
```
## Generate so module that can be imported

### compile 
```
python -m nuitka add.py --module --lto=no \
    --nofollow-import-to=pytest --python-flag=nosite,-O --prefer-source-code \
    --clang --plugin-enable=anti-bloat,implicit-imports,data-files,pylint-warnings
```
```
python -m nuitka sum.py --module --lto=no \
    --nofollow-import-to=pytest --python-flag=nosite,-O --prefer-source-code \
    --clang --plugin-enable=anti-bloat,implicit-imports,data-files,pylint-warnings

```
### import 
```
>> from add import add 
>> add
<compiled_function add at 0x105aa6e50>
```
