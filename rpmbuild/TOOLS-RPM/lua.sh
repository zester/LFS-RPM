#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
pkgname=lua
pkgver=5.1.5
srcname="../SOURCES/${pkgname}-${pkgver}.tar.gz"
srcdir=${pkgname}-${pkgver}
function unpack() {
	tar xf ${srcname}
}
function clean() {
	rm -rf ${srcdir}
}
function build() {
	patch -p1 -i "../../SOURCES/lua-arch.patch"
	patch -p1 -i "../../SOURCES/lua-5.1-cflags.diff"
	export CFLAGS="$CFLAGS -fPIC"
	make INSTALL_DATA="cp -d" \
		TO_LIB="liblua.a liblua.so liblua.so.5.1" \
		INSTALL_TOP="/tools" \
		INSTALL_MAN="/tools/share/man/man1" \
		linux
	make INSTALL_DATA="cp -d" \
		TO_LIB="liblua.a liblua.so liblua.so.5.1 liblua.so.5.1.5" \
		INSTALL_TOP="/tools" \
		INSTALL_MAN="/tools/share/man/man1" \
		install
	install -D -m644 etc/lua.pc /tools/lib/pkgconfig/lua.pc
}
clean;unpack;pushd ${srcdir};build;popd;clean
