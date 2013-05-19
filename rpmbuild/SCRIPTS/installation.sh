set -o errexit	# exit if error
#set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail

DEVICE=/dev/sda6
PARTITION=/mnt/installation

die() {
	local msg=$1
	printf "Installation failed: ${msg}\n"
	exit 1
}
mnt_kernel_filesystem () {
if ! mountpoint ${PARTITION}/dev >/dev/null; then
	mount -v --bind /dev "${PARTITION}"
fi
if ! mountpoint ${PARTITION}/dev/pts >/dev/null; then
	mount -vt devpts devpts "${PARTITION}/dev/pts"
fi
if [ -h /dev/shm ]; then
   rm -f ${PARTITION}/dev/shm
   mkdir ${PARTITION}/dev/shm
fi
if ! mountpoint ${PARTITION}/dev/shm >/dev/null; then
	mount -vt tmpfs shm "${PARTITION}/dev/shm"
fi
if ! mountpoint ${PARTITION}/proc	>/dev/null; then
	mount -vt proc proc "${PARTITION}/proc"
fi
if ! mountpoint ${PARTITION}/sys	>/dev/null; then
	mount -vt sysfs sysfs "${PARTITION}/sys"
fi
}
#	Mount partition
[ -d ${PARTITION} ] || install -vdm 777 ${PARTITION}
mount ${DEVICE} ${PARTITION} || die "Can not mount PARTITION\n"
mnt_kernel_filesystem || die "Can not mount kernel filesystems\n"
#	Install base packages
rpm --initdb --dbpath ${PARTITION}/var/lib/rpm
rpm -Uvh --nodeps --noscripts --root ${PARTITION} RPMS/noarch/* RPMS/i686/*
#	Create device nodes
/bin/mknod -m 600 ${PARTITION}/dev/console c 5 1
/bin/mknod -m 666 ${PARTITION}/dev/null c 1 3
#	Configuration
LIST=(/etc/sysconfig/clock /etc/sysconfig/console /etc/profile /etc/sysconfig/network /etc/hosts /etc/fstab /etc/sysconfig/ifconfig.eth0 /etc/resolv.conf /etc/passwd /etc/lsb-release /etc/sysconfig/rc.site)
for i in ${LIST[@]}; do
	vim "${PARTITION}/${i}"
done
#	create script and complete installation
cat > ${PARTITION}/finish.sh <<- "EOF"
#	create here doc and exec chroot bash -c here.doc
	#	install locale files
	printf "%s\n" "Creating locale files"
	/sbin/locale-gen.sh
	#	install ld cache
	/sbin/ldconfig -v
	#	enable shadowed passwords and group passwords
	/usr/sbin/pwconv
	/usr/sbin/grpconv
	#	udev script
	source	/lib/udev/init-net-rules.sh
	/sbin/udevadm hwdb --update
EOF
chmod +x ${PARTITION}/finish.sh
printf "Enter chroot to run finish.sh\n"
su -c 'chroot /mnt/installation /usr/bin/env -i \
	HOME=/root TERM="$TERM" PS1="\u:\w\$ " \
	PATH=/bin:/usr/bin:/sbin:/usr/sbin \
	/bin/bash --login -c /finish.sh' root
rm ${PARTITION}/finish.sh
umount ${PARTITION}
#	Completed
printf "Installation completed\n"
