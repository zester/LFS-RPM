Summary:	Programs that show the differences between files or directories
Name:		diffutils
Version:	3.2
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/diffutils
Group:		Applications/File
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/diffutils/%{name}-%{version}.tar.gz
%description
The Diffutils package contains programs that show the
differences between files or directories.
%prep
%setup -q
sed -i -e '/gets is a/d' lib/stdio.in.h
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
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:2.6.1-0
-	Initial build.	First version