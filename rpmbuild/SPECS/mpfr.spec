Summary:	Functions for multiple precision math
Name:		mpfr
Version:	3.1.2
Release:	1
License:	GPLv3
URL:		http://www.mpfr.org
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.mpfr.org/%{name}-%{version}/%{name}-%{version}.tar.xz
%description
The MPFR package contains functions for multiple precision math.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr \
	--docdir=/usr/share/doc/%{name}-%{version} \
	--enable-thread-safe
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
find %{buildroot}/usr/lib -name '*.a'  -delete
find %{buildroot}/usr/lib -name '*.la' -delete
rm -rf %{buildroot}/usr/share/info
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/usr/include/*
/usr/lib/*
/usr/share/doc/%{name}-%{version}/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 3.1.1-0
-	Initial build.	First version
