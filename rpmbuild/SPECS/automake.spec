Summary:	Programs for generating Makefiles
Name:		automake
Version:	1.13.1
Release:	1
License:	GPLv2
URL:		http://www.gnu.org/software/automake/
Group:		LFS/Base
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/automake/%{name}-%{version}.tar.xz
%description
Contains programs for generating Makefiles for use with Autoconf.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--docdir=%{_defaultdocdir}/%{name}-%{version}
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_infodir}
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datarootdir}/aclocal/README
%{_datarootdir}/%{name}-1.13/*
%{_datarootdir}/aclocal-1.13/*
%{_defaultdocdir}/%{name}-%{version}/*
%{_mandir}/man1/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:1.13.1-1
-	Upgrade version
