Summary:	Contains a linker, an assembler, and other tools
Name:		binutils
Version:	2.23.2
Release:	1
License:	GPLv2
URL:		http://www.gnu.org/software/binutils
Group:		LFS/Base
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://ftp.gnu.org/gnu/binutils/%{name}-%{version}.tar.bz2
%description
The Binutils package contains a linker, an assembler,
and other tools for handling object files.
%prep
%setup -q
rm -fv etc/standards.info
sed -i.bak '/^INFO/s/standards.info //' etc/Makefile.in
sed -i -e 's/@colophon/@@colophon/' \
       -e 's/doc@cygnus.com/doc@@cygnus.com/' bfd/doc/bfd.texinfo
%build
install -vdm 755 ../binutils-build
cd ../binutils-build
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
../%{name}-%{version}/configure \
	--prefix=%{_prefix} \
	--enable-shared
make %{?_smp_mflags} tooldir=/usr
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd ../binutils-build
make DESTDIR=%{buildroot} tooldir=%{_usr} install
cp -v ../%{name}-%{version}/include/libiberty.h %{buildroot}/%{_includedir}
find %{buildroot} -name '*.la' -delete
# Don't remove libiberity.a
rm -rf %{buildroot}/%{_infodir}
%check
cd ../binutils-build
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}/*
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
#	Executables
%{_bindir}/addr2line
%{_bindir}/ar
%{_bindir}/as
%{_bindir}/c++filt
%{_bindir}/elfedit
%{_bindir}/gprof
%{_bindir}/ld
%{_bindir}/ld.bfd
%{_bindir}/nm
%{_bindir}/objcopy
%{_bindir}/objdump
%{_bindir}/ranlib
%{_bindir}/readelf
%{_bindir}/size
%{_bindir}/strings
%{_bindir}/strip
#	Includes
%{_includedir}/*.h
#	Libraries
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/ldscripts/*
#	Internationalization
%lang(bg)%{_datarootdir}/locale/bg/LC_MESSAGES/*.mo
%lang(da)%{_datarootdir}/locale/da/LC_MESSAGES/*.mo
%lang(de)%{_datarootdir}/locale/de/LC_MESSAGES/*.mo
%lang(eo)%{_datarootdir}/locale/eo/LC_MESSAGES/*.mo
%lang(es)%{_datarootdir}/locale/es/LC_MESSAGES/*.mo
%lang(fi)%{_datarootdir}/locale/fi/LC_MESSAGES/*.mo
%lang(fr)%{_datarootdir}/locale/fr/LC_MESSAGES/*.mo
%lang(ga)%{_datarootdir}/locale/ga/LC_MESSAGES/*.mo
%lang(id)%{_datarootdir}/locale/id/LC_MESSAGES/*.mo
%lang(it)%{_datarootdir}/locale/it/LC_MESSAGES/*.mo
%lang(ja)%{_datarootdir}/locale/ja/LC_MESSAGES/*.mo
%lang(ms)%{_datarootdir}/locale/ms/LC_MESSAGES/*.mo
%lang(nl)%{_datarootdir}/locale/nl/LC_MESSAGES/*.mo
%lang(pt_BR)%{_datarootdir}/locale/pt_BR/LC_MESSAGES/*.mo
%lang(ro)%{_datarootdir}/locale/ro/LC_MESSAGES/*.mo
%lang(ru)%{_datarootdir}/locale/ru/LC_MESSAGES/*.mo
%lang(rw)%{_datarootdir}/locale/rw/LC_MESSAGES/*.mo
%lang(sk)%{_datarootdir}/locale/sk/LC_MESSAGES/*.mo
%lang(sr)%{_datarootdir}/locale/sr/LC_MESSAGES/*.mo
%lang(sv)%{_datarootdir}/locale/sv/LC_MESSAGES/*.mo
%lang(tr)%{_datarootdir}/locale/tr/LC_MESSAGES/*.mo
%lang(uk)%{_datarootdir}/locale/uk/LC_MESSAGES/*.mo
%lang(vi)%{_datarootdir}/locale/vi/LC_MESSAGES/*.mo
%lang(zh_CN)%{_datarootdir}/locale/zh_CN/LC_MESSAGES/*.mo
%lang(zh_TW)%{_datarootdir}/locale/zh_TW/LC_MESSAGES/*.mo
#	Manpages
%{_mandir}/man1/*.gz
%changelog
*	Mon Apr 01 2013 baho-utot <baho-utot@columbus.rr.com> 2.23.2-1
-	Upgrade version
