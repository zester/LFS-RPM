Summary:	Programs for basic networking
Name:		inetutils
Version:	1.9.1
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/inetutils
Group:		Applications/Communications
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/inetutils/%{name}-%{version}.tar.gz
%description
The Inetutils package contains programs for basic networking.
%prep
%setup -q
sed -i -e '/gets is a/d' lib/stdio.in.h
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_sbindir} \
	--localstatedir=%{_var} \
	--disable-ifconfig \
	--disable-logger \
	--disable-syslogd \
	--disable-whois \
	--disable-servers
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/bin
mv -v %{buildroot}%{_bindir}/{hostname,ping,ping6,traceroute} %{buildroot}/bin
rm -rf %{buildroot}%{_infodir}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
/bin/*
%{_bindir}/*
%{_mandir}/*/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 1.9.1-1
-	Initial build.	First version
