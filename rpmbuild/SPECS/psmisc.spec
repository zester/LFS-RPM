Summary:	Displays information about running processes
Name:		psmisc
Version:	22.20
Release:	1
License:	GPLv2
URL:		http://psmisc.sourceforge.net/
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://prdownloads.sourceforge.net/psmisc/%{name}-%{version}.tar.gz
%description
The Psmisc package contains programs for displaying information
about running processes.
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
install -vdm 755 %{buildroot}/bin
mv -v %{buildroot}/usr/bin/fuser   %{buildroot}/bin
mv -v %{buildroot}/usr/bin/killall %{buildroot}/bin
%find_lang %{name}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%files -f %{name}.lang
%defattr(-,root,root)
/bin/*
/usr/bin/*
/usr/share/man/*/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:22.20-1
-	Upgrade version
