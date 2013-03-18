#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=diffutils
pkgver=3.2
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
	sed -i -e '/gets is a/d' lib/stdio.in.h
	./configure --prefix=/tools
	make
	make -j1 install
}

clean;unpack;pushd ${srcdir};build;popd;clean

