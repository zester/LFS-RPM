Summary:	Reading, writing, and converting info pages
Name:		texinfo
Version:	4.13
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/texinfo/
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://ftp.gnu.org/gnu/texinfo/%{name}-%{version}.tar.gz
%description
The Texinfo package contains programs for reading, writing,
and converting info pages.
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
make DESTDIR=%{buildroot} TEXMF=/usr/share/texmf install-tex
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
/usr/share/texinfo
/usr/share/texmf
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:4.13a-0
-	Initial build.	First version
