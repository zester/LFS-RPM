Summary:	Time zone data
Name:		tzdata
Version:	2012j
Release:	1
URL:		http://www.iana.org/time-zones
License:	GPLv3
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.iana.org//time-zones/repository/releases/%{name}%{version}.tar.gz
BuildArch:	noarch
%define blddir %{name}-%{version}
%define tarball	%{name}%{version}.tar.gz
%description
Sources for time zone and daylight saving time data
%prep
rm -rf %{blddir}
install -vdm 755 %{blddir}
cd %{blddir}
tar xf %{_sourcedir}/%{name}%{version}.tar.gz
%build
%install
cd %{blddir}
ZONEINFO=%{buildroot}/usr/share/zoneinfo
install -vdm 755 $ZONEINFO/{posix,right}
for tz in etcetera southamerica northamerica europe africa antarctica  \
         asia australasia backward pacificnew solar87 solar88 solar89 \
         systemv; do
	zic -L /dev/null   -d $ZONEINFO       -y "sh yearistype.sh" ${tz}
	zic -L /dev/null   -d $ZONEINFO/posix -y "sh yearistype.sh" ${tz}
	zic -L leapseconds -d $ZONEINFO/right -y "sh yearistype.sh" ${tz}
done
cp -v zone.tab iso3166.tab $ZONEINFO
zic -d $ZONEINFO -p America/New_York
install -vdm 755 %{buildroot}/etc
ln -s /usr/share/zoneinfo/America/New_York %{buildroot}/etc/localtime
%clean
rm -rf %{buildroot} %{_builddir}/*
%files
%defattr(-,root,root)
/etc/localtime
/usr/share/zoneinfo/*
%changelog
*	Sun Mar 24 2013 GangGreene <GangGreene@bildanet.com> 2012j-1
-	Update version

*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 2012e-1
-	Initial build.	First version
