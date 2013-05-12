Summary:	Compression and decompression routines
Name:		zlib
Version:	1.2.8
Release:	1
URL:		http://www.zlib.net/
License:	MIT
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.zlib.net/%{name}-%{version}.tar.xz
%description
Compression and decompression routines
%prep
%setup -q
%build
CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/%{_lib}
mv -v %{buildroot}%{_libdir}/libz.so.* %{buildroot}/%{_lib}
ln -sfv ../../%{_lib}/libz.so.1.2.8 %{buildroot}%{_libdir}/libz.so
find %{buildroot}%{_libdir} -name '*.a' -delete
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
/%{_lib}/*
%{_includedir}/*.h
%{_libdir}/libz.so
%{_libdir}/pkgconfig/zlib.pc
%{_mandir}/man3/*
%changelog
*	Fri May 10 2013 baho-utot <baho-utot@columbus.rr.com> 1.2.8-1
-	Upgrade version
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 1.2.7-1
-	Initial build.	First version
