#!/bin/bash
##############################################
# Installing Geant4 and other necessary packages
# locally. This script will install dependencies
# into home directory and set the environment
# variables
##############################################


cd depedencies/Geant4

sudo chmod +x geant4.10.06-install.sh
./geant4.10.06-install.sh

cd ../Python

sudo chmod +x python3.7_local_install.sh
./python3.7_local_install.sh

cd ../../build

source ~/.bashrc

cmake ..

make -j8

echo 'Installation has been completed successfully..!!'
