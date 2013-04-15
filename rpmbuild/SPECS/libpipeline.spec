Summary:	Library for manipulating pipelines
Name:		libpipeline
Version:	1.2.2
Release:	1
License:	GPLv3
URL:		http://libpipeline.nongnu.org
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		 http://download.savannah.gnu.org/releases/libpipeline/%{name}-%{version}.tar.gz
%description
Contains a library for manipulating pipelines of sub processes
in a flexible and convenient way.
%prep
%setup -q
sed -i -e '/gets is a/d' gnulib/lib/stdio.in.h
%build
PKG_CONFIG_PATH=/tools/lib/pkgconfig \
	./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
find %{buildroot}/ -name '*.la' -delete
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/usr/include/*
/usr/lib/*
/usr/share/man/*/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:1.2.2-1
-	Upgrade version
