#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
pkgname=popt
pkgver=1.16
srcname="../../SOURCES/${pkgname}-${pkgver}.tar.gz"
srcdir="${pkgname}-${pkgver}"
pkgdir=$(pwd)/pkg
function unpack() {
	tar xf ${srcname}
}
function clean() {
	rm -rf ${srcdir}
}
function build() {
	./configure --prefix=/tools --disable-static
	make
	make -j1 install
}
clean;unpack;pushd ${srcdir};build;popd;clean

