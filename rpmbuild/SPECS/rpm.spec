Summary:	Package manager
Name:		rpm
Version:	4.10.3.1
Release:	1
License:	GPLv2
URL:		http://rpm.org
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://rpm.org/releases/rpm-4.10.x/%{name}-%{version}.tar.bz2
%description
RPM package manager
%prep
%setup -q
%build
#	LIBS=-'L/usr/lib' \
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	CPPFLAGS='-I/usr/include/nspr -I/usr/include/nss' \
	--prefix=/usr \
	--bindir=/usr/bin \
	--libdir=/usr/lib \
	--disable-static \
	--without-lua \
	--with-external-db
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
find %{buildroot}/usr/lib -name '*.a'  -delete
find %{buildroot}/usr/lib -name '*.la' -delete
%find_lang %{name}
# 	Fix macros and prefix
sed -i 's|optflags: i386 -O2 -g -march=i386 -mtune=i686|optflags: i386 -O2 -march=i486 -mtune=i686 -pipe|' %{buildroot}/usr/lib/rpm/rpmrc
sed -i 's|optflags: i486 -O2 -g -march=i486|optflags: i486 -O2 -march=i486 -mtune=i686 -pipe|' %{buildroot}/usr/lib/rpm/rpmrc
sed -i 's|optflags: i586 -O2 -g -march=i586|optflags: i586 -O2 -march=i586 -mtune=i686 -pipe|' %{buildroot}/usr/lib/rpm/rpmrc
sed -i 's|optflags: i686 -O2 -g -march=i686|optflags: i686 -O2 -march=i486 -mtune=i686 -pipe|' %{buildroot}/usr/lib/rpm/rpmrc
sed -i 's|optflags: x86_64 -O2 -g|optflags: x86_64 -O2 -march=x86_64 -mtune=generic -pipe|'    %{buildroot}/usr/lib/rpm/rpmrc
sed -i 's|optflags: athlon -O2 -g -march=athlon|optflags: athlon -O2 -march=athlon -mtune=generic -pipe|' %{buildroot}/usr/lib/rpm/rpmrc
sed -i 's|\${prefix}||' %{buildroot}/usr/lib/rpm/macros
%post -p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%clean
rm -rf %{buildroot}
%files -f %{name}.lang
%defattr(-,root,root)
/bin/*
/usr/bin/*
/usr/include/*
/usr/lib/%{name}/*
/usr/lib/*
/usr/share/man/*/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:4.10.3.1-1
-	Upgrade version
