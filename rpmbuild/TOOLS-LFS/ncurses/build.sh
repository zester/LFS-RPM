#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=ncurses
pkgver=5.9
srcname="../../SOURCES/${pkgname}-${pkgver}.tar.gz"
srcdir=${pkgname}-${pkgver}
startdir=$(pwd)

function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir}
}

function build() {
	./configure --prefix=/tools --with-shared --without-debug --without-ada --enable-overwrite
	make
	make -j1 install
}

clean;unpack;pushd ${srcdir};build;popd;clean

