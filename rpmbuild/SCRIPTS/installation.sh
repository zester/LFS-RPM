set -o errexit	# exit if error
#set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
#	install base packages
rpm --initdb --dbpath /mnt/var/lib/rpm
rpm -Uvh --nodeps --root /mnt RPMS/noarch/*
rpm -Uvh --nodeps --root /mnt RPMS/i686/*
#	Configuration
LIST=(/etc/sysconfig/clock /etc/sysconfig/console /etc/profile /etc/sysconfig/network /etc/hosts /etc/fstab /etc/sysconfig/ifconfig.eth0 /etc/resolv.conf /etc/passwd /etc/lsb-release /etc/sysconfig/rc.site)
for i in ${LIST[@]}; do
	vim "/mnt${i}"
done
#	create script and complete installation
cat > /mnt/finish.sh <<- "EOF"
#	create here doc and exec chroot bash -c here.doc
	#	install locale files
	printf "%s\n" "Creating locale files"
	/usr/bin/localedef -i cs_CZ -f UTF-8 cs_CZ.UTF-8
	/usr/bin/localedef -i de_DE -f ISO-8859-1 de_DE
	/usr/bin/localedef -i de_DE@euro -f ISO-8859-15 de_DE@euro
	/usr/bin/localedef -i de_DE -f UTF-8 de_DE.UTF-8
	/usr/bin/localedef -i en_GB -f UTF-8 en_GB.UTF-8
	/usr/bin/localedef -i en_HK -f ISO-8859-1 en_HK
	/usr/bin/localedef -i en_PH -f ISO-8859-1 en_PH
	/usr/bin/localedef -i en_US -f ISO-8859-1 en_US
	/usr/bin/localedef -i en_US -f UTF-8 en_US.UTF-8
	/usr/bin/localedef -i es_MX -f ISO-8859-1 es_MX
	/usr/bin/localedef -i fa_IR -f UTF-8 fa_IR
	/usr/bin/localedef -i fr_FR -f ISO-8859-1 fr_FR
	/usr/bin/localedef -i fr_FR@euro -f ISO-8859-15 fr_FR@euro
	/usr/bin/localedef -i fr_FR -f UTF-8 fr_FR.UTF-8
	/usr/bin/localedef -i it_IT -f ISO-8859-1 it_IT
	/usr/bin/localedef -i it_IT -f UTF-8 it_IT.UTF-8
	/usr/bin/localedef -i ja_JP -f EUC-JP ja_JP
	/usr/bin/localedef -i ru_RU -f KOI8-R ru_RU.KOI8-R
	/usr/bin/localedef -i ru_RU -f UTF-8 ru_RU.UTF-8
	/usr/bin/localedef -i tr_TR -f UTF-8 tr_TR.UTF-8
	/usr/bin/localedef -i zh_CN -f GB18030 zh_CN.GB18030
	#	install ld cache
	/sbin/ldconfig -v
	#	enable shadowed passwords and group passwords
	/usr/sbin/pwconv
	/usr/sbin/grpconv
	#	udev script
	source	/lib/udev/init-net-rules.sh
	/sbin/udevadm hwdb --update
EOF
chmod +x /mnt/finish.sh
su -c 'chroot "/mnt" /usr/bin/env -i \
	HOME=/root TERM="$TERM" PS1="\u:\w\$ " \
	PATH=/bin:/usr/bin:/sbin:/usr/sbin \
	/bin/bash --login -c /finish.sh' root
#	Completed
printf "Installation completed\n"


