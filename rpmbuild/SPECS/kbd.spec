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
	--prefix=/usr \
	--datadir=/lib/kbd \
	--disable-vlock
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/bin
install -vdm 755 %{buildroot}/usr/share/doc/%{name}-%{version}
install -vdm 755 %{buildroot}/etc/ld.so.conf.d
mv -v %{buildroot}/usr/bin/{kbd_mode,loadkeys,openvt,setfont} %{buildroot}/bin
cp -R -v doc/* %{buildroot}/usr/share/doc/%{name}-%{version}
cat > %{buildroot}/etc/ld.so.conf.d/kbd.conf <<- "EOF"
	/lib/kbd
EOF
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/etc/ld.so.conf.d/kbd.conf
/bin/*
/lib/kbd/*
/usr/bin/*
/usr/share/doc/%{name}-%{version}/*
/usr/share/man/*/*
%changelog
*	Wed Mar 21 2013 GangGreene <GangGreene@bildanet.com> 0:1.15.5-1
-	Upgrade version
