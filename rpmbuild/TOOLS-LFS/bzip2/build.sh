#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=bzip2
pkgver=1.0.6
srcname="../../SOURCES/${pkgname}-${pkgver}.tar.gz"
srcdir=${pkgname}-${pkgver}
startdir=$(pwd)
export CFLAGS="${CFLAGS} -fPIC"
function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir}
}

function build() {
	make -f Makefile-libbz2_so
	make bzip2 bzip2recover libbz2.a
	make
	make -j1 PREFIX=/tools install
	install -m755 libbz2.so.1.0.6 /tools/lib
	ln -s libbz2.so.1.0.6 /tools/lib/libbz2.so
	ln -s libbz2.so.1.0.6 /tools/lib/libbz2.so.1
	ln -s libbz2.so.1.0.6 /tools/lib/libbz2.so.1.0
}

clean;unpack;pushd ${srcdir};build;popd;clean

