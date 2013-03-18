Summary:	Build tool
Name:		pkg-config
Version:	0.27
Release:	1
License:	GPLv2
URL:		http://www.freedesktop.org/wiki/Software/pkg-config
Group:		Development/Tools
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://pkgconfig.freedesktop.org/releases/%{name}-%{version}.tar.gz
%description
Contains a tool for passing the include path and/or library paths
to build tools during the configure and make file execution.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr \
	--docdir=/usr/share/doc/%{name}-%{version} \
	--disable-shared \
	--with-internal-glib
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
%check
#make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
/usr/bin/*
/usr/share/aclocal/*
/usr/share/doc/%{name}-%{version}/*
/usr/share/man/*/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:0.27-0
-	Initial build.	First version
