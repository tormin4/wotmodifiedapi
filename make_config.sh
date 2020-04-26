#!/bin/bash

live_user=$1
live_pass=$2
test_user=$3
test_pass=$4

echo "[distutils]" >> ~/.pypirc
echo "index-servers=" >> ~/.pypirc
echo "  pypi" >> ~/.pypirc
echo "  testpypi" >> ~/.pypirc
echo "" >> ~/.pypirc
echo "[pypi]" >> ~/.pypirc
echo "username="$1 >> ~/.pypirc
echo "password="$2 >> ~/.pypirc
echo "" >> ~/.pypirc
echo "[testpypi]" >> ~/.pypirc
echo "repository=https://test.pypi.org/legacy/" >> ~/.pypirc
echo "username="$3 >> ~/.pypirc
echo "password="$4 >> ~/.pypirc