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
trap 'echo Base build failed...;touch ${FAILURE};exit 1' ERR
_list="filesystem linux-api-headers man-pages glibc tzdata adjust-tool-chain zlib file binutils gmp mpfr mpc gcc sed bzip2 pkg-config ncurses util-linux psmisc e2fsprogs shadow coreutils iana-etc m4 bison procps grep readline bash libtool gdbm inetutils perl autoconf automake diffutils gawk findutils flex gettext groff xz grub less gzip iproute2 kbd kmod libpipeline make man-db patch sysklogd sysvinit tar texinfo udev vim bootscripts linux db elfutils lua nspr nss popt rpm"
for i in ${_list}; do
	[ -f ${FAILURE} ] && (printf "Base: Error exiting script \n";exit 1)
	RPM=""
	case ${i} in
		adjust-tool-chain)
			./adjust-tool-chain.sh	;;
		linux)
			RPM=$( find ../RPMS -name "${i}-[0-9]*.rpm" )
			if [ -z $RPM ]; then
				rm -rf ../BUILD/*
				rpmbuild -ba --target ${build} --nocheck ${i}.spec |& tee ${i}.log
				RPM=$(find ../RPMS -name "${i}-[0-9]*.rpm" )
				if [ -z $RPM ]; then
					printf "RPM package ${i} not found\n";exit 1
				else
					rpm -Uvh --nodeps $RPM
				fi
			else
				printf "RPM package ${i} already built\n"
			fi
		;;
		*)
			RPM=$(find ../RPMS -name "${i}-[0-9]*.rpm" )
			if [ -z $RPM ]; then
				rm -rf ../BUILD/*
				rpmbuild -ba --target ${build} --nocheck ${i}.spec |& tee ${i}.log
				RPM=$(find ../RPMS -name "${i}-[0-9]*.rpm" -print)
				if [ -z $RPM ]; then
					printf "RPM package ${i} not found\n";exit 1
				else
					rpm -Uvh --nodeps $RPM
				fi
			else
				printf "RPM package ${i} already built\n"
			fi
		;;
	esac
done
