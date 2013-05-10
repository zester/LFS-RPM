#!/bin/bash
set -o errexit
set -o nounset
set +h
LFS=/mnt/lfs
PART=/dev/sdxx
fsck.ext4 ${PART}
install -vdm 777 ${LFS}
mount ${PART} ${LFS}
install -vdm 777 ${LFS}/tools
pushd /;ln -vs ${LFS}/tools;popd
pushd ${LFS}
	[ -d LFS-RPM ] || git clone git://github.com/baho-utot/LFS-RPM.git
	[ -d rpmbuild ] || ln -vfs LFS-RPM/rpmbuild
	rpmbuild/SCRIPTS/add.user.lfs.sh
	pushd rpmbuild/SOURCES
		wget -nc -i wget-list
		wget -nc -i wget-list.rpm
		md5sum -c md5sums || true
		md5sum -c md5sums.rpm || true
	popd
	chown -R lfs.lfs ${LFS}
	find . -name '*.sh' -exec chmod +x '{}' \;
	
popd
printf "Setup completed\n"
