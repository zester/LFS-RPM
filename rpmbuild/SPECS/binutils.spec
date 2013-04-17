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
rm -rf %{buildroot}
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
%{_bindir}/*
%{_libdir}/*
%{_includedir}*
%{_datarootdir}/locale/*
%{_mandir}/*/*
%changelog
*	Mon Apr  1 2013 baho-utot <baho-utot@columbus.rr.com> 2.23.1-1
-	Upgrade version

*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 2.23.1-1
-	Upgrade version
