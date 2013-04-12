#!/bin/bash
set -o errexit
set -o nounset
set +h
LFS=/mnt/lfs

install -vdm 777 ${LFS}
install -vdm 777 ${LFS}/tools
pushd /;ln -vfs ${LFS}/tools;popd
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
	#install -vdm 777 rpmbuild/TOOLS-LFS/{DONE,LOGS}
	#install -vdm 777 rpmbuild/TOOLS-RPM/{DONE,LOGS}
	#install -vdm 777 rpmbuild/SPECS/LOGS
	#install -vdm 777 rpmbuild/{BUILD,BUILDROOT,RPMS}
	chown -R lfs.lfs rpmbuild/TOOLS-RPM
	chown -R lfs.lfs rpmbuild/TOOLS-LFS
	find . -name '*.sh' -exec chmod +x '{}' \;
	
popd
printf "Setup completed\n"


