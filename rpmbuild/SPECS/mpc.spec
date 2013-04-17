Summary:	Library for the arithmetic of complex numbers
Name:		mpc
Version:	1.0.1
Release:	1
License:	LGPLv3
URL:		http://www.multiprecision.org
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.multiprecision.org/mpc/download/%{name}-%{version}.tar.gz
%description
The MPC package contains a library for the arithmetic of complex
numbers with arbitrarily high precision and correct rounding of
the result.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -name '*.a'  -delete
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
%{_includedir}/*
%{_libdir}/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:1.0.1-1
-	Upgrade version
