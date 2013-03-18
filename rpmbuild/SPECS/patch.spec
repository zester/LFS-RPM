Summary:	Program for modifying or creating files
Name:		patch
Version:	2.6.1
Release:	1
License:	GPLv3
URL:		http://savannah.gnu.org/projects/patch
Group:		Development/Tools
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://ftp.gnu.org/gnu/patch/patch-2.6.1.tar.bz2
Patch0:		http://www.linuxfromscratch.org/patches/lfs/7.2/patch-2.6.1-test_fix-1.patch
%description
Program for modifying or creating files by applying a patch
file typically created by the diff program.
%prep
%setup -q
%patch0 -p1
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
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:2.6.1-0
-	Initial build.	First version
