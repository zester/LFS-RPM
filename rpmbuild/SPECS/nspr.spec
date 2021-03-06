Summary:	Platform-neutral API
Name:		nspr
Version:	4.9.6
Release:	1
License:	MPLv2.0
URL:		http://ftp.mozilla.org/pub/mozilla.org
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:	http://ftp.mozilla.org/pub/mozilla.org/%{name}/releases/v%{version}/src/%{name}-%{version}.tar.gz
%description
Netscape Portable Runtime (NSPR) provides a platform-neutral API
for system level and libc like functions.
%prep
%setup -q
cd mozilla/nsprpub
sed -ri 's#^(RELEASE_BINS =).*#\1#' pr/src/misc/Makefile.in
sed -i 's#$(LIBRARY) ##' config/rules.mk
%build
cd mozilla/nsprpub
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--with-mozilla \
	--with-pthreads \
	$([ $(uname -m) = x86_64 ] && echo --enable-64bit)
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd mozilla/nsprpub
make DESTDIR=%{buildroot} install
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datarootdir}/aclocal/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 4.9.6-1
-	Upgrade version
