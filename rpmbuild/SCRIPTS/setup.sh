#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h			# disable hashall
LFS=/mnt/lfs
PARTITION=/dev/sda4
SOURCE=/media/rpmbuild
#yum install patch gcc bison
install -vdm 777 ${LFS}
mount ${PARTITION} ${LFS}
[ -e /mnt/lfs/tools ] || install -vdm 777 /mnt/lfs/tools
ln -vfs /mnt/lfs/tools /
chmod -R 777 ${LFS}
cp -var ${SOURCE} ${LFS}
/mnt/lfs/rpmbuild/SCRIPTS/add.user.lfs.sh
su - lfs
