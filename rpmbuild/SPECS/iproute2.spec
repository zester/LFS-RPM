Summary:	Basic and advanced IPV4-based networking
Name:		iproute2
Version:	3.8.0
Release:	1
License:	GPLv2
URL:		http://www.kernel.org/pub/linux/utils/net/iproute2
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.kernel.org/pub/linux/utils/net/iproute2/%{name}-%{version}.tar.xz
%description
The IPRoute2 package contains programs for basic and advanced
IPV4-based networking.
%prep
%setup -q
sed -i '/^TARGETS/s@arpd@@g' misc/Makefile
sed -i /ARPD/d Makefile
sed -i 's/arpd.8//' man/man8/Makefile
sed -i 's/-Werror//' Makefile
%build
export CFLAGS="%{optflags}"
sed -i "s/CCOPTS = -O2/CCOPTS = %{optflags}/" Makefile
make %{?_smp_mflags} DESTDIR=
%install
rm -rf %{buildroot}
make	DESTDIR=%{buildroot} \
	MANDIR=/usr/share/man \
	DOCDIR=/usr/share/doc/%{name}-%{version} install
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/etc/%{name}/*
/sbin/*
/usr/lib/*
/usr/share/doc/%{name}-%{version}/*
/usr/share/man/*/*
%changelog
*	Wed Mar 21 2013 GangGreene <GangGreene@bildanet.com> 0:3.8.0-1
-	Upgrade version
