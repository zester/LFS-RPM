Summary:	Reading, writing, and converting info pages
Name:		texinfo
Version:	5.1
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/texinfo/
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://ftp.gnu.org/gnu/texinfo/%{name}-%{version}.tar.xz
%description
The Texinfo package contains programs for reading, writing,
and converting info pages.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} TEXMF=%{_datarootdir}/texmf install-tex
rm -rf %{buildroot}%{_infodir}
%find_lang %{name}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datarootdir}/locale/*
%{_mandir}/*/*
%{_datarootdir}/texinfo
%{_datarootdir}/texmf
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:5.0-1
-	Upgrade version
