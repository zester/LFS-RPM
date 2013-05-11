#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
pkgname=zlib
pkgver=1.2.8
srcname="../SOURCES/${pkgname}-${pkgver}.tar.xz"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xf ${srcname}
}
function clean() {
	rm -rf ${srcdir}
}
function build() {
	export PKG_CONFIG_PATH='/tools/lib/pkgconfig'
	CFLAGS="${CFLAGS} -fPIC" ./configure --prefix=/tools
	make
	make -j1 install
}
clean;unpack;pushd ${srcdir};build;popd;clean

