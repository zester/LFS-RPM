Summary:	Shared libraries, portable interface.
Name:		libtool
Version:	2.4.2
Release:	1
License:	GPLv2
URL:		http://www.gnu.org/software/libtool
Group:		Development/Tools
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/libtool/%{name}-%{version}.tar.gz
%description
It wraps the complexity of using shared libraries in a consistent, portable interface.
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
/usr/bin/*
/usr/lib/*
/usr/include/*
/usr/share/aclocal/*
/usr/share/%{name}/*
/usr/share/man/*/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:2.4.2-0
-	Initial build.	First version	
