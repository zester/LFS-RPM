Summary:	Library for the arithmetic of complex numbers
Name:		mpc
Version:	1.0
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
	--prefix=/usr 
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
#find %{buildroot}/usr/lib -name '*.a'  -delete
find %{buildroot}/usr/lib -name '*.la' -delete
rm -rf %{buildroot}//usr/share/info
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
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 1.0-0
-	Initial build.	First version
