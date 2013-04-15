Summary:	Practical Extraction and Report Language
Name:		perl
Version:	5.16.3
Release:	1
License:	GPLv1
URL:		http://www.perl.org/
Group:		Development/Languages
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.cpan.org/src/5.0/%{name}-%{version}.tar.bz2
Provides:	perl
%description
The Perl package contains the Practical Extraction and
Report Language.
%prep
%setup -q
sed -i -e "s|BUILD_ZLIB\s*= True|BUILD_ZLIB = False|" \
	-e "s|INCLUDE\s*= ./zlib-src|INCLUDE    = /usr/include|" \
	-e "s|LIB\s*= ./zlib-src|LIB        = /usr/lib|" \
	cpan/Compress-Raw-Zlib/config.in
%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
sh Configure -des -Dprefix=/usr \
	-Dvendorprefix=/usr \
	-Dman1dir=/usr/share/man/man1 \
	-Dman3dir=/usr/share/man/man3 \
	-Dpager="/usr/bin/less -isR" \
	-Duseshrplib
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
chmod -R u+w %{buildroot}/usr/lib*
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/usr/bin/*
/usr/lib/*
/usr/share/man/*/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 5.16.3-1
-	Upgrade version 5.16.3
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:5.16.2-1
-	Upgrade version
