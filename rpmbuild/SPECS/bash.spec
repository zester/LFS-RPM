Summary:	Bourne-Again SHell
Name:		bash
Version:	4.2
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/bash/
Group:		System Environment/Shells
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://ftp.gnu.org/gnu/bash/%{name}-%{version}.tar.gz
Patch0:		http://www.linuxfromscratch.org/patches/lfs/7.3/bash-4.2-fixes-11.patch
Provides:	/bin/sh
Provides:	/bin/bash
%description
The package contains the Bourne-Again SHell
%prep
%setup -q
%patch0 -p1
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr \
	--bindir=/bin \
	--htmldir=/usr/share/doc/%{name}-%{version} \
	--without-bash-malloc \
	--with-installed-readline
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
%find_lang %{name}
rm -rf %{buildroot}/usr/share/info
%clean
rm -rf %{buildroot}
%files -f %{name}.lang
%defattr(-,root,root)
/bin/*
/usr/share/doc/%{name}-%{version}/*
/usr/share/man/*/*
%changelog
*	Wed Mar 21 2013 GangGreene <GangGreene@bildanet.com> 0:4.2-1
-	Upgrade version
