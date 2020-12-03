install:
	sudo mkdir /var/lib/pypack/
	sudo touch /var/lib/pypack/packages.lst
	sudo python3 pypack.py -i py2elf -f py2elf.py
	sudo python3 pypack.py -i pypack -f pypack.py
uninstall:
	sudo python3 pypack.py -p '*'
	sudo rm -r /var/lib/pypack
	sudo rm /usr/bin/pypack
	sudo rm /usr/bin/py2elf
dependencies:
	sudo apt -y install gcc cython3 python-pip3 python3-lxml
