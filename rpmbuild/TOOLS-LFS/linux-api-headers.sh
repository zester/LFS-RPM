#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=linux
pkgver=3.8.1
srcname="../SOURCES/${pkgname}-${pkgver}.tar.xz"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir}
}

function build() {
	make -j1 mrproper
	make -j1 headers_check
	make -j1 INSTALL_HDR_PATH=dest headers_install
	cp -rv dest/include/* /tools/include
}

unpack;pushd ${srcdir};build;popd;clean
