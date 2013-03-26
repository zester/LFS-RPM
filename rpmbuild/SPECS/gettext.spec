Summary:	Utilities for internationalization and localization
Name:		gettext
Version:	0.18.2
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/gettext
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/gettext/%{name}-%{version}.tar.gz
%description
These allow programs to be compiled with NLS
(Native Language Support), enabling them to output
messages in the user's native language.
%prep
%setup -q
sed -i -e '/gets is a/d' gettext-*/*/stdio.in.h
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr \
	--docdir=/usr/share/doc/%{name}-%{version}
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
find %{buildroot}/usr/lib -name '*.la' -delete
rm -rf %{buildroot}/usr/share/info
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/usr/bin/*
/usr/include/*
/usr/lib/*
/usr/share/aclocal/*
/usr/share/doc/%{name}-%{version}/*
/usr/share/%{name}/*
/usr/share/locale/*
/usr/share/man/*/*
%changelog
*	Wed Mar 21 2013 GangGreene <GangGreene@bildanet.com> 0:0.18.2-1
-	Upgrade version
