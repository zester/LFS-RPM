Summary:	Main C library
Name:		glibc
Version:	2.16.0
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/libc
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/glibc/%{name}-%{version}.tar.xz
Patch:		http://www.linuxfromscratch.org/patches/lfs/7.2/glibc-2.16.0-res_query_fix-1.patch
%description
This library provides the basic routines for allocating memory,
searching directories, opening and closing files, reading and
writing files, string handling, pattern matching, arithmetic,
and so on.
%prep
%setup -q
sed -i 's#<rpc/types.h>#"rpc/types.h"#' sunrpc/rpc_clntout.c
sed -i '/test-installation.pl/d' Makefile
sed -i 's|@BASH@|/bin/bash|' elf/ldd.bash.in
%patch -p1
%build
install -vdm 755 %{_builddir}/%{name}-build
cd %{_builddir}/%{name}-build
../glibc-2.16.0/configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr \
	--libexecdir=/usr/lib/glibc \
	--disable-profile \
	--enable-add-ons \
	--enable-kernel=2.6.25
make %{?_smp_mflags}
%check
cd %{_builddir}/glibc-build
make -k check |& tee %{_specdir}/%{name}-check-log || true
%install
rm -rf %{_buildrootdir}/%{name}*
cd %{_builddir}/glibc-build
install -vdm 755 %{buildroot}/usr/lib/locale
make install_root=%{buildroot} install
#find %{buildroot}/usr/lib -name '*.a'  -delete
find %{buildroot}/usr/lib -name '*.la' -delete
rm -rf %{buildroot}/usr/share/info
cp -v ../glibc-2.16.0/sunrpc/rpc/*.h %{buildroot}/usr/include/rpc
cp -v ../glibc-2.16.0/sunrpc/rpcsvc/*.h %{buildroot}/usr/include/rpcsvc
cp -v ../glibc-2.16.0/nis/rpcsvc/*.h %{buildroot}/usr/include/rpcsvc
cat > %{buildroot}/etc/nsswitch.conf <<- "EOF"
	#Begin /etc/nsswitch.conf
	passwd: files
	group: files
	shadow: files

	hosts: files dns
	networks: files

	protocols: files
	services: files
	ethers: files
	rpc: files
	# End /etc/nsswitch.conf
EOF
cat > %{buildroot}/etc/ld.so.conf <<- "EOF"
# Begin /etc/ld.so.conf
	/lib
	/usr/lib
	/usr/local/lib
	include /etc/ld.so.conf.d/*.conf
EOF
install -vdm 755 %{buildroot}/etc/ld.so.conf.d
%clean
rm -rf %{buildroot} %{_builddir}/* %{builddir}/glibc-build
%files
%defattr(-,root,root)
%config(noreplace) /etc/ld.so.conf
%config(noreplace) /etc/nsswitch.conf
%dir /etc/ld.so.conf.d
/etc/rpc
/etc/ld.so.cache
/lib/*
/sbin/*
/usr/bin/*
/usr/include/*
/usr/lib/*
/usr/sbin/*
/usr/share/i18n/*
/usr/share/locale/*
/var/db/Makefile
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:2.16.0-0
-	Initial build.:	First version
