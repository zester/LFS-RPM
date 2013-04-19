Summary:	Contains the GNU compiler collection
Name:		gcc
Version:	4.8.0
Release:	1
License:	GPLv2
URL:		http://gcc.gnu.org
Group:		Development/Tools
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/gcc/%{name}-%{version}/%{name}-%{version}.tar.bz2
%description
The GCC package contains the GNU compiler collection,
which includes the C and C++ compilers.
%prep
%setup -q
case `uname -m` in
	i?86) sed -i 's/^T_CFLAGS =$/& -fomit-frame-pointer/' gcc/Makefile.in ;;
esac
sed -i 's/install_to_$(INSTALL_DEST) //' libiberty/Makefile.in
sed -i -e /autogen/d -e /check.sh/d fixincludes/Makefile.in
mv -v libmudflap/testsuite/libmudflap.c++/pass41-frag.cxx{,.disable}
#sed -i 's/BUILD_INFO=info/BUILD_INFO=/' gcc/configure
install -vdm 755 ../gcc-build
%build
cd ../gcc-build
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
../%{name}-%{version}/configure \
	--prefix=%{_prefix} \
	--libexecdir=%{_libexecdir} \
	--enable-shared \
	--enable-threads=posix \
	--enable-__cxa_atexit \
	--enable-clocale=gnu \
	--enable-languages=c,c++ \
	--disable-multilib \
	--disable-bootstrap \
	--disable-install-libiberty \
	--with-system-zlib
make %{?_smp_mflags}
%install
rm -rf %{buildroot}/*
cd ../gcc-build
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/lib
ln -sv ../usr/bin/cpp %{buildroot}/lib
ln -sv gcc %{buildroot}/usr/bin/cc
install -vdm 755 %{buildroot}%{_datarootdir}/gdb/auto-load/usr/lib
mv -v %{buildroot}/usr/lib/*gdb.py %{buildroot}%{_datarootdir}/gdb/auto-load/usr/lib
find %{buildroot}%{_libdir} -name '*.la' -delete
rm -rf %{buildroot}%{_infodir}
%check
cd ../gcc-build
ulimit -s 32768
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/lib/cpp
%{_bindir}/*
%{_libdir}/*
%{_libexecdir}/*
%{_includedir}/*
%{_datarootdir}/%{name}-%{version}/*
%{_datarootdir}/gdb/auto-load/usr/lib/libstdc++.so.6.0.18-gdb.py
%{_datarootdir}/locale/*
%{_mandir}/*/*
%changelog
*	Mon Apr  1 2013 baho-utot <baho-utot@columbus.rr.com> 4.8.0-1
-	Upgrade version 4.8.0

*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:4.7.2-1
-	Upgrade version
