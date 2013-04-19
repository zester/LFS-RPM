Summary:	Contains a parser generator
Name:		bison
Version:	2.7
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/bison
Group:		LFS/Base
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/bison/%{name}-%{version}.tar.xz
%description
This package contains a parser generator
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}
echo '#define YYENABLE_NLS 1' >> lib/config.h
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_infodir}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%files 
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_datarootdir}/%{name}/*
%{_datarootdir}/aclocal/*
%{_datarootdir}/locale/*
%{_mandir}/*/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:2.7-1
-	Upgrade version
