Summary:	Programs for monitoring processes
Name:		procps-ng
Version:	3.3.6
Release:	1
License:	GPLv2
URL:		http://procps.sourceforge.net/
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://procps.sourceforge.net/%{name}-%{version}.tar.xz
%description
The Procps package contains programs for monitoring processes.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr \
	--exec-prefix= \
	--libdir=/usr/lib \
	--docdir=/usr/share/doc/%{name}-%{version} \
	--disable-static \
	--disable-skill \
	--disable-kill
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/lib
mv -v %{buildroot}/usr/lib/libprocps.so.* %{buildroot}/lib
ln -sfv ../../lib/libprocps.so.1.1.0 %{buildroot}/usr/lib/libprocps.so
find %{buildroot}/usr/lib -name '*.la' -delete
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/bin/*
/sbin/*
/lib/*
/usr/bin/*
/usr/include/*
/usr/lib/*
/usr/share/doc/*
/usr/share/man/*/*
%changelog
*	Wed Mar 21 2013 GangGreene <GangGreene@bildanet.com> 0:3.3.6-1
-	Upgrade version
