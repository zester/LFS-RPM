Summary:	Main C library
Name:		glibc
Version:	2.17
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/libc
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/glibc/%{name}-%{version}.tar.xz
%description
This library provides the basic routines for allocating memory,
searching directories, opening and closing files, reading and
writing files, string handling, pattern matching, arithmetic,
and so on.
%prep
%setup -q
%build
install -vdm 755 %{_builddir}/%{name}-build
cd %{_builddir}/%{name}-build
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	../%{name}-%{version}/configure \
	--prefix=/usr \
	--disable-profile \
	--enable-kernel=2.6.25 \
	--libexecdir=/usr/lib/glibc
make %{?_smp_mflags}
%check
cd %{_builddir}/glibc-build
make -k check |& tee %{_specdir}/%{name}-check.log || true
%install
rm -rf %{_buildrootdir}/*
cd %{_builddir}/glibc-build
#	Create directories
install -vdm 755 %{buildroot}/usr/lib/locale
install -vdm 755 %{buildroot}/etc/ld.so.conf.d
make install_root=%{buildroot} install
cp -v %{_builddir}/%{name}-%{version}/sunrpc/rpc/*.h	%{buildroot}/usr/include/rpc
cp -v %{_builddir}/%{name}-%{version}/sunrpc/rpcsvc/*.h	%{buildroot}/usr/include/rpcsvc
cp -v %{_builddir}/%{name}-%{version}/nis/rpcsvc/*.h	%{buildroot}/usr/include/rpcsvc
#	Install locale generation script and config file
cp -v %{_sourcedir}/locale-gen.conf		%{buildroot}/etc
cp -v %{_sourcedir}/locale-gen.sh		%{buildroot}/sbin
#	Remove unwanted cruft
rm -rf %{buildroot}/usr/share/info
find %{buildroot}/usr/lib -name '*.la' -delete
#	Install configuration files
cat > %{buildroot}/etc/nsswitch.conf <<- "EOF"
#	Begin /etc/nsswitch.conf
	passwd: files
	group: files
	shadow: files

	hosts: files dns
	networks: files

	protocols: files
	services: files
	ethers: files
	rpc: files
#	End /etc/nsswitch.conf
EOF
cat > %{buildroot}/etc/ld.so.conf <<- "EOF"
#	Begin /etc/ld.so.conf
	/usr/local/lib
	include /etc/ld.so.conf.d/*.conf
EOF
%post
printf "Creating ldconfig cache\n";/sbin/ldconfig
printf "Creating locale files\n";/sbin/locale-gen.sh
%clean
rm -rf %{buildroot}/* %{_builddir}/*
%files
%defattr(-,root,root)
%config(noreplace) /etc/ld.so.conf
%config(noreplace) /etc/locale-gen.conf
%config /etc/nsswitch.conf
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
*	Sun Mar 24 2013 baho-utot <baho-utot@columbus.rr.com> 2.17-1
-	Update version

*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 2.16-1
-	Initial build.	First version
