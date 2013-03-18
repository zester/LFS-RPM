Summary:	The package automatically configure source code
Name:		autoconf
Version:	2.69
Release:	1
License:	GPLv2
URL:		http://www.gnu.org/software/autoconf
Group:		Development/Tools
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/autoconf/%{name}-%{version}.tar.xz
%description
The package contains programs for producing shell scripts that can
automatically configure source code.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr 
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/share/info
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
/usr/bin/*
/usr/share/man/man1/*
/usr/share/autoconf/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:2.69-0
-	Initial build.	First version
