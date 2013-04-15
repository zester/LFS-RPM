Summary:	Data for network services and protocols
Name:		iana-etc
Version:	2.30
Release:	1
License:	OSLv3
URL:		http://freshmeat.net/projects/iana-etc
Group:		System Environment/Base
Vendor:		Bildanet
Distribution:	Octothorpe
BuildArch:	noarch
Source:		http://anduin.linuxfromscratch.org/sources/LFS/lfs-packages/conglomeration//iana-etc/%{name}-%{version}.tar.bz2
%description
The Iana-Etc package provides data for network services and protocols.
%prep
%setup -q
%build
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
/etc/protocols
/etc/services
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 0:2.30-0
-	Initial build.	First version
