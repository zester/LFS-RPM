Summary:	Contains a linker, an assembler, and other tools
Name:		binutils
Version:	2.22
Release:	1
License:	GPLv2
URL:		http://www.gnu.org/software/binutils
Group:		System Environment/Base
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://ftp.gnu.org/gnu/binutils/%{name}-%{version}.tar.bz2
Patch0:		http://www.linuxfromscratch.org/patches/lfs/7.2/binutils-2.22-build_fix-1.patch
%description
The Binutils package contains a linker, an assembler,
and other tools for handling object files.
%prep
%setup -q
%patch0 -p1
rm -fv etc/standards.info
sed -i.bak '/^INFO/s/standards.info //' etc/Makefile.in
%build
install -vdm 755 binutils-build
cd binutils-build
../configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr \
	--enable-shared
make %{?_smp_mflags} tooldir=/usr
%install
rm -rf %{buildroot}
cd binutils-build
make DESTDIR=%{buildroot} tooldir=/usr install
cp -v ../include/libiberty.h %{buildroot}/usr/include
find %{buildroot}/usr/lib -name '*.la' -delete
find %{buildroot}/usr/lib -name '*.a' -delete
rm -rf %{buildroot}/usr/share/info
%check
cd binutils-build
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/usr/bin/*
/usr/lib
/usr/include/*
/usr/share/locale/*
/usr/share/man/*/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:2.22-0
-	Initial build.	First version
