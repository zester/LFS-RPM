Summary:	Programs for dynamic creation of device nodes
Name:		udev
Version:	202
Release:	1
License:	GPLv2
URL:		http://www.freedesktop.org/wiki/Software/systemd/
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://www.freedesktop.org/software/systemd/systemd-%{version}.tar.xz
Source1:	http://anduin.linuxfromscratch.org/sources/other/udev-lfs-%{version}-1.tar.bz2
%description
The Udev package contains programs for dynamic creation of device nodes.
%prep
rm -rf %{_builddir}/*
cd %{_builddir}
tar xvf %{SOURCE0}
tar xvf %{SOURCE1}
cd %{_builddir}/systemd-%{version}
mv ../udev-lfs-%{version}-1 .
%build
cd %{_builddir}/systemd-%{version}
make %{?_smp_mflags} -f udev-lfs-202-1/Makefile.lfs
%install
rm -rf %{buildroot}
cd %{_builddir}/systemd-%{version}
make -f udev-lfs-202-1/Makefile.lfs DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/%{_defaultdocdir}/%{name|-%{version}/html
mv %{buildroot}/%{_defaultdocdir}/gtk-doc/html/* %{buildroot}/%{_defaultdocdir}/%{name|-%{version}/html
rm -rf %{buildroot}/%{_defaultdocdir}/gtk-doc
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
/%{_lib}/*
/sbin/*
%{_libdir}/*
%{_includedir}/*
%{_defaultdocdir}/%{name}-%{version}/*
%{_mandir}/*/*
%changelog
*	Fri May 10 2013 baho-utot <baho-utot@columbus.rr.com> 202-1
-	Update version to 202
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 200-1
-	Upgrade version
