Summary:	Platform-neutral API
Name:		nspr
Version:	4.9.2
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
	--prefix=/usr \
	--bindir=/usr/bin \
	--libdir=/usr/lib \
	--with-mozilla \
	--with-pthreads \
	$([ $(uname -m) = x86_64 ] && echo --enable-64bit)
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
cd mozilla/nsprpub
make DESTDIR=%{buildroot} install
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/usr/bin/*
/usr/include/*
/usr/lib/*
/usr/share/aclocal/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:4.9.2-0
-	Initial build.	First version
