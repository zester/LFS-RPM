#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=patch
pkgver=2.7.1
srcname="../SOURCES/${pkgname}-${pkgver}.tar.xz"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir}
}

function build() {
	./configure \
		--prefix=/tools
	make
	make -j1 install
}

clean;unpack;pushd ${srcdir};build;popd;clean

