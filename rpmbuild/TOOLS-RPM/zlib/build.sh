#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
pkgname=zlib
pkgver=1.2.7
srcname="../../SOURCES/${pkgname}-${pkgver}.tar.bz2"
srcdir=${pkgname}-${pkgver}
function unpack() {
	tar xf ${srcname}
}
function clean() {
	rm -rf ${srcdir}
}
function build() {
	CFLAGS="${CFLAGS} -fPIC" ./configure --prefix=/tools
	make
	make -j1 install
}
clean;unpack;pushd ${srcdir};build;popd;clean

