set -o errexit	# exit if error
#set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
#	install locale files
printf "%s\n" "Creating locale files"
/sbin/locale-gen.sh
#	install ld cache
/sbin/ldconfig
#	enable shadowed passwords and group passwords
/usr/sbin/pwconv
/usr/sbin/grpconv
#	udev script
source /lib/udev/init-net-rules.sh
/sbin/udevadm hwdb --update
#	Configuration
LIST="/etc/sysconfig/clock /etc/sysconfig/console /etc/profile /etc/sysconfig/network /etc/hosts /etc/fstab /etc/sysconfig/ifconfig.eth0 /etc/resolv.conf /etc/passwd /etc/lsb-release /etc/sysconfig/rc.site"
for i in ${LIST}; do
	vim "${i}"
done
