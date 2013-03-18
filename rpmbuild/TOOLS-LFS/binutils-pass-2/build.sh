#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
pkgname=binutils
pkgver=2.22
srcname=../../SOURCES/${pkgname}-${pkgver}.tar.bz2
patchname="../../../SOURCES/${pkgname}-${pkgver}-build_fix-1.patch"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir} binutils-build
}

function build() {
	patch -Np1 -i ${patchname}
	mkdir -v ../binutils-build
	cd ../binutils-build
	CC=$LFS_TGT-gcc \
	AR=$LFS_TGT-ar \
	RANLIB=$LFS_TGT-ranlib \
	../binutils-2.22/configure \
		--prefix=/tools \
		--disable-nls \
		--with-lib-path=/tools/lib
	make
	make -j1 install
	make -C ld clean
	make -C ld LIB_PATH=/usr/lib:/lib
	cp -v ld/ld-new /tools/bin
}

clean;unpack;pushd ${srcdir};build;popd;clean

