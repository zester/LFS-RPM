Summary:	Contains a parser generator
Name:		bison
Version:	2.7.1
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
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
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
%lang(ast) %{_datarootdir}/locale/ast/LC_MESSAGES/bison-runtime.mo
%lang(da) %{_datarootdir}/locale/da/LC_MESSAGES/bison-runtime.mo
%lang(da) %{_datarootdir}/locale/da/LC_MESSAGES/bison.mo
%lang(de) %{_datarootdir}/locale/de/LC_MESSAGES/bison-runtime.mo
%lang(de) %{_datarootdir}/locale/de/LC_MESSAGES/bison.mo
%lang(el) %{_datarootdir}/locale/el/LC_MESSAGES/bison-runtime.mo
%lang(el) %{_datarootdir}/locale/el/LC_MESSAGES/bison.mo
%lang(eo) %{_datarootdir}/locale/eo/LC_MESSAGES/bison-runtime.mo
%lang(eo) %{_datarootdir}/locale/eo/LC_MESSAGES/bison.mo
%lang(es) %{_datarootdir}/locale/es/LC_MESSAGES/bison-runtime.mo
%lang(es) %{_datarootdir}/locale/es/LC_MESSAGES/bison.mo
%lang(et) %{_datarootdir}/locale/et/LC_MESSAGES/bison-runtime.mo
%lang(et) %{_datarootdir}/locale/et/LC_MESSAGES/bison.mo
%lang(fi) %{_datarootdir}/locale/fi/LC_MESSAGES/bison-runtime.mo
%lang(fi) %{_datarootdir}/locale/fi/LC_MESSAGES/bison.mo
%lang(fr) %{_datarootdir}/locale/fr/LC_MESSAGES/bison-runtime.mo
%lang(fr) %{_datarootdir}/locale/fr/LC_MESSAGES/bison.mo
%lang(ga) %{_datarootdir}/locale/ga/LC_MESSAGES/bison-runtime.mo
%lang(ga) %{_datarootdir}/locale/ga/LC_MESSAGES/bison.mo
%lang(gl) %{_datarootdir}/locale/gl/LC_MESSAGES/bison-runtime.mo
%lang(hr) %{_datarootdir}/locale/hr/LC_MESSAGES/bison-runtime.mo
%lang(hr) %{_datarootdir}/locale/hr/LC_MESSAGES/bison.mo
%lang(hu) %{_datarootdir}/locale/hu/LC_MESSAGES/bison-runtime.mo
%lang(id) %{_datarootdir}/locale/id/LC_MESSAGES/bison-runtime.mo
%lang(id) %{_datarootdir}/locale/id/LC_MESSAGES/bison.mo
%lang(it) %{_datarootdir}/locale/it/LC_MESSAGES/bison-runtime.mo
%lang(it) %{_datarootdir}/locale/it/LC_MESSAGES/bison.mo
%lang(ja) %{_datarootdir}/locale/ja/LC_MESSAGES/bison-runtime.mo
%lang(ja) %{_datarootdir}/locale/ja/LC_MESSAGES/bison.mo
%lang(ky) %{_datarootdir}/locale/ky/LC_MESSAGES/bison-runtime.mo
%lang(lt) %{_datarootdir}/locale/lt/LC_MESSAGES/bison-runtime.mo
%lang(lv) %{_datarootdir}/locale/lv/LC_MESSAGES/bison-runtime.mo
%lang(ms) %{_datarootdir}/locale/ms/LC_MESSAGES/bison-runtime.mo
%lang(ms) %{_datarootdir}/locale/ms/LC_MESSAGES/bison.mo
%lang(nb) %{_datarootdir}/locale/nb/LC_MESSAGES/bison-runtime.mo
%lang(nb) %{_datarootdir}/locale/nb/LC_MESSAGES/bison.mo
%lang(nl) %{_datarootdir}/locale/nl/LC_MESSAGES/bison-runtime.mo
%lang(nl) %{_datarootdir}/locale/nl/LC_MESSAGES/bison.mo
%lang(pl) %{_datarootdir}/locale/pl/LC_MESSAGES/bison-runtime.mo
%lang(pl) %{_datarootdir}/locale/pl/LC_MESSAGES/bison.mo
%lang(pt) %{_datarootdir}/locale/pt/LC_MESSAGES/bison-runtime.mo
%lang(pt) %{_datarootdir}/locale/pt/LC_MESSAGES/bison.mo
%lang(pt_BR) %{_datarootdir}/locale/pt_BR/LC_MESSAGES/bison-runtime.mo
%lang(pt_BR) %{_datarootdir}/locale/pt_BR/LC_MESSAGES/bison.mo
%lang(ro) %{_datarootdir}/locale/ro/LC_MESSAGES/bison-runtime.mo
%lang(ro) %{_datarootdir}/locale/ro/LC_MESSAGES/bison.mo
%lang(ru) %{_datarootdir}/locale/ru/LC_MESSAGES/bison-runtime.mo
%lang(ru) %{_datarootdir}/locale/ru/LC_MESSAGES/bison.mo
%lang(sl) %{_datarootdir}/locale/sl/LC_MESSAGES/bison-runtime.mo
%lang(sq) %{_datarootdir}/locale/sq/LC_MESSAGES/bison-runtime.mo
%lang(sr) %{_datarootdir}/locale/sr/LC_MESSAGES/bison-runtime.mo
%lang(sr) %{_datarootdir}/locale/sr/LC_MESSAGES/bison.mo
%lang(sv) %{_datarootdir}/locale/sv/LC_MESSAGES/bison-runtime.mo
%lang(sv) %{_datarootdir}/locale/sv/LC_MESSAGES/bison.mo
%lang(th) %{_datarootdir}/locale/th/LC_MESSAGES/bison-runtime.mo
%lang(tr) %{_datarootdir}/locale/tr/LC_MESSAGES/bison-runtime.mo
%lang(tr) %{_datarootdir}/locale/tr/LC_MESSAGES/bison.mo
%lang(uk) %{_datarootdir}/locale/uk/LC_MESSAGES/bison-runtime.mo
%lang(uk) %{_datarootdir}/locale/uk/LC_MESSAGES/bison.mo
%lang(vi) %{_datarootdir}/locale/vi/LC_MESSAGES/bison-runtime.mo
%lang(vi) %{_datarootdir}/locale/vi/LC_MESSAGES/bison.mo
%lang(zh_CN) %{_datarootdir}/locale/zh_CN/LC_MESSAGES/bison-runtime.mo
%lang(zh_CN) %{_datarootdir}/locale/zh_CN/LC_MESSAGES/bison.mo
%lang(zh_TW) %{_datarootdir}/locale/zh_TW/LC_MESSAGES/bison-runtime.mo
%lang(zh_TW) %{_datarootdir}/locale/zh_TW/LC_MESSAGES/bison.mo
%{_mandir}/*/*
%changelog
*	Fri May 10 2013 baho-utot <baho-utot@columbus.rr.com> 2.7.1-1
-	Update version to 2.7.2
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 2.7-1
-	Upgrade version
