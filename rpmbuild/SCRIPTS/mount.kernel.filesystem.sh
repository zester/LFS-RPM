#!/tools/bin/bash
#set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail

export LFS=/mnt/lfs
if ! mountpoint $LFS/dev >/dev/null; then
	mount -v --bind /dev "$LFS/dev"
fi
if ! mountpoint $LFS/dev/pts >/dev/null; then
	mount -vt devpts devpts "$LFS/dev/pts"
fi
if [ -h /dev/shm ]; then
   rm -f $LFS/dev/shm
   mkdir $LFS/dev/shm
fi
if ! mountpoint $LFS/dev/shm >/dev/null; then
	mount -vt tmpfs shm "$LFS/dev/shm"
fi
if ! mountpoint $LFS/proc	>/dev/null; then
	mount -vt proc proc "$LFS/proc"
fi
if ! mountpoint $LFS/sys	>/dev/null; then
	mount -vt sysfs sysfs "$LFS/sys"
fi
echo "Kernel filesystems are mounted"