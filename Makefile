build:
	pyinstaller -F main.py --hidden-import pyexcel_io.writers.csv_in_file --hidden-import pyexcel_xls  --hidden-import pyexcel_io.readers.csv_in_file --hidden-import pyexcel_xlsx

clean:
	rm -rf dist