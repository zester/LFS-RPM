Summary:	Programs for handling passwords in a secure way
Name:		shadow
Version:	4.1.5.1
Release:	1
URL:		http://pkg-shadow.alioth.debian.org/
License:	BSD
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://pkg-shadow.alioth.debian.org/releases/%{name}-%{version}.tar.bz2
%description
The Shadow package contains programs for handling passwords
in a secure way.
%prep
%setup -q
sed -i 's/groups$(EXEEXT) //' src/Makefile.in
find man -name Makefile.in -exec sed -i 's/groups\.1 / /' {} \;
sed -i -e 's@#ENCRYPT_METHOD DES@ENCRYPT_METHOD SHA512@' \
	-e 's@/var/spool/mail@/var/mail@' etc/login.defs
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--sysconfdir=/etc
make %{?_smp_mflags}
%install
rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/bin
mv -v %{buildroot}/usr/bin/passwd %{buildroot}/bin
sed -i 's/yes/no/' %{buildroot}/etc/default/useradd
%find_lang %{name}
%post
/usr/sbin/pwconv
/usr/sbin/grpconv
%clean
rm -rf %{buildroot}
%files -f %{name}.lang
%defattr(-,root,root)
%config(noreplace) /etc/login.defs
%config(noreplace) /etc/login.access
%config(noreplace) /etc/default/useradd
%config(noreplace) /etc/limits
/bin/*
/sbin/*
/usr/bin/*
/usr/sbin/*
/usr/share/man/*/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 0:4.1.5.1-0
-	Initial build.	First version
