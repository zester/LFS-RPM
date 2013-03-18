#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=glibc
pkgver=2.16.0
srcname=../../SOURCES/${pkgname}-${pkgver}.tar.xz
srcdir=${pkgname}-${pkgver}
startdir=$(pwd)

function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir} glibc-build
}

function build() {
	if [ ! -r /usr/include/rpc/types.h ]; then
		su -c 'mkdir -p /usr/include/rpc'
		su -c 'cp -v sunrpc/rpc/*.h /usr/include/rpc'
	fi
	sed -i 's/ -lgcc_s//' Makeconfig
	mkdir -v ../glibc-build
	cd ../glibc-build
	../${pkgname}-${pkgver}/configure \
		--prefix=/tools \
		--host=$LFS_TGT \
		--build=$(../glibc-2.16.0/scripts/config.guess) \
		--disable-profile \
		--enable-add-ons \
		--enable-kernel=2.6.25 \
		--with-headers=/tools/include \
		libc_cv_forced_unwind=yes \
		libc_cv_ctors_header=yes \
		libc_cv_c_cleanup=yes
	make
	make -j1 install
	echo 'main(){}' > dummy.c
	$LFS_TGT-gcc dummy.c
	readelf -l a.out | grep ': /tools' |& tee ${startdir}/test.log
	rm -v dummy.c a.out
}
clean;unpack;pushd ${srcdir};build;popd;clean

