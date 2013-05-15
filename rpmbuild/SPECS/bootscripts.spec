Summary:	Scripts for booting system
Name:		bootscripts
Version:	20130511
Release:	1
License:	GPLv3
URL:		http://www.linuxfromscratch.org/lfs
Group:		LFS/Base
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://www.linuxfromscratch.org/lfs/downloads/development/lfs-%{name}-%{version}.tar.bz2
%description
The LFS-Bootscripts package contains a set of scripts to start/stop
the LFS system at boot up/shutdown.
%prep
rm -rf %{_builddir}/*
cd %{_builddir}
tar xvf %{SOURCE0}
cd %{_builddir}/lfs-%{name}-%{version}
%build
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd %{_builddir}/lfs-%{name}-%{version}
make DESTDIR=%{buildroot} install
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
%dir /etc/init.d
%config /etc/rc.d/init.d
%config /etc/rc.d/rc0.d
%config /etc/rc.d/rc1.d
%config /etc/rc.d/rc2.d
%config /etc/rc.d/rc3.d
%config /etc/rc.d/rc4.d
%config /etc/rc.d/rc5.d
%config /etc/rc.d/rc6.d
%config /etc/rc.d/rcS.d
%config /etc/sysconfig/createfiles
%config /etc/sysconfig/modules
%config (noreplace) /etc/sysconfig/rc.site
%config /etc/sysconfig/udev_retry
/%{_lib}/*
/sbin/*
%{_mandir}/*/*
%changelog
*	Wed May 15 2013 baho-utot <baho-utot@columbus.rr.com> 20130511-1
-	Upgrade version to 20130511
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 20130123-1
-	Upgrade version
