#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
pkgname=bash
pkgver=4.2
srcname="../SOURCES/${pkgname}-${pkgver}.tar.gz"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir}
}

function build() {
	patch -Np1 -i ../../SOURCES/${pkgname}-${pkgver}-fixes-11.patch
	./configure \
		--prefix=/tools \
		--without-bash-malloc
	make
	make -j1 install
	ln -vs bash /tools/bin/sh
}

clean;unpack;pushd ${srcdir};build;popd;clean

