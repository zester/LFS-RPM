#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=tcl
pkgver=8.5.12
srcname="../../SOURCES/${pkgname}${pkgver}-src.tar.gz"
srcdir=${pkgname}${pkgver}
startdir=$(pwd)

function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir}
}

function build() {
	cd unix
	./configure --prefix=/tools
	make
	make -j1 install
	chmod -v u+w /tools/lib/libtcl8.5.so
	make -j1 install-private-headers
	ln -sv tclsh8.5 /tools/bin/tclsh
}

clean;unpack;pushd ${srcdir};build;popd;clean
