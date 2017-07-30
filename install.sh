#!/bin/bash

if [ $1 == "init" ]
then
    echo "Installing pip requirements..."
	pip install -r requirements.txt
	git clone https://github.com/dugsong/libdnet.git
	cd libdnet
	./configure && make
	cd python
	python setup.py install
	cd ../..
	rm -rf libdnet
fi
