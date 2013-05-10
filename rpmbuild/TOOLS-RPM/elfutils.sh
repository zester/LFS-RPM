#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=elfutils
pkgver=0.155
srcname="../SOURCES/${pkgname}-${pkgver}.tar.bz2"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xf ${srcname}
}
function clean() {
	rm -rf ${srcdir}
}
function build() {
	#CPPFLAGS='-L/tools/lib'
	CFLAGS+=" -g"  # required for test-suite success
	patch -p1 -i ../../SOURCES/elfutils-robustify.patch
	patch -p1 -i ../../SOURCES/elfutils-portability.patch
	export PKG_CONFIG_PATH='/tools/lib/pkgconfig'
	./configure --prefix=/tools --program-prefix="eu-" --with-bzlib=no  --disable-werror #--with-lzma=no
	make 
	make -j1 install
}
clean;unpack;pushd ${srcdir};build;popd;clean
