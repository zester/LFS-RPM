Summary:	Program for modifying or creating files
Name:		patch
Version:	2.7.1
Release:	1
License:	GPLv3
URL:		http://savannah.gnu.org/projects/patch
Source		http://ftp.gnu.org/gnu/patch/%{name}-%{version}.tar.xz
Group:		Development/Tools
Vendor:		Bildanet
Distribution:	Octothorpe
%description
Program for modifying or creating files by applying a patch
file typically created by the diff program.
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
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
/usr/bin/*
/usr/share/man/*/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:2.7.1-1
-	Upgrade version
