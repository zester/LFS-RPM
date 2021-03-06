Summary:	Programs that show the differences between files or directories
Name:		diffutils
Version:	3.3
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/diffutils
Group:		LFS/Base
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/diffutils/%{name}-%{version}.tar.xz
%description
The Diffutils package contains programs that show the
differences between files or directories.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_infodir}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%changelog
*	Mon Apr 01 2013 baho-utot <baho-utot@columbus.rr.com> 3.3-1
-	Initial build.	First version

*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 2.6.1-1
-	Initial build.	First version
