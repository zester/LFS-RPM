Summary:	Controls the start up, running and shutdown of the system
Name:		sysvinit
Version:	2.88dsf
Release:	1
License:	GPLv2
URL:		http://savannah.nongnu.org/projects/sysvinit
Group:		System Environment/Daemons
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://download.savannah.gnu.org/releases/sysvinit/%{name}-%{version}.tar.bz2
%description
Contains programs for controlling the start up, running and
shutdown of the system
%prep
%setup -q
sed -i 's@Sending processes@& configured via /etc/inittab@g' src/init.c
sed -i -e '/mountpoint/d' \
       -e '/utmpdump/d' src/Makefile
%build
make %{?_smp_mflags} CC="%{__cc}" CFLAGS="%{optflags} -D_GNU_SOURCE" LDFLAGS="-lcrypt" -C src
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make -C src ROOT=%{buildroot} \
	MANDIR=/usr/share/man \
	STRIP=/bin/true \
	BIN_OWNER=`id -nu` BIN_GROUP=`id -ng` install
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/bin/*
/sbin/*
/usr/include/*
/usr/bin/*
/usr/share/man/*/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 2.88dsf-1
-	Initial build.	First version
