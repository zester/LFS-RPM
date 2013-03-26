Summary:	Text file viewer
Name:		less
Version:	451
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
	--prefix=/usr \
	--sysconfdir=/etc
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
/usr/bin/*
/usr/share/man/*/*
%changelog
*	Wed Mar 21 2013 GangGreene <GangGreene@bildanet.com> 0:451-1
-	Upgrade version