Summary:	Utilities for file systems, consoles, partitions, and messages
Name:		util-linux
Version:	2.22.2
Release:	1
URL:		http://www.kernel.org/pub/linux/utils/util-linux
License:	GPLv2
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.kernel.org/pub/linux/utils/util-linux/v2.22/%{name}-%{version}.tar.xz
%description
Utilities for handling file systems, consoles, partitions,
and messages.
%prep
%setup -q
sed -i -e 's@etc/adjtime@var/lib/hwclock/adjtime@g' $(grep -rl '/etc/adjtime' .)
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--libdir=%{_libdir} \
	--disable-su \
	--disable-sulogin \
	--disable-login
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
install -vdm 755 %{buildroot}/var/lib/hwclock
make DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -name '*.la' -delete
%find_lang %{name}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files -f %{name}.lang
%defattr(-,root,root)
%attr(4755,root,root)	/bin/mount
%attr(4755,root,root)	/bin/umount
%attr(2755,root,tty)	%{_bindir}/wall
/sbin/*
/bin/dmesg
/bin/findmnt
/bin/kill
/bin/lsblk
/bin/more
/bin/mountpoint
/bin/wdctl
%{_bindir}/cal
%{_bindir}/chrt
%{_bindir}/col
%{_bindir}/colcrt
%{_bindir}/colrm
%{_bindir}/column
%{_bindir}/cytune
%{_bindir}/eject
%{_bindir}/fallocate
%{_bindir}/flock
%{_bindir}/getopt
%{_bindir}/hexdump
%{_bindir}/i386
%{_bindir}/ionice
%{_bindir}/ipcmk
%{_bindir}/ipcrm
%{_bindir}/ipcs
%{_bindir}/isosize
%{_bindir}/linux32
%{_bindir}/linux64
%{_bindir}/logger
%{_bindir}/look
%{_bindir}/lscpu
%{_bindir}/lslocks
%{_bindir}/mcookie
%{_bindir}/namei
%{_bindir}/pg
%{_bindir}/prlimit
%{_bindir}/rename
%{_bindir}/renice
%{_bindir}/rev
%{_bindir}/script
%{_bindir}/scriptreplay
%{_bindir}/setarch
%{_bindir}/setsid
%{_bindir}/setterm
%{_bindir}/tailf
%{_bindir}/taskset
%{_bindir}/ul
%{_bindir}/unshare
%{_bindir}/utmpdump
%{_bindir}/uuidgen
%{_bindir}/whereis
%{_includedir}/*
%{_libdir}/*
%{_sbindir}/*
%{_datarootdir}/getopt/*
%{_mandir}/*/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 2.22.2-1
-	Upgrade version

