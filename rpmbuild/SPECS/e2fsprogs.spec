Summary:	Contains the utilities for the ext2 file system
Name:		e2fsprogs
Version:	1.42.7
Release:	1
License:	GPLv2
URL:		http://e2fsprogs.sourceforge.net
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://prdownloads.sourceforge.net/e2fsprogs/%{name}-%{version}.tar.gz
%description
The E2fsprogs package contains the utilities for handling
the ext2 file system.
%prep
%setup -q
install -vdm 755 build
%build
cd build
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
../configure \
--prefix=/usr \
--with-root-prefix='' \
--enable-elf-shlibs \
--disable-libblkid \
--disable-libuuid \
--disable-uuidd \
--disable-fsck
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
cd build
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install-libs
find %{buildroot}/usr/lib -name '*.a' -delete
rm -rf %{buildroot}/usr/share/info
%check
cd build
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/etc/mke2fs.conf
/lib/*
/sbin/*
/usr/bin/*
/usr/sbin/*
/usr/lib/*
/usr/include/*
/usr/share/locale/*
/usr/share/et/*
/usr/share/ss/*
/usr/share/man/*/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:1.42.7-1
-	Upgrade version
