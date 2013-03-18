#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=make
pkgver=3.82
srcname="../../SOURCES/${pkgname}-${pkgver}.tar.bz2"
srcdir=${pkgname}-${pkgver}
startdir=$(pwd)

function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir}
}

function build() {
	./configure --prefix=/tools
	make
	make -j1 install
}

clean;unpack;pushd ${srcdir};build;popd;clean
