Summary:	Time zone data
Name:		tzdata
Version:	2013c
Release:	1
URL:		http://www.iana.org/time-zones
License:	GPLv3
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source1:	http://www.iana.org//time-zones/repository/releases/%{name}%{version}.tar.gz
BuildArch:	noarch
%define blddir %{name}-%{version}
%description
Sources for time zone and daylight saving time data
%prep
rm -rf %{blddir}
install -vdm 755 %{blddir}
cd %{blddir}
tar xf %{SOURCE1}
%build
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd %{blddir}
ZONEINFO=%{buildroot}%{_datarootdir}/zoneinfo
install -vdm 755 $ZONEINFO/{posix,right}
for tz in etcetera southamerica northamerica europe africa antarctica  \
	asia australasia backward pacificnew solar87 solar88 solar89 \
	systemv; do
	zic -L /dev/null	-d $ZONEINFO		-y "sh yearistype.sh" ${tz}
	zic -L /dev/null	-d $ZONEINFO/posix	-y "sh yearistype.sh" ${tz}
	zic -L leapseconds	-d $ZONEINFO/right	-y "sh yearistype.sh" ${tz}
done
cp -v zone.tab iso3166.tab $ZONEINFO
zic -d $ZONEINFO -p America/New_York
install -vdm 755 %{buildroot}/etc
ln -s %{_datarootdir}/zoneinfo/America/New_York %{buildroot}/etc/localtime
%clean
rm -rf %{buildroot} %{_builddir}/*
%files
%defattr(-,root,root)
/etc/localtime
%{_datarootdir}/zoneinfo/*
%changelog
*	Fri May 10 2013 baho-utot <baho-utot@columbus.rr.com> 2013c-1
-	Update version to 2013c
*	Sun Mar 24 2013 baho-utot <baho-utot@columbus.rr.com> 2013b-1
-	Update version to 2013b
*	Sun Mar 24 2013 baho-utot <baho-utot@columbus.rr.com> 2012j-1
-	Update version
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 2012e-1
-	Initial build.	First version
