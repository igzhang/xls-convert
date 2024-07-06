# xls-convert
A tool used for compatible excel format,call by bin.

# CLI Usage
1. Download binary
2. xls-convert -i 1.xls -o 2.csv

# Docker Usage
1. Pull and run docker image
2. curl http://host:6000/convert?from=/app/1.csv&to=/app/1.xls

# Build
```shell
make -B build
```
