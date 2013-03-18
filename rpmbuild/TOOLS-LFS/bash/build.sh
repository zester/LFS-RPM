#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
pkgname=bash
pkgver=4.2
srcname="../../SOURCES/${pkgname}-${pkgver}.tar.gz"
patchname="../../../SOURCES/${pkgname}-${pkgver}-fixes-8.patch"
srcdir=${pkgname}-${pkgver}
startdir=$(pwd)

function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir}
}

function build() {
	patch -Np1 -i ${patchname}
	./configure --prefix=/tools --without-bash-malloc
	make
	make -j1 install
	ln -vs bash /tools/bin/sh
}

clean;unpack;pushd ${srcdir};build;popd;clean

