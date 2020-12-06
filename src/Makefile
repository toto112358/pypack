install:
	sudo mkdir /var/lib/pypack/
	sudo touch /var/lib/pypack/packages.lst
	sudo chmod 777 /var/lib/pypack
	sudo chmod 777 /var/lib/pypack/*
	sudo su -c 'mkdir /opt/pypack && chmod 777 /opt/pypack && mkdir /opt/pypack/bin'
	sudo python3 DEBIAN/postinst
	python3 pypack.py -i py2elf -f py2elf.py
	python3 pypack.py -i pypack -f pypack.py
