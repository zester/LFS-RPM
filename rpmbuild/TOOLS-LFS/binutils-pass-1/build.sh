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
	../${pkgname}-${pkgver}/configure \
		--prefix=/tools \
		--with-sysroot=$LFS \
		--with-lib-path=/tools/lib \
		--target=$LFS_TGT \
		--disable-nls \
		--disable-werror
	make
	case $(uname -m) in
		x86_64) mkdir -v /tools/lib && ln -sv lib /tools/lib64 ;;
	esac
	make -j1 install
}

clean;unpack;pushd ${srcdir};build;popd;clean

