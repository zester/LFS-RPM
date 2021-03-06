#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
pkgname=gcc
pkgver=4.8.0
srcname="../SOURCES/${pkgname}-${pkgver}.tar.bz2"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xjf ${srcname}
}

function clean() {
	rm -rf ${srcdir} gcc-build
}

function build() {
	tar -Jxf ../../SOURCES/mpfr-3.1.2.tar.xz
	mv -v mpfr-3.1.2 mpfr
	tar -Jxf ../../SOURCES/gmp-5.1.1.tar.xz
	mv -v gmp-5.1.1 gmp
	tar -zxf ../../SOURCES/mpc-1.0.1.tar.gz
	mv -v mpc-1.0.1 mpc
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
	sed -i '/k prot/agcc_cv_libc_provides_ssp=yes' gcc/configure
	sed -i 's/BUILD_INFO=info/BUILD_INFO=/' gcc/configure
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
		--disable-libatomic \
		--disable-libgomp \
		--disable-libitm \
		--disable-libmudflap \
		--disable-libquadmath \
		--disable-libsanitizer \
		--disable-libssp \
		--disable-libstdc++-v3 \
		--enable-languages=c,c++ \
		--with-mpfr-include=$(pwd)/../${pkgname}-${pkgver}/mpfr/src \
		--with-mpfr-lib=$(pwd)/mpfr/src/.libs
	make
	make -j1 install
	ln -vs libgcc.a `$LFS_TGT-gcc -print-libgcc-file-name | sed 's/libgcc/&_eh/'`
}

clean;unpack;pushd ${srcdir};build;popd;clean
