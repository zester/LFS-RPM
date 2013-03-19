#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=gettext
pkgver=0.18.2
srcname="../SOURCES/${pkgname}-${pkgver}.tar.gz"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir}
}

function build() {
	cd gettext-tools
	EMACS="no" ./configure --prefix=/tools --disable-shared
	make -C gnulib-lib
	make -C src msgfmt
	cp -v src/msgfmt /tools/bin
}

clean;unpack;pushd ${srcdir};build;popd;clean

