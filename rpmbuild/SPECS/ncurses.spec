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
	--prefix=/usr \
	--mandir=/usr/share/man \
	--with-shared \
	--without-debug \
	--enable-widec \
	--enable-pc-files
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/lib/pkgconfig
mv -v %{buildroot}/usr/lib/libncursesw.so.5* %{buildroot}/lib
ln -sfv ../../lib/libncursesw.so.5 %{buildroot}/usr/lib/libncursesw.so
for lib in ncurses form panel menu ; do \
    rm -vf %{buildroot}/usr/lib/lib${lib}.so ; \
    echo "INPUT(-l${lib}w)" > %{buildroot}/usr/lib/lib${lib}.so ; \
    ln -sfv lib${lib}w.a %{buildroot}/usr/lib/lib${lib}.a ; \
    ln -sfv ${lib}w.pc %{buildroot}/usr/lib/pkgconfig/${lib}.pc
done
ln -sfv libncurses++w.a %{buildroot}/usr/lib/libncurses++.a
rm -vf %{buildroot}/usr/lib/libcursesw.so
echo "INPUT(-lncursesw)" > %{buildroot}/usr/lib/libcursesw.so
ln -sfv libncurses.so %{buildroot}/usr/lib/libcurses.so
ln -sfv libncursesw.a %{buildroot}/usr/lib/libcursesw.a
ln -sfv libncurses.a %{buildroot}/usr/lib/libcurses.a
install -vdm 755  %{buildroot}/usr/share/doc/%{name}-%{version}
cp -v -R doc/* %{buildroot}/usr/share/doc/%{name}-%{version}
#find %{buildroot}/usr/lib -name '*.a'  -delete
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/lib/*
/usr/bin/*
/usr/include/*
/usr/lib/*
/usr/share/doc/%{name}-%{version}/*
/usr/share/man/*/*
/usr/share/tabset/*
/usr/share/terminfo/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 0:5.9-0
-	Initial build.	First version
