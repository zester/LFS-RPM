#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
pkgname=rpm
#pkgver=4.10.3.1
pkgver=4.11.0.1
srcname="../SOURCES/${pkgname}-${pkgver}.tar.bz2"
srcdir=${pkgname}-${pkgver}

function unpack() {
	tar xf ${srcname}
}
function clean() {
	rm -rf ${srcdir} 
}
function build() {
	export LIBS=-'L/tools/lib'
	export CPPFLAGS='-I/tools/include/nspr'
	./autogen.sh --noconfigure
	./configure \
		--prefix=/tools \
		--disable-static \
		--with-external-db
	make
	make -j1 install
	sed -i 's|optflags: i386 -O2 -g -march=i386 -mtune=i686|optflags: i386 -O2 -march=i486 -mtune=i686 -pipe|'	/tools/lib/rpm/rpmrc
	sed -i 's|optflags: i486 -O2 -g -march=i486|optflags: i486 -O2 -march=i486 -mtune=generic -pipe|'		/tools/lib/rpm/rpmrc
	sed -i 's|optflags: i586 -O2 -g -march=i586|optflags: i586 -O2 -march=i586 -mtune=generic -pipe|'		/tools/lib/rpm/rpmrc
	sed -i 's|optflags: i686 -O2 -g -march=i686|optflags: i686 -O2 -march=i486 -mtune=i686 -pipe|'			/tools/lib/rpm/rpmrc
	sed -i 's|optflags: athlon -O2 -g -march=athlon|optflags: athlon -O2 -march=athlon -mtune=generic -pipe|'	/tools/lib/rpm/rpmrc
	sed -i 's|\${prefix}||'		/tools/lib/rpm/macros
	sed -i 's|%{getenv:HOME}||'	/tools/lib/rpm/macros
}
clean;unpack;pushd ${srcdir};build;popd;clean

