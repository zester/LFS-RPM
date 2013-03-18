#!/bin/bash
#set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail

export LFS=/mnt/lfs
if  mountpoint $LFS/sys	>/dev/null; then
	umount -v $LFS/sys
fi
if mountpoint $LFS/proc	>/dev/null; then
	umount -v $LFS/proc
fi
if mountpoint $LFS/dev/shm >/dev/null; then
	umount -v $LFS/dev/shm
fi
if mountpoint $LFS/dev/pts >/dev/null; then
	umount -v $LFS/dev/pts
fi

if mountpoint $LFS/dev >/dev/null; then
	umount -v $LFS/dev
fi
echo "Kernel filesystems are umounted"