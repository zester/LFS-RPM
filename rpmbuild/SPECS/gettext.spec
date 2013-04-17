Summary:	Utilities for internationalization and localization
Name:		gettext
Version:	0.18.2
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/gettext
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/gettext/%{name}-%{version}.tar.gz
%description
These allow programs to be compiled with NLS
(Native Language Support), enabling them to output
messages in the user's native language.
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
find %{buildroot}%{_libdir} -name '*.la' -delete
rm -rf %{buildroot}%{_infodir}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datarootdir}/aclocal/*
%{_defaultdocdir}/%{name}-%{version}/*
%{_datarootdir}/%{name}/*
%{_datarootdir}/locale/*
%{_mandir}/*/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:0.18.2-1
-	Upgrade version
