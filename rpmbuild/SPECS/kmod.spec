Summary:	Utilities for loading kernel modules
Name:		kmod
Version:	13
Release:	1
License:	GPLv2
URL:		http://www.kernel.org/pub/linux/utils/kernel/kmod
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.kernel.org/pub/linux/utils/kernel/kmod/%{name}-%{version}.tar.xz
%description
The Kmod package contains libraries and utilities for loading kernel modules
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--bindir=/bin \
	--libdir=/%{_lib} \
	--sysconfdir=/etc \
	--disable-manpages \
	--with-xz \
	--with-zlib
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} pkgconfigdir=%{_libdir}/pkgconfig install
install -vdm 755 %{buildroot}/sbin
for target in depmod insmod modinfo modprobe rmmod; do
	ln -sv ../bin/kmod %{buildroot}/sbin/$target
done
ln -sv kmod %{buildroot}/bin/lsmod
find %{buildroot}/%{_lib} -name '*.la' -delete
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/bin/*
/%{_lib}/*
/sbin/*
%{_libdir}/pkgconfig/libkmod.pc
%{_includedir}/*
#/usr/share/man/*/*
%changelog
*	Fri May 10 2013 baho-utot <baho-utot@columbus.rr.com> 13-1
-	Update version to 13
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 12-1
-	Upgrade version
