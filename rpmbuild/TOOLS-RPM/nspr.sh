#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
pkgname=nspr
pkgver=4.9.6
srcname="../SOURCES/${pkgname}-${pkgver}.tar.gz"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xf ${srcname}
}
function clean() {
	rm -rf ${srcdir} 
}
function build() {
	cd mozilla/nsprpub
	sed -ri 's#^(RELEASE_BINS =).*#\1#' pr/src/misc/Makefile.in
	sed -i 's#$(LIBRARY) ##' config/rules.mk
	export PKG_CONFIG_PATH='/tools/lib/pkgconfig'	
	./configure --prefix=/tools \
		--disable-static \
		--with-mozilla \
		--with-pthreads \
		$([ $(uname -m) = x86_64 ] && echo --enable-64bit)
	make 
	make -j1 install
}
clean;unpack;pushd ${srcdir};build;popd;clean

