#!/bin/bash

rm -r /home/gabriel/worldoftanks
cp -R /home/gabriel/d/projects/worldoftanks/ /home/gabriel/
cd /home/gabriel/worldoftanks

python3 setup.py sdist bdist_wheel
twine check dist/*
python3 -m twine upload --repository testpypi dist/* --verbose