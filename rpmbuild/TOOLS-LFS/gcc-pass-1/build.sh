#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=gcc
pkgver=4.7.1
srcname="../../SOURCES/${pkgname}-${pkgver}.tar.bz2"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xjf ${srcname}
}

function clean() {
	rm -rf ${srcdir} gcc-build
}

function build() {
	tar -Jxf ../../../SOURCES/mpfr-3.1.1.tar.xz
	mv -v mpfr-3.1.1 mpfr
	tar -Jxf ../../../SOURCES/gmp-5.0.5.tar.xz
	mv -v gmp-5.0.5 gmp
	tar -zxf ../../../SOURCES/mpc-1.0.tar.gz
	mv -v mpc-1.0 mpc
#	patch -Np1 -i ../../../SOURCES/${pkgname}-${pkgver}-gengtype.patch
	for file in $(find gcc/config -name linux64.h -o -name linux.h -o -name sysv4.h)
	do
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
	sed -i '/k prot/agcc_cv_libc_provides_ssp=yes' gcc/configure
	mkdir -v ../gcc-build
	cd ../gcc-build
	../${pkgname}-${pkgver}/configure \
		--target=$LFS_TGT \
		--prefix=/tools \
		--with-sysroot=$LFS \
		--with-newlib \
		--without-headers \
		--with-local-prefix=/tools \
		--with-native-system-header-dir=/tools/include \
		--disable-nls \
		--disable-shared \
		--disable-multilib \
		--disable-decimal-float \
		--disable-threads \
		--disable-libmudflap \
		--disable-libssp \
		--disable-libgomp \
		--disable-libquadmath \
		--enable-languages=c \
		--with-mpfr-include=$(pwd)/../gcc-4.7.1/mpfr/src \
		--with-mpfr-lib=$(pwd)/mpfr/src/.libs
	make
	make -j1 install
	ln -vs libgcc.a `$LFS_TGT-gcc -print-libgcc-file-name | sed 's/libgcc/&_eh/'`
}

clean;unpack;pushd ${srcdir};build;popd;clean
