Summary:	Programs for monitoring processes
Name:		procps
Version:	3.2.8
Release:	1
License:	GPLv2
URL:		http://procps.sourceforge.net/
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://procps.sourceforge.net/%{name}-%{version}.tar.gz
Patch1:		procps-3.2.8-fix_HZ_errors-1.patch
Patch2:		procps-3.2.8-watch_unicode-1.patch
%description
The Procps package contains programs for monitoring processes.
%prep
%setup -q
%patch1	-p1
%patch2	-p1
sed -i -e 's@\*/module.mk@proc/module.mk ps/module.mk@' Makefile
%build
make %{?_smp_mflags} SHARED=1 CFLAGS="%{optflags}" W_SHOWFROM=-DW_SHOWFROM
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} ldconfig=true install="install -D" install
chmod -R u+w %{buildroot}/sbin
chmod -R u+w %{buildroot}/bin
chmod -R u+w %{buildroot}/usr/bin
chmod -R u+w %{buildroot}/lib*
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/bin/*
/sbin/*
/lib/*
/usr/bin/*
/usr/share/man/*/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:3.2.8-0
-	ver -0
-	Initial build.	First version
