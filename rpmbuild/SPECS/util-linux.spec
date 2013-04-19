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
/bin/*
/sbin/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_sbindir}/*
%{_datarootdir}/getopt/*
%{_mandir}/*/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 0:2.22.2-0
-	Upgrade version

