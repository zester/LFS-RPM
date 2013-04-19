Summary:	Linux Api header files
Name:		linux-api-headers
Version:	3.8.5
Release:	1
License:	GPLv2
URL:		http://www.kernel.org/
Group:		System Environment/Kernel
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.kernel.org/pub/linux/kernel/v3.x/linux-%{version}.tar.xz
BuildArch:	noarch
%description
The Linux API Headers expose the kernel's API for use by Glibc.
%define pkgdir	%{_builddir}/linux-%{version}
%prep
tar xf %{_sourcedir}/linux-%{version}.tar.xz
%build
cd %{_builddir}/linux-%{version}
make mrproper
make headers_check
%install
cd %{_builddir}/linux-%{version}
rm -rf %{buildroot}/*
make INSTALL_HDR_PATH=dest headers_install
find dest/include \( -name .install -o -name ..install.cmd \) -delete
install -vdm 755 %{buildroot}%{_includedir}
cp -rv dest/include/* %{buildroot}%{_includedir}
%clean
rm -rf %{buildroot} %{_builddir}/*
%files
%defattr(-,root,root)
%{_includedir}/asm/*.h
%{_includedir}/asm-generic/*.h
%{_includedir}/drm/*.h
%{_includedir}/linux/byteorder/*.h
%{_includedir}/linux/caif/*.h
%{_includedir}/linux/dvb/*.h
%{_includedir}/linux/hdlc/*.h
%{_includedir}/linux/hsi/*.h
%{_includedir}/linux/isdn/*.h
%{_includedir}/linux/*.h
%{_includedir}/linux/can/*.h
%{_includedir}/linux/mmc/*.h
%{_includedir}/linux/netfilter/*.h
%{_includedir}/linux/netfilter_arp/*.h
%{_includedir}/linux/netfilter_bridge/*.h
%{_includedir}/linux/netfilter_ipv4/*.h
%{_includedir}/linux/netfilter_ipv6/*.h
%{_includedir}/linux/netfilter/ipset/*.h
%{_includedir}/linux/nfsd/*.h
%{_includedir}/linux/raid/*.h
%{_includedir}/linux/spi/*.h
%{_includedir}/linux/sunrpc/*.h
%{_includedir}/linux/tc_act/*.h
%{_includedir}/linux/tc_ematch/*.h
%{_includedir}/linux/usb/*.h
%{_includedir}/linux/wimax/*.h
%{_includedir}/mtd/*.h
%{_includedir}/rdma/*.h
%{_includedir}/scsi/*.h
%{_includedir}/scsi/fc/*.h
%{_includedir}/sound/*.h
%{_includedir}/video/*.h
%{_includedir}/xen/*.h


%changelog
*	Fri Apr 19 2013 baho-utot <baho-utot@columbus.rr.com> 3.8.5-1
-	Update version to 3.8.4
*	Mon Apr 1 2013 baho-utot <baho-utot@columbus.rr.com> 3.8.4-1
-	Update version to 3.8.4
*	Sun Mar 24 2013 baho-utot <baho-utot@columbus.rr.com> 3.8.3-1
-	Update version to 3.8.3
*	Sun Mar 24 2013 baho-utot <baho-utot@columbus.rr.com> 3.8.1-1
-	Update version
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 3.5.2-1
-	Initial build.	First version
