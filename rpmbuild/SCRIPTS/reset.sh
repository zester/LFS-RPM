#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h			# disable hashall
SCRIPTS/umount.kernel.filesystem.sh
export LFS=/mnt/lfs
list="bin boot dev etc home lib media mnt opt proc root run sbin srv sys tmp usr var"
for i in $list; do
	rm -rf ${LFS}/${i}
done
find ${LFS} -name '*.log'	-delete
find ${LFS} -name '*~'		-delete
find ${LFS} -name '*.rpm'	-delete
find ${LFS} -name '*.done'	-delete
rm -rf ${LFS}/tools/*
install -vdm 777 ${LFS}/tools
ln -svf ${LFS}/tools /
