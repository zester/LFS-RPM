Summary:	Libraries for terminal handling of character screens
Name:		ncurses
Version:	5.9
Release:	1
License:	GPLv2
URL:		http://www.gnu.org/software/ncurses
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		ftp://ftp.gnu.org/gnu/ncurses/%{name}-%{version}.tar.gz
%description
The Ncurses package contains libraries for terminal-independent
handling of character screens.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--with-shared \
	--without-debug \
	--enable-widec \
	--enable-pc-files
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}%{_libdir}/pkgconfig
install -vdm 755 %{buildroot}/%{_lib}
mv -v %{buildroot}%{_libdir}/libncursesw.so.5* %{buildroot}/%{_lib}
ln -sfv ../../lib/libncursesw.so.5 %{buildroot}%{_libdir}/libncursesw.so
for lib in ncurses form panel menu ; do \
    rm -vf %{buildroot}%{_libdir}/lib${lib}.so ; \
    echo "INPUT(-l${lib}w)" > %{buildroot}%{_libdir}/lib${lib}.so ; \
    ln -sfv lib${lib}w.a %{buildroot}%{_libdir}/lib${lib}.a ; \
    ln -sfv ${lib}w.pc %{buildroot}%{_libdir}/pkgconfig/${lib}.pc
done
ln -sfv libncurses++w.a %{buildroot}%{_libdir}/libncurses++.a
rm -vf %{buildroot}%{_libdir}/libcursesw.so
echo "INPUT(-lncursesw)" > %{buildroot}%{_libdir}/libcursesw.so
ln -sfv libncurses.so %{buildroot}%{_libdir}/libcurses.so
ln -sfv libncursesw.a %{buildroot}%{_libdir}/libcursesw.a
ln -sfv libncurses.a %{buildroot}%{_libdir}/libcurses.a
install -vdm 755  %{buildroot}%{_defaultdocdir}/%{name}-%{version}
cp -v -R doc/* %{buildroot}%{_defaultdocdir}/%{name}-%{version}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/lib/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_defaultdocdir}/%{name}-%{version}/*
%{_mandir}/*/*
%{_datarootdir}/tabset/*
%{_datarootdir}/terminfo/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 5.9-1
-	Initial build.	First version
