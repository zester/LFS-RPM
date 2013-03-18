#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=gettext
pkgver=0.18.1.1
srcname="../../SOURCES/${pkgname}-${pkgver}.tar.gz"
srcdir=${pkgname}-${pkgver}
startdir=$(pwd)

function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir}
}

function build() {
	sed -i -e '/gets is a/d' gettext-*/*/stdio.in.h
	cd gettext-tools
	EMACS="no" ./configure --prefix=/tools --disable-shared
	make -C gnulib-lib
	make -C src msgfmt
	cp -v src/msgfmt /tools/bin
}

clean;unpack;pushd ${srcdir};build;popd;clean

