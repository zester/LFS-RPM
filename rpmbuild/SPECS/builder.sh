#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
export FAILURE="/rpmbuild/FAILURE"
#	set correct file ownership
chown root.root -R ../SOURCES
chown root.root -R ../SPECS
build=$(uname -m)
list="filesystem linux-api-headers man-pages glibc tzdata adjust-tool-chain zlib file binutils gmp mpfr mpc gcc sed bzip2 pkg-config ncurses util-linux psmisc e2fsprogs shadow coreutils iana-etc m4 bison procps-ng grep readline bash libtool gdbm inetutils perl autoconf automake diffutils gawk findutils flex gettext groff xz grub less gzip iproute2 kbd kmod libpipeline make man-db patch sysklogd sysvinit tar texinfo udev vim bootscripts linux db elfutils nspr nss popt rpm" 
# lua"
 
die() {
	local msg=$1
	printf "Base build failed: ${msg}\n"
	touch ${FAILURE}
	exit 1
}
findpkg() {
	local pkg=$1
	RPM=$(find ../RPMS -name "${pkg}-[0-9]*.rpm" -print)
}
buildpkg() {
	local pkg=$1
	rm -rf ../BUILD/*
	rpmbuild -ba --target ${build} --nocheck ${pkg}.spec |& tee LOGS/${pkg} || die "buildpkg: ${pkg}: rpmbuild failure"
	rm -rf ../BUILD/* ../BUILDROOT/* > /dev/null 2>&1
}
installpkg() {
	# --noscripts - add to rpm to disable %post scripts
	local pkg=$1
	findpkg ${pkg}
	printf "installpkg: $RPM\n"
	[ -z $RPM ] && die "installation error: rpm package not found\n"
	case ${pkg} in
		glibc)	rpm -Uvh --nodeps ${RPM} || die "installation error: ${pkg} rpm barfed\n" ;;
		    *)	rpm -Uvh --nodeps ${RPM} || die "installation error: ${pkg} rpm barfed\n" ;;
	esac
}
for i in ${list}; do
	[ -f ${FAILURE} ] && die "FAILURE: ${i}: detected exiting script\n"
	RPM=""
	case ${i} in
		adjust-tool-chain) ./adjust-tool-chain.sh || die "Toolchain adjustment error";;
		*)
			findpkg ${i}
			[ -z $RPM ] && printf "Building --> ${i}\n" || printf "Skipping --> ${i}\n"
			[ -z $RPM ] && buildpkg ${i} || continue
			installpkg ${i}
		;;
	esac
done
rm -rf ../BUILD/*
