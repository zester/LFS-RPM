#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=perl
pkgver=5.16.3
srcname="../SOURCES/${pkgname}-${pkgver}.tar.bz2"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir}
}

function build() {
	patch -Np1 -i ../../SOURCES/${pkgname}-${pkgver}-libc-1.patch
	sh Configure -des -Dprefix=/tools
	make
	cp -v perl cpan/podlators/pod2man /tools/bin
	mkdir -pv /tools/lib/${pkgname}5/${pkgver}
	cp -Rv lib/* /tools/lib/${pkgname}5/${pkgver}
}

clean;unpack;pushd ${srcdir};build;popd;clean
