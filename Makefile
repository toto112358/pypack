build:
	python3 src/py2elf.py -o src/opt/pypack/bin/py2elf src/py2elf.py
	python3 src/py2elf.py -o src/opt/pypack/bin/pypack src/pypack.py

deb:
	dpkg-deb --build src pypack.deb

clean:
	rm src/opt/pypack/bin/*
	rm pypack.deb

install:
	make build
	make -C src/
	export $(PATH) = $(PATH):/opt/pypack/bin/

uninstall:
	sudo python3 src/pypack.py -p '*'
	sudo rm -r /var/lib/pypack
	sudo rm -r /opt/pypack

dependencies:
	sudo apt -y install gcc cython3 python3-pip python3-lxml
