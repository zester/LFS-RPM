Summary:	Default file system
Name:		filesystem
Version:	20130401
Release:	1
License:	GPLv3
Group:		System Environment/Base
Vendor:		Bildanet
URL:		http://www.linuxfromscratch.org
Distribution:	Octothorpe
BuildArch: noarch
%define		LIBDIR	"/lib"
%description
The filesystem package is one of the basic packages that is installed
on a Linux system. Filesystem contains the basic directory
layout for a Linux operating system, including the correct permissions
for the directories.
%prep
%build
%install
rm -rf %{buildroot}
#	Kernel required directories
install -vdm 755 %{buildroot}/{dev,proc,sys}
#	Begin
install -vdm 755 %{buildroot}/{bin,boot,etc/{opt,sysconfig},home,lib,mnt,opt,run}
install -vdm 755 %{buildroot}/{media/{floppy,cdrom},sbin,srv,var}
install -vdm 0750 %{buildroot}/root
install -vdm 1777 %{buildroot}/tmp %{buildroot}/var/tmp
install -vdm 755 %{buildroot}/usr/{,local/}{bin,include,lib,sbin,src}
install -vdm 755 %{buildroot}/usr/{,local/}share/{doc,info,locale,man}
install -vdm 755 %{buildroot}/usr/{,local/}share/{misc,terminfo,zoneinfo}
install -vdm 755 %{buildroot}/usr/{,local/}share/man/man{1..8}
install -vdm 755 %{buildroot}/var/{log,mail,spool}
install -vdm 755 %{buildroot}/var/{opt,cache,lib/{misc,locate},local}
install -vdm 755 %{buildroot}/%{_libdir}/locale
#	End
%ifarch x86_64
ln -sv lib %{buildroot}/lib64
ln -sv lib %{buildroot}/usr/lib64
%endif
#	Symlinks
install -vdm 755 %{buildroot}/run/lock
ln -sv /run %{buildroot}/var/run
ln -sv /run/lock %{buildroot}/var/lock
#	install configuration files
touch %{buildroot}/etc/mtab
touch %{buildroot}/var/log/{btmp,lastlog,wtmp}
#	Configuration files
cat > %{buildroot}/etc/passwd <<- "EOF"
	root::0:0:root:/root:/bin/bash
	bin:x:1:1:bin:/dev/null:/bin/false
	nobody:x:99:99:Unprivileged User:/dev/null:/bin/false
EOF
cat > %{buildroot}/etc/group <<- "EOF"
	root:x:0:
	bin:x:1:
	sys:x:2:
	kmem:x:3:
	tape:x:4:
	tty:x:5:
	daemon:x:6:
	floppy:x:7:
	disk:x:8:
	lp:x:9:
	dialout:x:10:
	audio:x:11:
	video:x:12:
	utmp:x:13:
	usb:x:14:
	cdrom:x:15:
	mail:x:34:
	nogroup:x:99:
EOF
touch %{buildroot}/etc/mtab
cat > %{buildroot}/etc/sysconfig/ifconfig.eth0 <<- "EOF"
	ONBOOT=no
	IFACE=eth0
	SERVICE=ipv4-static
	IP=192.168.1.2
	GATEWAY=192.168.1.1
	PREFIX=24
	BROADCAST=192.168.1.255
EOF
cat > %{buildroot}/etc/resolv.conf <<- "EOF"
#	Begin /etc/resolv.conf
#	domain <Your Domain Name>
#	nameserver <IP address>
#	End /etc/resolv.conf
EOF
cat > %{buildroot}/etc/hosts <<- "EOF"
#	Begin /etc/hosts (network card version)
	127.0.0.1 localhost
#<192.168.1.1> <HOSTNAME.example.org> [alias1] [alias2 ...]
#	End /etc/hosts (network card version)
EOF
cat > %{buildroot}/etc/inittab <<- "EOF"
#	Begin /etc/inittab
	id:3:initdefault:
	si::sysinit:/etc/rc.d/init.d/rc S
	l0:0:wait:/etc/rc.d/init.d/rc 0
	l1:S1:wait:/etc/rc.d/init.d/rc 1
	l2:2:wait:/etc/rc.d/init.d/rc 2
	l3:3:wait:/etc/rc.d/init.d/rc 3
	l4:4:wait:/etc/rc.d/init.d/rc 4
	l5:5:wait:/etc/rc.d/init.d/rc 5
	l6:6:wait:/etc/rc.d/init.d/rc 6
	ca:12345:ctrlaltdel:/sbin/shutdown -t1 -a -r now
	su:S016:once:/sbin/sulogin
	1:2345:respawn:/sbin/agetty --noclear tty1 9600
	2:2345:respawn:/sbin/agetty tty2 9600
	3:2345:respawn:/sbin/agetty tty3 9600
	4:2345:respawn:/sbin/agetty tty4 9600
	5:2345:respawn:/sbin/agetty tty5 9600
	6:2345:respawn:/sbin/agetty tty6 9600
#	End /etc/inittab
EOF
echo "HOSTNAME=lfs" > %{buildroot}/etc/sysconfig/network
cat > %{buildroot}/etc/sysconfig/clock <<- "EOF"
#	Begin /etc/sysconfig/clock
	UTC=1
#	Set this to any options you might need to give to hwclock,
#	such as machine hardware clock type for Alphas.
	CLOCKPARAMS=
#	End /etc/sysconfig/clock
EOF
cat > %{buildroot}/etc/sysconfig/console <<- "EOF"
#	Begin /etc/sysconfig/console
#	KEYMAP="us"
#	FONT="lat1-16 -m utf8"
#	FONT="lat1-16 -m 8859-1"
#	KEYMAP_CORRECTIONS="euro2"
#	UNICODE="1"
#	LEGACY_CHARSET="iso-8859-1"
# End /etc/sysconfig/console
EOF
cat > %{buildroot}/etc/profile <<- "EOF"
# Begin /etc/profile
#export LANG=<ll>_<CC>.<charmap><@modifiers>
#	export LANG=en_US
#	export LANG=en_US.UTF-8
#	export LANG=C
# End /etc/profile
EOF
cat > %{buildroot}/etc/inputrc <<- "EOF"
#	Begin /etc/inputrc
#	Modified by Chris Lynn <roryo@roryo.dynup.net>
#	Allow the command prompt to wrap to the next line
	set horizontal-scroll-mode Off
#	Enable 8bit input
	set meta-flag On
	set input-meta On
#	Turns off 8th bit stripping
	set convert-meta Off
#	Keep the 8th bit for display
	set output-meta On
#	none, visible or audible
	set bell-style none
#	All of the following map the escape sequence of the value
#	contained in the 1st argument to the readline specific functions
	"\eOd": backward-word
	"\eOc": forward-word
#	for linux console
	"\e[1~": beginning-of-line
	"\e[4~": end-of-line
	"\e[5~": beginning-of-history
	"\e[6~": end-of-history
	"\e[3~": delete-char
	"\e[2~": quoted-insert
#	for xterm
	"\eOH": beginning-of-line
	"\eOF": end-of-line
#	for Konsole
	"\e[H": beginning-of-line
	"\e[F": end-of-line
#	End /etc/inputrc
EOF
cat > %{buildroot}/etc/fstab <<- "EOF"
#	Begin /etc/fstab
#	hdparm -I /dev/sda | grep NCQ --> can use barrier
#system		mnt-pt		type		options			dump fsck
#/dev/sdax	/		/ext3	defaults,barrier,noatime,noacl,data=ordered 1 1
/dev/sdxx	/		ext3		defaults		1 1
/dev/sdxx	/boot		ext3		defaults		1 2
#/dev/sdax	swap		swap		pri=1			0 0
proc		/proc		proc		nosuid,noexec,nodev	0 0
sysfs		/sys		sysfs		nosuid,noexec,nodev	0 0
devpts		/dev/pts	devpts		gid=5,mode=620		0 0
tmpfs		/run		tmpfs		defaults		0 0
devtmpfs	/dev		devtmpfs	mode=0755,nosuid	0 0
#	mount points
tmpfs		/tmp		tmpfs		defaults		0 0
#	End /etc/fstab
EOF
echo %{version} > %{buildroot}/etc/lfs-release
cat > %{buildroot}/etc/lsb-release <<- "EOF"
	DISTRIB_ID="Linux From Scratch"
	DISTRIB_RELEASE=%{version}
	DISTRIB_CODENAME="<your name here>"
	DISTRIB_DESCRIPTION="Linux From Scratch"
EOF
%files
%defattr(-,root,root)
%dir /
%dir /bin
%dir /boot
%dir /dev
%config(noreplace) /etc/fstab
%config(noreplace) /etc/group
%config(noreplace) /etc/hosts
%config(noreplace) /etc/inittab
%config(noreplace) /etc/inputrc
%config(noreplace) /etc/lfs-release
%config(noreplace) /etc/lsb-release
%config(noreplace) /etc/mtab
%config(noreplace) /etc/passwd
%config(noreplace) /etc/profile
%config(noreplace) /etc/resolv.conf
%config(noreplace) /etc/sysconfig/clock
%config(noreplace) /etc/sysconfig/console
%config(noreplace) /etc/sysconfig/ifconfig.eth0
%config(noreplace) /etc/sysconfig/network
%dir /home
%dir %{LIBDIR}
%dir /media
%dir /mnt
%dir /opt
%dir /proc
%dir /root
%dir /run
%dir /run/lock
%dir /sbin
%dir /srv
%dir /sys
%dir /tmp
%dir /usr
%dir %{_libdir}/locale
%dir /var/cache
%dir /var/lib
%dir /var/local
%dir /var/lock
%dir /var/mail
%dir /var/opt
%dir /var/run
%dir /var/spool
%dir /var/tmp
%ghost /var/log/wtmp
%ghost %attr(664,root,utmp)	/var/log/lastlog
%ghost %attr(600,-,-)		/var/log/btmp
%ifarch x86_64
%dir /lib64
%dir /usr/lib64
%endif
%clean
rm -rf %{buildroot}
%post
if [ -e /bin/mknod ]; then
[ -e /dev/console ] || /bin/mknod -m 600 /dev/console c 5 1
[ -e /dev/null ]    || /bin/mknod -m 666 /dev/null c 1 3
fi
%changelog
*	Fri Apr 19 2013 baho-utot <baho-utot@columbus.rr.com> 20130401-1
-	Upgrade version
