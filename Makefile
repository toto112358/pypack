build:
	python3 src/py2elf.py -o src/opt/pypack/bin/py2elf src/py2elf.py
	python3 src/py2elf.py -o src/opt/pypack/bin/pypack src/pypack.py

deb:
	make build
	dpkg-deb --build src pypack.deb

clean:
	rm src/opt/pypack/bin/*
	rm pypack.deb

install:
	make build
	make -C src/

stupid_install:
	echo this is a stupid install for debian
	make dependencies && make && dpkg -i pypack.deb && make clean

uninstall:
	sudo python3 src/pypack.py -p '*'
	sudo rm -r /var/lib/pypack
	sudo rm -r /opt/pypack

dependencies:
	sudo apt -y install gcc cython3

print_dependencies:
	echo gcc cython			# in some distros, cython3 is referred to cython
