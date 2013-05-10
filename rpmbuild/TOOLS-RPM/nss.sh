#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
pkgname=nss
pkgver=3.14.3
srcname="../SOURCES/${pkgname}-${pkgver}.tar.gz"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xf ${srcname}
}
function clean() {
	rm -rf ${srcdir}
}
function build() {
	export PKG_CONFIG_PATH='/tools/lib/pkgconfig'
	patch -Np1 -i ../../SOURCES/nss-3.14.3-standalone-1.patch
	cd mozilla/security/nss
	make -j1 nss_build_all BUILD_OPT=1 \
	NSPR_INCLUDE_DIR=/tools/include/nspr \
	$([ $(uname -m) = x86_64 ] && echo USE_64=1)
	cd ../../dist
	install -vdm 755 /tools/bin
	install -vdm 755 /tools/lib/pkgconfig
	install -vdm 755 /tools/include
	install -v -m755 Linux*/lib/*.so /tools/lib
	install -v -m644 Linux*/lib/{*.chk,libcrmf.a} /tools/lib
	install -v -m755 -d /tools/include
	cp -v -RL {public,private}/nss/* /tools/include
	install -v -m755 Linux*/bin/{certutil,nss-config,pk12util} /tools/bin
	install -v -m644 Linux*/lib/pkgconfig/nss.pc /tools/lib/pkgconfig
	sed -i 's|usr|tools|' /tools/lib/pkgconfig/nss.pc
}
clean;unpack;pushd ${srcdir};build;popd;clean
