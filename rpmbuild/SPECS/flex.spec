Summary:	A utility for generating programs that recognize patterns in text
Name:		flex
Version:	2.5.37
Release:	1
License:	BSD
URL:		http://flex.sourceforge.net
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://prdownloads.sourceforge.net/flex/%{name}-%{version}.tar.bz2
Patch:		http://www.linuxfromscratch.org/patches/lfs/7.2/flex-2.5.37-bison-2.6.1-1.patch
%description
The Flex package contains a utility for generating programs
that recognize patterns in text.
%prep
%setup -q
%patch -p1
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr \
	--docdir=/usr/share/doc/%{name}-%{version \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
ln -sv libfl.a %{buildroot}/usr/lib/libl.a
install -vdm 755   %{buildroot}/usr/share/doc/%{name}
cp -v doc/flex.pdf %{buildroot}/usr/share/doc/%{name}
cat > %{buildroot}/usr/bin/lex <<- "EOF"
#!/bin/sh
# Begin /usr/bin/lex

	exec /usr/bin/flex -l "$@"

# End /usr/bin/lex
EOF
rm -rf %{buildroot}/usr/share/info
%find_lang %{name}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files -f %{name}.lang
%defattr(-,root,root)
/usr/bin/flex
/usr/bin/flex++
%attr(755,root,root) /usr/bin/lex
/usr/lib/*
/usr/include/*
/usr/share/doc/%{name}/*
/usr/share/man/*/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:2.5.37-0
-	Initial build.	First version
