#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
pkgname=readline
pkgver=6.2
srcname="../SOURCES/${pkgname}-${pkgver}.tar.gz"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xf ${srcname}
}
function clean() {
	rm -rf ${srcdir}
}
function build() {
	sed -i '/MV.*old/d' Makefile.in
	sed -i '/{OLDSUFF}/c:' support/shlib-install
	patch -Np1 -i ../../SOURCES/$pkgname-$pkgver-fixes-1.patch
	export PKG_CONFIG_PATH='/tools/lib/pkgconfig'	
	./configure \
		--prefix=/tools \
		--libdir=/tools/lib
	make SHLIB_LIBS=-lncurses
	make -j1 install
}
clean;unpack;pushd ${srcdir};build;popd;clean

