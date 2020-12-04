build:
	python3 src/py2elf.py -o src/usr/bin/py2elf src/py2elf.py
	python3 src/py2elf.py -o src/usr/bin/pypack src/pypack.py
	dpkg-deb --build src pypack.deb
clean:
	rm src/usr/bin/*
	rm pypack.deb
install:
	sudo mkdir /var/lib/pypack/
	sudo touch /var/lib/pypack/packages.lst
	sudo python3 scr/pypack.py -i py2elf -f scr/py2elf.py
	sudo python3 scr/pypack.py -i pypack -f scr/pypack.py
uninstall:
	sudo python3 scr/pypack.py -p '*'
	sudo rm -r /var/lib/pypack
	sudo rm /usr/bin/pypack
	sudo rm /usr/bin/py2elf
dependencies:
	sudo apt -y install gcc cython3 python3-pip python3-lxml
