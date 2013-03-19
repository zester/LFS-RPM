#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=bzip2
pkgver=1.0.6
srcname="../SOURCES/${pkgname}-${pkgver}.tar.gz"
srcdir=${pkgname}-${pkgver}

export CFLAGS="${CFLAGS} -fPIC"
function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir}
}

function build() {
	make
	make -j1 PREFIX=/tools install
}

clean;unpack;pushd ${srcdir};build;popd;clean

