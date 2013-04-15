Summary:	Programs for compressing and decompressing files
Name:		xz
Version:	5.0.4
Release:	1
URL:		http://tukaani.org/xz
License:	GPLv2
Group:		Applications/File
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://tukaani.org/xz/%{name}-%{version}.tar.xz
%description
The Xz package contains programs for compressing and
decompressing files
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr \
	--libdir=/lib \
	--docdir=/usr/share/doc/%{name}-%{version}
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} pkgconfigdir=/usr/lib/pkgconfig install
find %{buildroot}/usr/lib -name '*.la' -delete
%find_lang %{name}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%clean
rm -rf %{buildroot}
%files -f %{name}.lang
%defattr(-,root,root)
/lib/*
/usr/bin/*
/usr/include/*
/usr/share/doc/%{name}-%{version}/*
/usr/share/man/*/*
/usr/lib/pkgconfig/liblzma.pc
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 0:5.0.4-0
-	Initial build.	First version
