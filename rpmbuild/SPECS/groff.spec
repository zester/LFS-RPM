Summary:	Programs for processing and formatting text
Name:		groff
Version:	1.22.2
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/groff
Group:		Applications/Text
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/groff/%{name}-%{version}.tar.gz
%description
The Groff package contains programs for processing
and formatting text.
%prep
%setup -q
%build
PAGE=letter ./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr 
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
ln -sv eqn %{buildroot}/usr/bin/geqn
ln -sv tbl %{buildroot}/usr/bin/gtbl
rm -rf %{buildroot}/usr/share/info
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/usr/bin/*
/usr/lib/*
/usr/share/doc/%{name}-%{version}/*
/usr/share/%{name}/*
/usr/share/man/*/*
%changelog
*	Wed Mar 21 2013 GangGreene <GangGreene@bildanet.com> 0:1.22.2-1
-	Upgrade version
