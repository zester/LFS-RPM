Summary:	Man pages
Name:		man-pages
Version:	3.47
Release:	1
License:	GPL
URL:		http://www.kernel.org/doc/man-pages
Group:		System Environment/Base
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.kernel.org/pub/linux/docs/man-pages/%{name}-%{version}.tar.xz
BuildArch: 	noarch
%description
The Man-pages package contains over 1,900 man pages.
%prep
%setup -q
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/share/man/man3/getspnam.3
rm %{buildroot}/usr/share/man/man5/passwd.5
%clean
rm -rf %{buildroot} %{_builddir}/*
%files
%defattr(-,root,root)
/usr/share/man/*/*
%changelog
*	Sun Mar 24 2013 GangGreene <GangGreene@bildanet.com> 3.47-1
-	Update version

*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 3.42-1
-	Initial build.	First version


