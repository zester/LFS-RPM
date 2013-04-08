#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
#	These environmnet variables are from the lfs user environment
umask 022
LC_ALL=POSIX
LFS_TGT=$(uname -m)-lfs-linux-gnu
PATH=/tools/bin:/bin:/usr/bin
export LFS LC_ALL LFS_TGT PATH
#	These are the build environment flags for the tool chain
MAKEFLAGS="-j4"
case $(uname -m) in
	i686)
		CFLAGS="-march=i486 -mtune=i686 -O2 -pipe"
		CXXFLAGS="-march=i486 -mtune=i686 -O2 -pipe"
	;;
	x86_64)
		CFLAGS="-march=x86-64 -mtune=generic -O2 -pipe"
		CXXFLAGS="-march=x86-64 -mtune=generic -O2 -pipe"
	;;
	native)
		CFLAGS="-march=native -mtune=native -O2 -pipe"
		CXXFLAGS="-march=native -mtune=native -O2 -pipe"
	;;
	*)
		printf "%s" "ERROR: CARCH not set!\n"
		printf "%s" "Can not continue exitting\n"
		touch FAILURE;exit 1
	;;
esac
LDFLAGS="-Wl,-O1,--sort-common,--as-needed,-z,relro"
export CARCH MAKEFLAGS CFLAGS CXXFLAGS LDFLAGS
#	Customizable environment variables
export FAILURE="$(pwd)/FAILURE"
#	Commence with the bombardment
#	Build the tool chain Chapter 5
[ -f ${FAILURE} ] && (printf "FAILURE detected exiting script \n";exit 1)
printf "Building Tool chain \n"
pushd TOOLS-LFS > /dev/null 2>&1;./builder.sh;popd > /dev/null 2>&1
#	Build the rpm package manager tool chain
[ -f ${FAILURE} ] && (printf "FAILURE detected exiting script \n";exit 1)
printf "Building Tool chain package manager\n"
pushd TOOLS-RPM > /dev/null 2>&1;./builder.sh;popd > /dev/null 2>&1
printf "Build tool chain package manager completed \n"
#	If the symlink for bash is not found then the root filesystem hasn't been installed
[ -f ${FAILURE} ] && (printf "FAILURE detected exiting script \n";exit 1)
printf "Building filesystem \n"
pushd SCRIPTS > /dev/null;./filesystem.sh;popd > /dev/null
printf "Build filesystem completed \n"
#	Mount the kernel filesystems for the chroot
su -c 'SCRIPTS/mount.kernel.filesystem.sh'
#Build the base system Chapter 6
printf "Building base system \n"
su -c 'chroot "$LFS" /tools/bin/env -i \
	HOME=/root TERM="$TERM" PS1="\u:\w\$ " \
	PATH=/bin:/usr/bin:/sbin:/usr/sbin:/tools/bin \
	/tools/bin/bash --login +h -c "pushd /rpmbuild/SPECS>/dev/null;./builder.sh;popd>/dev/null" ' root
#	Configure the newly installed LFS system
[ -f ${FAILURE} ] && (printf "FAILURE detected exiting script \n";exit 1)
printf "Configuring finished system \n"
su -c 'chroot "$LFS" /usr/bin/env -i \
	HOME=/root TERM="$TERM" PS1="\u:\w\$ " \
	PATH=/bin:/usr/bin:/sbin:/usr/sbin \
	/bin/bash --login -c /rpmbuild/SCRIPTS/configuration.sh' root
#	Unmount the kernel filesystems for the chroot
su -c 'SCRIPTS/umount.kernel.filesystem.sh' root
