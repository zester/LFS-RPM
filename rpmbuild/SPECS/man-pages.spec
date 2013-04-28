Summary:	Man pages
Name:		man-pages
Version:	3.50
Release:	1
License:	GPLv2
URL:		http://www.kernel.org/doc/man-pages
Group:		System Environment/Base
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.kernel.org/pub/linux/docs/man-pages/%{name}-%{version}.tar.xz
BuildArch:	noarch
%description
The Man-pages package contains over 1,900 man pages.
%prep
%setup -q
%build
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -vf %{buildroot}%{_mandir}/man3/getspnam.3
rm -vf %{buildroot}%{_mandir}/man5/passwd.5
%clean
rm -rf %{buildroot} %{_builddir}/*
%files
%defattr(-,root,root)
%{_mandir}/*/*
%changelog
*	Sun Mar 24 2013 baho-utot <baho-utot@columbus.rr.com> 3.50-1
-	Update version to 3.50

*	Sun Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 3.47-1
-	Update version

*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 3.42-1
-	Initial build.	First version


