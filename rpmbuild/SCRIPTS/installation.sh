set -o errexit	# exit if error
#set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail

DEVICE=/dev/sdax
PARTITION=/mnt/installation

die() {
	local msg=$1
	printf "Installation failed: ${msg}\n"
	exit 1
}
#	Mount partition
[ -d ${PARTITION } || install -vdm 777 ${PARTITION}
mount ${DEVICE} ${PARTITION} || die "Can not mount PARTITION\n"
#	Install base packages
rpm --initdb --dbpath ${PARTITION}/var/lib/rpm
rpm -Uvh --nodeps --root ${PARTITION} RPMS/noarch/*
rpm -Uvh --nodeps --root ${PARTITION} RPMS/i686/*
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
su -c 'chroot "${PARTITION}" /usr/bin/env -i \
	HOME=/root TERM="$TERM" PS1="\u:\w\$ " \
	PATH=/bin:/usr/bin:/sbin:/usr/sbin \
	/bin/bash --login -c /finish.sh' root
rm ${PARTITION}/finish.sh
#	Completed
printf "Installation completed\n"
