Summary:	Build tool
Name:		pkg-config
Version:	0.28
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
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--with-internal-glib \
	--disable-host-tool \
	--docdir=%{_defaultdocdir}/%{name}-%{version} \
	--disable-shared
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}/*
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datarootdir}/aclocal/*
%{_defaultdocdir}/%{name}-%{version}/*
%{_mandir}/*/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0.28-1
-	Upgrade version
