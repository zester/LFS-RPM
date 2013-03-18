Summary:	Programs for logging system messages
Name:		sysklogd
Version:	1.5
Release:	1
License:	GPLv2
URL:		http://www.infodrom.org/projects/sysklogd
Group:		System Environment/Daemons
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://www.infodrom.org/projects/sysklogd/download/%{name}-%{version}.tar.gz
%description
The package contains programs for logging system messages
such as those given by the kernel when unusual things happen.
%prep
%setup -q
%build
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
install -vdm 755 %{buildroot}/etc/logrotate.d
install -vdm 755 %{buildroot}/usr/bin
install -vdm 755 %{buildroot}/usr/share/man/man{5,8}
install -vdm 755 %{buildroot}/usr/sbin
install -vdm 755 %{buildroot}/usr/include/sysklogd
install -vdm 755 %{buildroot}/sbin
make install prefix=%{buildroot} \
	TOPDIR=%{buildroot} \
	MANDIR=%{buildroot}/usr/share/man \
	BINDIR=%{buildroot}/sbin \
	MAN_USER=`id -nu` MAN_GROUP=`id -ng`
cat > %{buildroot}/etc/syslog.conf <<- "EOF"
	# Begin /etc/syslog.conf

	auth,authpriv.* -/var/log/auth.log
	*.*;auth,authpriv.none -/var/log/sys.log
	daemon.* -/var/log/daemon.log
	kern.* -/var/log/kern.log
	mail.* -/var/log/mail.log
	user.* -/var/log/user.log
	*.emerg *

	# End /etc/syslog.conf
EOF
cat > %{buildroot}/etc/logrotate.d/sysklogd <<- "EOF"
	/var/log/messages /var/log/secure /var/log/maillog /var/log/spooler /var/log/boot.log /var/log/cron {
	weekly
	sharedscripts
	postrotate
	/bin/kill -HUP `cat /var/run/syslogd.pid 2> /dev/null` 2> /dev/null || true
	endscript
}
EOF
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
%config(noreplace) /etc/syslog.conf
%config(noreplace) /etc/logrotate.d/sysklogd
/sbin/*
/usr/share/man/*/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:1.5-0
-	Initial build.	First version
