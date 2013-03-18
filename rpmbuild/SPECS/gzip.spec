Summary:	Programs for compressing and decompressing files
Name:		gzip
Version:	1.5
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software
Group:		Applications/File
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/gzip/%{name}-%{version}.tar.xz
%description
The Gzip package contains programs for compressing and
decompressing files.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr \
	--bindir=/bin
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/bin
install -vdm 755 %{buildroot}/usr/bin
mv -v %{buildroot}/bin/{gzexe,uncompress,zcmp,zdiff,zegrep}	%{buildroot}/usr/bin
mv -v %{buildroot}/bin/{zfgrep,zforce,zgrep,zless,zmore,znew}	%{buildroot}/usr/bin
rm -rf %{buildroot}/usr/share/info
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
/bin/*
/usr/bin/*
/usr/share/man/*/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:1.5-0
-	Initial build.	First version
