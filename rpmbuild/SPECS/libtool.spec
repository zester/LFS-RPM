Summary:	Shared libraries, portable interface
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
It wraps the complexity of using shared libraries in a 
consistent, portable interface.
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
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_datarootdir}/aclocal/*
%{_datarootdir}/%{name}/*
%{_mandir}/*/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 2.4.2-1
-	Initial build.	First version	
