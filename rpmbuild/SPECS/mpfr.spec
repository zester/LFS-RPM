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
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--docdir=%{_defaultdocdir}/%{name}-%{version} \
	--enable-thread-safe
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -name '*.a' -delete
find %{buildroot}%{_libdir} -name '*.la' -delete
rm -rf %{buildroot}%{_infodir}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_defaultdocdir}/%{name}-%{version}/*
%{_defaultdocdir}/%{name}-%{version}/AUTHORS
%{_defaultdocdir}/%{name}-%{version}/BUGS
%{_defaultdocdir}/%{name}-%{version}/COPYING
%{_defaultdocdir}/%{name}-%{version}/COPYING.LESSER
%{_defaultdocdir}/%{name}-%{version}/FAQ.html
%{_defaultdocdir}/%{name}-%{version}/NEWS
%{_defaultdocdir}/%{name}-%{version}/TODO
%{_defaultdocdir}/%{name}-%{version}/examples/*
%changelog
*	Sat Apr 20 2013 baho-utot <baho-utot@columbus.rr.com> 3.1.2-1
-	Upgrade version
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 3.1.1-1
-	Initial build.	First version
