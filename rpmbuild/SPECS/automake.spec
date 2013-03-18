Summary:	Programs for generating Makefiles
Name:		automake
Version:	1.12.3
Release:	1
License:	GPLv2
URL:		http://www.gnu.org/software/automake/
Group:		Development/Tools
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/automake/%{name}-%{version}.tar.xz
%description
Contains programs for generating Makefiles for use with Autoconf.
%prep
%setup -q
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
rm -rf %{buildroot}/usr/share/info
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
/usr/bin/*
/usr/share/aclocal/README
/usr/share/aclocal-1.12/*
/usr/share/doc/%{name}-%{version}/*
/usr/share/%{name}-1.12/*
/usr/share/man/man1/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 1.12.3-0
-	Initial build.	First version
