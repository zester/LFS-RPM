Summary:	Text file viewer
Name:		less
Version:	458
Release:	1
License:	GPLv3
URL:		http://www.greenwoodsoftware.com/less
Group:		Applications/File
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.greenwoodsoftware.com/less/%{name}-%{version}.tar.gz
%description
The Less package contains a text file viewer
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--sysconfdir=/etc
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*/*
%changelog
*	Fri May 10 2013 baho-utot <baho-utot@columbus.rr.com> 458-1
-	Update version to 458
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 451-1
-	Upgrade version
