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
	--prefix=/usr \
	--libexecdir=/usr/lib \
	--docdir=/usr/share/doc/%{name}-%{version} \
	--sysconfdir=/etc \
	--disable-setuid \
	--with-browser=/usr/bin/lynx \
	--with-vgrind=/usr/bin/vgrind \
	--with-grap=/usr/bin/grap
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
find %{buildroot}/usr/lib -name '*.la' -delete
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/etc/*
/usr/bin/*
/usr/sbin/*
/usr/lib/%{name}/*
/usr/lib/*
/usr/share/doc/%{name}-%{version}/*
/usr/share/man/*/*
/usr/share/locale/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:2.6.3-1
-	Upgrade version
