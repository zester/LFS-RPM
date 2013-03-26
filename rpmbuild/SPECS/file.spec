Summary:	Contains a utility for determining file types
Name:		file
Version:	5.13
Release:	1
License:	BSD
URL:		http://www.darwinsys.com/file
Group:		Applications/File
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		ftp://ftp.astron.com/pub/file/%{name}-%{version}.tar.gz
%description
The package contains a utility for determining the type of a
given file or files
%prep
%setup -q
%build
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
./configure --prefix=/usr
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
find %{buildroot}/usr/lib -name '*.la' -delete
find %{buildroot}/usr/lib -name '*.a' -delete
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/usr/bin/*
/usr/lib/*
/usr/include/*
/usr/share/man/*/*
/usr/share/misc/magic.mgc
%changelog
*	Wed Mar 21 2013 GangGreene <GangGreene@bildanet.com> 5.13-1
-	Upgrade version

*	Wed Mar 19 2013 GangGreene <GangGreene@bildanet.com> 5.12-1
-	Initial version
