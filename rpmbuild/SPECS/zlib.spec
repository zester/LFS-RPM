Summary:	Compression and decompression routines
Name:		zlib
Version:	1.2.7
Release:	1
URL:		http://www.zlib.net/
License:	MIT
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.zlib.net/%{name}-%{version}.tar.bz2
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
rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/lib
mv -v %{buildroot}%{_libdir}/libz.so.* %{buildroot}/lib
ln -sfv ../../lib/libz.so.1.2.7 %{buildroot}%{_libdir}/libz.so
find %{buildroot}%{_libdir} -name '*.a'  -delete
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
/lib/*
%{_includedir}/*
%{_libdir}/*
%{_mandir}/*/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 0:1.2.7-0
-	Initial build.	First version
