#!/tools/bin/bash
set -o errexit	# exit if error
set -o nounset	# exit if variable not initalized
set +h		# disable hashall
shopt -s -o pipefail
trap 'echo Filesystem build failed...;touch ${FAILURE};exit 1' ERR
[ -e $LFS/dev/console ] && exit 0
#	this is for kernel filesystem
export LFS=/mnt/lfs
su -c "chown lfs.lfs $LFS"
install -vdm 755 $LFS/{dev,proc,sys}
su -c "mknod	-m 600 $LFS/dev/console c 5 1"
su -c "mknod	-m 600 $LFS/dev/null c 1 3"
#	build filesystem on $LFS
install -vdm 755 $LFS/{bin,boot,etc/{opt,sysconfig},home,lib,opt,run}
install -vdm 755 $LFS/{media/{floppy,cdrom},sbin,srv,var}
install -vdm 0750 $LFS/root
install -vdm 1777 $LFS/tmp $LFS/var/tmp
install -vdm 755 $LFS/usr/{,local/}{bin,include,lib,sbin,src}
install -vdm 755 $LFS/usr/{,local/}share/{doc,info,locale,man}
install -vdm 755 $LFS/usr/{,local/}share/{misc,terminfo,zoneinfo}
install -vdm 755 $LFS/usr/{,local/}share/man/man{1..8}
install -vdm 755 $LFS/var/{log,mail,spool}
install -vdm 755 $LFS/var/{opt,cache,lib/{misc,locate},local}
case $(uname -m) in
	x86_64) ln -fsv lib $LFS/lib64 && ln -fsv lib $LFS/usr/lib64 ;;
esac
#	Set symlinks
ln	-fsv /run		$LFS/var/run
ln	-fsv /run/lock		$LFS/var/lock
ln	-sv /proc/self/mounts	$LFS/etc/mtab
#	symlinks needed for installation
ln 	-fsv /tools/bin/{bash,cat,echo,pwd,stty}	$LFS/bin
ln	-fsv /tools/bin/{env,perl,du,strip}		$LFS/usr/bin
ln	-fsv /tools/lib/libgcc_s.so{,.1}		$LFS/usr/lib
ln 	-fsv /tools/lib/libstdc++.so{,.6}		$LFS/usr/lib
ln	-fsv bash					$LFS/bin/sh
#	Needed for rpm
ln	-fsv /tools/bin/getconf				$LFS/usr/bin
ln	-fsv /tools/bin/sed				$LFS/usr/bin
ln	-fsv /tools/bin/rm				$LFS/usr/bin
ln	-fsv /tools/bin/strip				$LFS/usr/bin
#	Setup needed files
touch $LFS/etc/mtab
cat > $LFS/etc/passwd <<- "EOF"
	root::0:0:root:/root:/bin/bash
	bin:x:1:1:bin:/dev/null:/bin/false
	nobody:x:99:99:Unprivileged User:/dev/null:/bin/false
EOF
cat > $LFS/etc/group <<- "EOF"
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
touch $LFS/var/log/{btmp,lastlog,wtmp}
su -c "chgrp -v utmp $LFS/var/log/lastlog"
su -c "chmod -v 664  $LFS/var/log/lastlog"
su -c "chmod -v 600  $LFS/var/log/btmp"
