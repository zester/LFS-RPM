#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=expect
pkgver=5.45
srcname="../SOURCES/${pkgname}${pkgver}.tar.gz"
srcdir=${pkgname}${pkgver}

function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir}
}

function build() {
	cp -v configure{,.orig}
	sed 's:/usr/local/bin:/bin:' configure.orig > configure
	./configure --prefix=/tools \
		--with-tcl=/tools/lib \
		--with-tclinclude=/tools/include
	make
	make -j1  SCRIPTS="" install
}

clean;unpack;pushd ${srcdir};build;popd;clean

