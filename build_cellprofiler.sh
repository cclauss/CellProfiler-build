#!/bin/bash
#
# This script will be run as the cpbuild user inside the virtual build
# machine. It is started from the Fabric script fabfile.py.

# Stop at first error.
set -e
# Print each command before executing it.
set -x

function makeall {
    export GITHOME=/usr/CellProfiler/src/CellProfiler
    export JAVA_HOME=$GITHOME/jdk1.7.0_21
    export LD_LIBRARY_PATH=$JAVA_HOME/jre/lib/amd64/server:/usr/CellProfiler/lib/
    export PATH=/usr/CellProfiler/bin:$PATH
    export HOSTTYPE=amd64
    export BLAS=/usr/lib64
    export LAPACK=/usr/lib64
    cd $GITHOME
    make -f Makefile.CP2.standard.64 all || true
    /usr/CellProfiler/bin/python -m easy_install pyzmq
    make -f Makefile.CP2.standard.64 all
}
function downloadjava {
    url='http://cellprofiler.org/linked_files/CPPackageHost/'
    javajdk='jdk-7u21-linux-x64.tar.gz'
    javajre='jre-7u21-linux-x64.tar.gz'
    javajdkrpm='jdk-7u21-linux-x64.rpm'
    javajrerpm='jre-7u21-linux-x64.rpm'
    cd /usr/CellProfiler/src/CellProfiler
    wget $url/$javajdk
}

function installjava {
    cd /usr/CellProfiler/src/CellProfiler
    tar xf jdk-7u21-linux-x64.tar.gz
    cd jdk1.7.0_21
    unzip -q -o src.zip
}

function tarup {
    cd $HOME
    tar cvzf cellprofiler.tar.gz --exclude=/usr/CellProfiler/src /usr/CellProfiler
}

function clean {
    cd /usr/CellProfiler/src/CellProfiler
    rm ./*.tar.gz
    rm ./*.tar.bz2
}

echo This is inside "$0"

# Install dependencies as RPM packages. These are the build dependencies;
# not all of them are required to run the finished software.
sudo yum -q -y install python-setuptools gcc gcc-c++ wget vim gtk2-devel git svn gcc-gfortran cmake mesa-libGL mesa-libGL-devel blas atlas lapack blas-devel atlas-devel lapack-devel xorg-x11-xauth* xorg-x11-xkb-utils* unzip dejavu-lgc-sans-fonts qt-devel openssl openssl-devel xclock bzip2 bzip2-devel bzip2-libs libXtst make

# Create directories.
sudo mkdir /usr/CellProfiler
sudo chown cpbuild:cpbuild /usr/CellProfiler
mkdir /usr/CellProfiler/src
mkdir /usr/CellProfiler/src/CellProfiler

# Get the source code for CellProfiler.
git clone https://github.com/CellProfiler/CellProfiler.git /usr/CellProfiler/src/CellProfiler

downloadjava
installjava
makeall
clean
tarup
