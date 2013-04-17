Summary:	Programs for finding and viewing man pages
Name:		man-db
Version:	2.6.3
Release:	1
License:	GPLv2
URL:		http://www.nongnu.org/man-db
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://download.savannah.gnu.org/releases/man-db/%{name}-%{version}.tar.xz
%description
The Man-DB package contains programs for finding and viewing man pages.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--docdir=%{_defaultdocdir}/%{name}-%{version} \
	--sysconfdir=/etc \
	--disable-setuid \
	--with-browser=%{_bindir}/lynx \
	--with-vgrind=%{_bindir}/vgrind \
	--with-grap=%{_bindir}/grap
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -name '*.la' -delete
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/etc/*
%{_bindir}*
%{_sbindir}/*
%{_libdir}/%{name}/*
%{_libdir}/*
%{_defaultdocdir}/%{name}-%{version}/*
%{_mandir}/*/*
%{_datarootdir}/locale/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:2.6.3-1
-	Upgrade version
