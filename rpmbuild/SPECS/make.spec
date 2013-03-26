Summary:	Program for compiling packages
Name:		make
Version:	3.82
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/make
Group:		Development/Tools
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/make/%{name}-%{version}.tar.bz2
Patch:		http://www.linuxfromscratch.org/patches/lfs/7.2/make-3.82-upstream_fixes-3.patch
%description
The Make package contains a program for compiling packages.
%prep
%setup -q
%patch	-p1
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
%find_lang %{name}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%files -f %{name}.lang
%defattr(-,root,root)
/usr/bin/*
/usr/share/man/*/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:3.82-0
-	Initial build.	First version
