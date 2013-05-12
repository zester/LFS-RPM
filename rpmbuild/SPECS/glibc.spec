Summary:	Main C library
Name:		glibc
Version:	2.17
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/libc
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://ftp.gnu.org/gnu/glibc/%{name}-%{version}.tar.xz
Source1:	locale-gen.conf
Source2:	locale-gen.sh

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
	--prefix=%{_prefix} \
	--disable-profile \
	--enable-kernel=2.6.25 \
	--libexecdir=%{_libexecdir}
make %{?_smp_mflags}
%check
cd %{_builddir}/glibc-build
make -k check |& tee %{_specdir}/%{name}-check.log || true
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd %{_builddir}/glibc-build
#	Create directories
install -vdm 755 %{buildroot}%{_libdir}/locale
install -vdm 755 %{buildroot}/etc/ld.so.conf.d
make install_root=%{buildroot} install
cp -v %{_builddir}/%{name}-%{version}/sunrpc/rpc/*.h	%{buildroot}%{_includedir}/rpc
cp -v %{_builddir}/%{name}-%{version}/sunrpc/rpcsvc/*.h	%{buildroot}%{_includedir}/rpcsvc
cp -v %{_builddir}/%{name}-%{version}/nis/rpcsvc/*.h	%{buildroot}%{_includedir}/rpcsvc
#	Install locale generation script and config file
cp -v %{SOURCE1}	%{buildroot}/etc
cp -v %{SOURCE2}	%{buildroot}/sbin

rm -rf %{buildroot}/%{_var}/db
#	Remove unwanted cruft
rm -rf %{buildroot}%{_infodir}
find %{buildroot}%{_libdir} -name '*.la' -delete
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
%config /etc/rpc
%config /etc/ld.so.cache
/lib/*
/sbin/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_libexecdir}/pt_chown
%{_libexecdir}/getconf/*
%{_sbindir}/*
%{_datarootdir}/i18n/*
%lang(be) %{_datarootdir}/locale/be/LC_MESSAGES/libc.mo
%lang(bg) %{_datarootdir}/locale/bg/LC_MESSAGES/libc.mo
%lang(ca) %{_datarootdir}/locale/ca/LC_MESSAGES/libc.mo
%lang(cs) %{_datarootdir}/locale/cs/LC_MESSAGES/libc.mo
%lang(da) %{_datarootdir}/locale/da/LC_MESSAGES/libc.mo
%lang(de) %{_datarootdir}/locale/de/LC_MESSAGES/libc.mo
%lang(el) %{_datarootdir}/locale/el/LC_MESSAGES/libc.mo
%lang(en_GB) %{_datarootdir}/locale/en_GB/LC_MESSAGES/libc.mo
%lang(eo) %{_datarootdir}/locale/eo/LC_MESSAGES/libc.mo
%lang(es) %{_datarootdir}/locale/es/LC_MESSAGES/libc.mo
%lang(fi) %{_datarootdir}/locale/fi/LC_MESSAGES/libc.mo
%lang(fr) %{_datarootdir}/locale/fr/LC_MESSAGES/libc.mo
%lang(gl) %{_datarootdir}/locale/gl/LC_MESSAGES/libc.mo
%lang(hr) %{_datarootdir}/locale/hr/LC_MESSAGES/libc.mo
%lang(hu) %{_datarootdir}/locale/hu/LC_MESSAGES/libc.mo
%lang(id) %{_datarootdir}/locale/id/LC_MESSAGES/libc.mo
%lang(it) %{_datarootdir}/locale/it/LC_MESSAGES/libc.mo
%lang(ja) %{_datarootdir}/locale/ja/LC_MESSAGES/libc.mo
%lang(ko) %{_datarootdir}/locale/ko/LC_MESSAGES/libc.mo
%{_datarootdir}/locale/locale.alias
%lang(lt) %{_datarootdir}/locale/lt/LC_MESSAGES/libc.mo
%lang(nb) %{_datarootdir}/locale/nb/LC_MESSAGES/libc.mo
%lang(nl) %{_datarootdir}/locale/nl/LC_MESSAGES/libc.mo
%lang(pl) %{_datarootdir}/locale/pl/LC_MESSAGES/libc.mo
%lang(pt_BR) %{_datarootdir}/locale/pt_BR/LC_MESSAGES/libc.mo
%lang(ru) %{_datarootdir}/locale/ru/LC_MESSAGES/libc.mo
%lang(rw) %{_datarootdir}/locale/rw/LC_MESSAGES/libc.mo
%lang(sk) %{_datarootdir}/locale/sk/LC_MESSAGES/libc.mo
%lang(sv) %{_datarootdir}/locale/sv/LC_MESSAGES/libc.mo
%lang(tr) %{_datarootdir}/locale/tr/LC_MESSAGES/libc.mo
%lang(vi) %{_datarootdir}/locale/vi/LC_MESSAGES/libc.mo
%lang(zh_CN) %{_datarootdir}/locale/zh_CN/LC_MESSAGES/libc.mo
%lang(zh_TW) %{_datarootdir}/locale/zh_TW/LC_MESSAGES/libc.mo
%changelog
*	Sun Mar 24 2013 baho-utot <baho-utot@columbus.rr.com> 2.17-1
-	Update version

*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 2.16-1
-	Initial build.	First version
