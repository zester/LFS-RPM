#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=elfutils
pkgver=0.154
srcname="../SOURCES/${pkgname}-${pkgver}.tar.bz2"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xf ${srcname}
}
function clean() {
	rm -rf ${srcdir}
}
function build() {
	CFLAGS+=" -g"  # required for test-suite success
	patch -p1 -i "../../SOURCES/elfutils-0.154-binutils-pr-ld-13621.patch"
	./configure --prefix=/tools --program-prefix="eu-"
	make -j2
	make -j1 install
}
clean;unpack;pushd ${srcdir};build;popd;clean
