#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=gcc
pkgver=4.7.2
srcname="../SOURCES/${pkgname}-${pkgver}.tar.bz2"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xf ${srcname}
}

function clean() {
	rm -rf ${srcdir} gcc-build
}

function build() {
	cat gcc/limitx.h gcc/glimits.h gcc/limity.h > \
		`dirname $($LFS_TGT-gcc -print-libgcc-file-name)`/include-fixed/limits.h
	cp -v gcc/Makefile.in{,.tmp}
	sed 's/^T_CFLAGS =$/& -fomit-frame-pointer/' gcc/Makefile.in.tmp > gcc/Makefile.in
	for file in $(find gcc/config -name linux64.h -o -name linux.h -o -name sysv4.h); do
		cp -uv $file{,.orig}
		sed -e 's@/lib\(64\)\?\(32\)\?/ld@/tools&@g' \
		    -e 's@/usr@/tools@g' $file.orig > $file
echo '
#undef STANDARD_STARTFILE_PREFIX_1
#undef STANDARD_STARTFILE_PREFIX_2
#define STANDARD_STARTFILE_PREFIX_1 "/tools/lib/"
#define STANDARD_STARTFILE_PREFIX_2 ""' >> $file
		touch $file.orig
	done
	tar -Jxf ../../SOURCES/mpfr-3.1.1.tar.xz
	mv -v mpfr-3.1.1 mpfr
	tar -Jxf ../../SOURCES/gmp-5.1.1.tar.xz
	mv -v gmp-5.1.1 gmp
	tar -zxf ../../SOURCES/mpc-1.0.1.tar.gz
	mv -v mpc-1.0.1 mpc	
	sed -i 's/BUILD_INFO=info/BUILD_INFO=/' gcc/configure	
	mkdir -v ../gcc-build
	cd ../gcc-build
	CC=$LFS_TGT-gcc \
	AR=$LFS_TGT-ar \
	RANLIB=$LFS_TGT-ranlib \
	../${pkgname}-${pkgver}/configure \
		--prefix=/tools \
		--with-local-prefix=/tools \
		--with-native-system-header-dir=/tools/include \
		--enable-clocale=gnu \
		--enable-shared \
		--enable-threads=posix \
		--enable-__cxa_atexit \
		--enable-languages=c,c++ \
		--disable-libstdcxx-pch \
		--disable-multilib \
		--disable-bootstrap \
		--disable-libgomp \
		--with-mpfr-include=$(pwd)/../${pkgname}-${pkgver}/mpfr/src \
		--with-mpfr-lib=$(pwd)/mpfr/src/.libs
	make
	make -j1 install
	ln -vs gcc /tools/bin/cc
	echo 'main(){}' > dummy.c
	cc dummy.c
	readelf -l a.out | grep ': /tools' |& tee ../${pkgname}-${pkgver}-pass-2-test.log
	rm -v dummy.c a.out
}
clean;unpack;pushd ${srcdir};build;popd;clean
