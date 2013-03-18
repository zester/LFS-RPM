#!/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
#
#	Grub
#
ls -alF /final/dev
mount -t proc proc /final/proc || true
mount -t sysfs sys /final/sys || true
mount -o bind /dev /final/dev || true
mount -t devpts pts /final/dev/pts || true
chroot /final /bin/bash -c 'grep -v rootfs /proc/mounts > /etc/mtab'
#grub-install /dev/sdx




