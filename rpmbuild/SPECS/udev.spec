Summary:	Programs for dynamic creation of device nodes
Name:		udev
Version:	199
Release:	1
License:	GPLv2
URL:		http://www.freedesktop.org/wiki/Software/systemd/
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://www.freedesktop.org/software/systemd/systemd-198.tar.xz
%description
The Udev package contains programs for dynamic creation of device nodes.
%prep
rm -rf %{_builddir}/*
cd %{_builddir}
tar xvf %{_sourcedir}/systemd-${version}.tar.xz
tar xvf %{_sourcedir}/udev-lfs-%{version}-2.tar.bz2
cd %{_builddir}/systemd-%{version}
mv ../udev-lfs-%{version}-3 .
%build
cd %{_builddir}/systemd-%{version}
make %{?_smp_mflags} -f udev-lfs-%{version}-2/Makefile.lfs
%install
rm -rf %{buildroot}
cd %{_builddir}/systemd-%{version}
make -f udev-lfs-%{version}-3/Makefile.lfs DESTDIR=%{buildroot} install
%clean
rm -rf %{buildroot}
%post
/sbin/ldconfig
/sbin/udevadm hwdb --update
/lib/udev/init-net-rules.sh
%postun	-p /sbin/ldconfig
%files 
%defattr(-,root,root)
%config /etc/udev/rules.d/55-lfs.rules
%config /etc/udev/rules.d/81-cdrom.rules
%config /etc/udev/rules.d/83-cdrom-symlinks.rules
/lib/*
/sbin/*
/usr/lib/*
/usr/include/*
/usr/share/doc/%{name}/*
/usr/share/man/*/*
%changelog
*	Mon Apr  1 2013 GangGreene <GangGreene@bildanet.com> 0:199-1
-	Upgrade version

*	Wed Mar 21 2013 GangGreene <GangGreene@bildanet.com> 0:197-1
-	Upgrade version
