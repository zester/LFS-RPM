Summary:	Programs that show the differences between files or directories
Name:		diffutils
Version:	3.3
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/diffutils
Group:		Applications/File
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
	--prefix=/usr 
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/share/info
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
/usr/bin/*
/usr/share/man/*
%changelog
*	Mon Apr  1 2013 baho-utot <baho-utot@columbus.rr.com> 0:2.6.1-0
-	Initial build.	First version

*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 0:2.6.1-0
-	Initial build.	First version
