Summary:	Programs for monitoring processes
Name:		procps-ng
Version:	3.3.7
Release:	1
License:	GPLv2
URL:		http://procps.sourceforge.net/
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://sourceforge.net/projects/procps-ng/files/Production/%{name}-%{version}.tar.xz
%description
The Procps package contains programs for monitoring processes.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--exec-prefix= \
	--libdir=%{_libdir} \
	--docdir=%{_defaultdocdir}/%{name}-%{version} \
	--disable-static \
	--disable-skill \
	--disable-kill
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/lib
mv -v %{buildroot}%{_libdir}/libprocps.so.* %{buildroot}/lib
ln -sfv ../../lib/libprocps.so.1.1.0 %{buildroot}%{_libdir}/libprocps.so
find %{buildroot}%{_libdir} -name '*.la' -delete
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/bin/*
/sbin/*
/lib/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_defaultdocdir}/*
%{_mandir}/*/*
%changelog
*	Mon Apr  1 2013 baho-utot <baho-utot@columbus.rr.com> 0:3.3.6-1
-	Upgrade version

*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:3.3.6-1
-	Upgrade version
