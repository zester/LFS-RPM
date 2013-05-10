Summary:	Key table files, console fonts, and keyboard utilities
Name:		kbd
Version:	1.15.5
Release:	1
License:	GPLv2
URL:		http://ftp.altlinux.org/pub/people/legion/kbd
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.altlinux.org/pub/people/legion/kbd/%{name}-%{version}.tar.gz
Patch0:		kbd-1.15.5-backspace-1.patch
%description
The Kbd package contains key-table files, console fonts, and keyboard utilities.
%prep
%setup -q
%patch0 -p1
sed -i -e '326 s/if/while/' src/loadkeys.analyze.l
sed -i 's/\(RESIZECONS_PROGS=\)yes/\1no/g' configure
sed -i 's/resizecons.8 //' man/man8/Makefile.in
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--disable-vlock
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/bin
install -vdm 755 %{buildroot}%{_defaultdocdir}/%{name}-%{version}
install -vdm 755 %{buildroot}/etc/ld.so.conf.d
cp -R -v doc/* %{buildroot}%{_defaultdocdir}/%{name}-%{version}
rm -rf %{buildroot}/usr/share/locale/gr
%find_lang %{name}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_defaultdocdir}/%{name}-%{version}/*
%{_datarootdir}/consolefonts/*
%{_datarootdir}/consoletrans/*
%{_datarootdir}/keymaps/*
%{_datarootdir}/unimaps/*
%{_mandir}/*/*
%changelog
*	Thu Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 1.15.5-1
-	Upgrade version
