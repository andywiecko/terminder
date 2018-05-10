#!/bin/bash



TERMINDER_DIR=`pwd`

echo "export TERMINDER_DIR=$TERMINDER_DIR" >> ~/.bashrc
echo "alias terminder='python \$TERMINDER_DIR/terminder.py'" >> ~/.bashrc
echo "terminder" >> ~/.bashrc

echo "pwd='$TERMINDER_DIR/'" >> libs/config.py
