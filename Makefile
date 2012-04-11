build=$(shell date +%s)

release: clean
	todos dynamixel/*.py
	zip $(build).zip Makefile example.py setup.py dynamixel/*.py

linux_release: clean
	fromdos dynamixel/*.py
	zip $(build).zip Makefile example.py setup.py dynamixel/*.py
clean:
	rm -f dynamixel/*.pyc


