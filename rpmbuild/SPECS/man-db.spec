Summary:	Programs for finding and viewing man pages
Name:		man-db
Version:	2.6.3
Release:	1
License:	GPLv2
URL:		http://www.nongnu.org/man-db
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://download.savannah.gnu.org/releases/man-db/%{name}-%{version}.tar.xz
%description
The Man-DB package contains programs for finding and viewing man pages.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--docdir=%{_defaultdocdir}/%{name}-%{version} \
	--sysconfdir=/etc \
	--disable-setuid \
	--with-browser=%{_bindir}/lynx \
	--with-vgrind=%{_bindir}/vgrind \
	--with-grap=%{_bindir}/grap
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -name '*.la' -delete
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%config() /etc/man_db.conf
%{_bindir}/*
%{_sbindir}/*
%{_libexecdir}/*
%{_libdir}/*
%{_defaultdocdir}/%{name}-%{version}/*
%{_mandir}/*/*
%lang(af) %{_datarootdir}/locale/af/LC_MESSAGES/man-db-gnulib.mo
%lang(be) %{_datarootdir}/locale/be/LC_MESSAGES/man-db-gnulib.mo
%lang(bg) %{_datarootdir}/locale/bg/LC_MESSAGES/man-db-gnulib.mo
%lang(ca) %{_datarootdir}/locale/ca/LC_MESSAGES/man-db-gnulib.mo
%lang(ca) %{_datarootdir}/locale/ca/LC_MESSAGES/man-db.mo
%lang(cs) %{_datarootdir}/locale/cs/LC_MESSAGES/man-db-gnulib.mo
%lang(cs) %{_datarootdir}/locale/cs/LC_MESSAGES/man-db.mo
%lang(da) %{_datarootdir}/locale/da/LC_MESSAGES/man-db-gnulib.mo
%lang(da) %{_datarootdir}/locale/da/LC_MESSAGES/man-db.mo
%lang(de) %{_datarootdir}/locale/de/LC_MESSAGES/man-db-gnulib.mo
%lang(de) %{_datarootdir}/locale/de/LC_MESSAGES/man-db.mo
%lang(el) %{_datarootdir}/locale/el/LC_MESSAGES/man-db-gnulib.mo
%lang(es) %{_datarootdir}/locale/es/LC_MESSAGES/man-db-gnulib.mo
%lang(es) %{_datarootdir}/locale/es/LC_MESSAGES/man-db.mo
%lang(et) %{_datarootdir}/locale/et/LC_MESSAGES/man-db-gnulib.mo
%lang(eu) %{_datarootdir}/locale/eu/LC_MESSAGES/man-db-gnulib.mo
%lang(fi) %{_datarootdir}/locale/fi/LC_MESSAGES/man-db-gnulib.mo
%lang(fi) %{_datarootdir}/locale/fi/LC_MESSAGES/man-db.mo
%lang(fr) %{_datarootdir}/locale/fr/LC_MESSAGES/man-db-gnulib.mo
%lang(fr) %{_datarootdir}/locale/fr/LC_MESSAGES/man-db.mo
%lang(ga) %{_datarootdir}/locale/ga/LC_MESSAGES/man-db-gnulib.mo
%lang(gl) %{_datarootdir}/locale/gl/LC_MESSAGES/man-db-gnulib.mo
%lang(hu) %{_datarootdir}/locale/hu/LC_MESSAGES/man-db-gnulib.mo
%lang(id) %{_datarootdir}/locale/id/LC_MESSAGES/man-db.mo
%lang(it) %{_datarootdir}/locale/it/LC_MESSAGES/man-db-gnulib.mo
%lang(it) %{_datarootdir}/locale/it/LC_MESSAGES/man-db.mo
%lang(ja) %{_datarootdir}/locale/ja/LC_MESSAGES/man-db-gnulib.mo
%lang(ja) %{_datarootdir}/locale/ja/LC_MESSAGES/man-db.mo
%lang(ko) %{_datarootdir}/locale/ko/LC_MESSAGES/man-db-gnulib.mo
%lang(ms) %{_datarootdir}/locale/ms/LC_MESSAGES/man-db-gnulib.mo
%lang(nb) %{_datarootdir}/locale/nb/LC_MESSAGES/man-db-gnulib.mo
%lang(nl) %{_datarootdir}/locale/nl/LC_MESSAGES/man-db-gnulib.mo
%lang(nl) %{_datarootdir}/locale/nl/LC_MESSAGES/man-db.mo
%lang(pl) %{_datarootdir}/locale/pl/LC_MESSAGES/man-db-gnulib.mo
%lang(pl) %{_datarootdir}/locale/pl/LC_MESSAGES/man-db.mo
%lang(pt) %{_datarootdir}/locale/pt/LC_MESSAGES/man-db-gnulib.mo
%lang(pt) %{_datarootdir}/locale/pt_BR/LC_MESSAGES/man-db-gnulib.mo
%lang(pt_BR) %{_datarootdir}/locale/pt_BR/LC_MESSAGES/man-db.mo
%lang(ro) %{_datarootdir}/locale/ro/LC_MESSAGES/man-db-gnulib.mo
%lang(ro) %{_datarootdir}/locale/ro/LC_MESSAGES/man-db.mo
%lang(ru) %{_datarootdir}/locale/ru/LC_MESSAGES/man-db-gnulib.mo
%lang(ru) %{_datarootdir}/locale/ru/LC_MESSAGES/man-db.mo
%lang(rw) %{_datarootdir}/locale/rw/LC_MESSAGES/man-db-gnulib.mo
%lang(sk) %{_datarootdir}/locale/sk/LC_MESSAGES/man-db-gnulib.mo
%lang(sl) %{_datarootdir}/locale/sl/LC_MESSAGES/man-db-gnulib.mo
%lang(sv) %{_datarootdir}/locale/sv/LC_MESSAGES/man-db-gnulib.mo
%lang(sv) %{_datarootdir}/locale/sv/LC_MESSAGES/man-db.mo
%lang(tr) %{_datarootdir}/locale/tr/LC_MESSAGES/man-db-gnulib.mo
%lang(uk) %{_datarootdir}/locale/uk/LC_MESSAGES/man-db-gnulib.mo
%lang(vi) %{_datarootdir}/locale/vi/LC_MESSAGES/man-db-gnulib.mo
%lang(vi) %{_datarootdir}/locale/vi/LC_MESSAGES/man-db.mo
%lang(zh_CN) %{_datarootdir}/locale/zh_CN/LC_MESSAGES/man-db-gnulib.mo
%lang(zh_CN) %{_datarootdir}/locale/zh_CN/LC_MESSAGES/man-db.mo
%lang(zh_TW) %{_datarootdir}/locale/zh_TW/LC_MESSAGES/man-db-gnulib.mo
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 2.6.3-1
-	Upgrade version
