Summary:	Package manager
Name:		rpm
Version:	4.11.0.1
Release:	1
License:	GPLv2
URL:		http://rpm.org
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://rpm.org/releases/rpm-4.11.x/%{name}-%{version}.tar.bz2
%description
RPM package manager
%prep
%setup -q
%build
./autogen.sh --noconfigure
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	CPPFLAGS='-I/usr/include/nspr -I/usr/include/nss' \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--disable-static \
	--with-lua 
#	--with-external-db
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -name '*.a' -delete
find %{buildroot}%{_libdir} -name '*.la' -delete
%find_lang %{name}
#	Fix macros and prefix
sed -i 's|optflags: i386 -O2 -g -march=i386 -mtune=i686|optflags: i386 -O2 -march=i486 -mtune=i686 -pipe|' %{buildroot}%{_libdir}/rpm/rpmrc
sed -i 's|optflags: i486 -O2 -g -march=i486|optflags: i486 -O2 -march=i486 -mtune=i686 -pipe|' %{buildroot}%{_libdir}/rpm/rpmrc
sed -i 's|optflags: i586 -O2 -g -march=i586|optflags: i586 -O2 -march=i586 -mtune=i686 -pipe|' %{buildroot}%{_libdir}/rpm/rpmrc
sed -i 's|optflags: i686 -O2 -g -march=i686|optflags: i686 -O2 -march=i486 -mtune=i686 -pipe|' %{buildroot}%{_libdir}/rpm/rpmrc
sed -i 's|optflags: x86_64 -O2 -g|optflags: x86_64 -O2 -march=x86_64 -mtune=generic -pipe|'    %{buildroot}%{_libdir}/rpm/rpmrc
sed -i 's|optflags: athlon -O2 -g -march=athlon|optflags: athlon -O2 -march=athlon -mtune=generic -pipe|' %{buildroot}%{_libdir}/rpm/rpmrc
sed -i 's|\${prefix}||' %{buildroot}%{_libdir}/rpm/macros
%post -p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%clean
rm -rf %{buildroot}
%files -f %{name}.lang
%defattr(-,root,root)
/bin/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_libdir}/pkgconfig/rpm.pc
%{_libdir}/rpm-plugins/exec.so
%{_mandir}/man1/*
%{_mandir}/fr/man8/*.gz
%{_mandir}/ja/man8/*.gz
%{_mandir}/ko/man8/*.gz
%{_mandir}/man8/*.gz
%{_mandir}/pl/man1/*.gz
%{_mandir}/pl/man8/*.gz
%{_mandir}/ru/man8/*.gz
%{_mandir}/sk/man8/*.gz

%changelog
*	Thu Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 4.11.0.1-1
-	Upgrade version
