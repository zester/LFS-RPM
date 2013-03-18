Summary:	Programs for dynamic creation of device nodes
Name:		udev
Version:	188
Release:	1
License:	GPLv2
URL:		http://www.freedesktop.org/wiki/Software/systemd/
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://www.freedesktop.org/software/systemd/systemd-188.tar.xz
%description
The Udev package contains programs for dynamic creation of device nodes.
%prep
rm -rf %{_builddir}/*
cd %{_builddir}
tar xvf %{_sourcedir}/systemd-188.tar.xz
tar xvf %{_sourcedir}/udev-lfs-188-3.tar.bz2
cd %{_builddir}/systemd-%{version}
mv ../udev-lfs-%{version} .
%build
cd %{_builddir}/systemd-%{version}
make %{?_smp_mflags} -f udev-lfs-188/Makefile.lfs
%install
rm -rf %{buildroot}
cd %{_builddir}/systemd-%{version}
make -f udev-lfs-188/Makefile.lfs DESTDIR=%{buildroot} install
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files 
%defattr(-,root,root)
%config(noreplace) /etc/udev/rules.d/55-lfs.rules
/lib/*
/sbin/*
/usr/lib/*
/usr/include/*
/usr/share/doc/%{name}/*
/usr/share/man/*/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:188-0
-	Initial build.	First version
-	/lib/udev/init-net-rules.sh
