Summary:	A flat file database
Name:		db
Version:	5.3.21
Release:	1
License:	BSD
URL:		http://download.oracle.com/berkeley-db/
Group:		Applications/Databases
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://download.oracle.com/berkeley-db/%{name}-%{version}.tar.gz
%description
This is Berkeley DB 11g Release 2 from Oracle
The Berkeley DB package contains programs and utilities used by many other 
applications for database related functions.
%prep
%setup -q
%build
cd build_unix
../dist/configure CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" \
	--prefix=/usr \
	--docdir=/usr/share/doc/%{name}-%{version} \
	--enable-compat185 \
	--enable-dbm \
	--disable-static \
	--enable-cxx \
	--with-posixmutexes
	sed -i 's|emode=\t555|emode=\t644|' Makefile
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
cd build_unix
make DESTDIR=%{buildroot} docdir=/usr/share/doc/%{name}-%{version} fmode=644 install
find %{buildroot}//usr/lib -name '*.la' -delete
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%attr(555, root, root) /usr/bin/*
/usr/lib/*
/usr/include/*
/usr/share/doc/%{name}-%{version}/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:5.3.21-1
-	Initial build.	First version
