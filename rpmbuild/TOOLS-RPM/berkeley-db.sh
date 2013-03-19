#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
pkgname=berkeley-db
_pkgname=db
pkgver=5.3.21
srcname="../SOURCES/${_pkgname}-${pkgver}.tar.gz"
srcdir=${_pkgname}-${pkgver}

function unpack() {
	tar xf ${srcname}
}
function clean() {
	rm -rf ${srcdir}
}
function build() {
	cd build_unix
	../dist/configure \
		--prefix=/tools \
		--enable-compat185 \
		--enable-dbm \
		--disable-static \
		--enable-cxx \
		--with-posixmutexes
	make
	make -j1 install
}
clean;unpack;pushd ${srcdir};build;popd;clean
