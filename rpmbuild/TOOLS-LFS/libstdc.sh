#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=gcc
pkgver=4.8.0
srcname="../SOURCES/${pkgname}-${pkgver}.tar.bz2"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir} gcc-build
}

function build() {
	mkdir -v ../gcc-build
	cd ../gcc-build
	../${pkgname}-${pkgver}/libstdc++-v3/configure \
	--host=$LFS_TGT \
	--prefix=/tools \
	--disable-multilib \
	--disable-shared \
	--disable-nls \
	--disable-libstdcxx-threads \
	--disable-libstdcxx-pch \
	--with-gxx-include-dir=/tools/$LFS_TGT/include/c++/4.8.0
	make
	make -j1 install
}
clean;unpack;pushd ${srcdir};build;popd;clean
