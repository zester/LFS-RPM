Summary:	Utilities for loading kernel modules
Name:		kmod
Version:	9
Release:	1
License:	GPLv2
URL:		http://www.kernel.org/pub/linux/utils/kernel/kmod
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.kernel.org/pub/linux/utils/kernel/kmod/%{name}-%{version}.tar.xz
Patch:		kmod-9-testsuite-1.patch
%description
The Kmod package contains libraries and utilities for loading kernel modules
%prep
%setup -q
%patch -p1
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr \
	--bindir=/bin \
	--libdir=/lib \
	--sysconfdir=/etc \
	--with-xz \
	--with-zlib
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} pkgconfigdir=/usr/lib/pkgconfig install
install -vdm 755 %{buildroot}/sbin
for target in depmod insmod modinfo modprobe rmmod; do
	ln -sv ../bin/kmod %{buildroot}/sbin/$target
done
ln -sv kmod %{buildroot}/bin/lsmod
find %{buildroot}/lib -name '*.la' -delete
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/bin/*
/lib/*
/sbin/*
/usr/lib/pkgconfig/libkmod.pc
/usr/include/*
/usr/share/man/*/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:9-0
-	Initial build.	First version
