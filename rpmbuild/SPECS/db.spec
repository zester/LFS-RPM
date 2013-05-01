Summary:	A flat file database
Name:		db
Version:	5.3.21
Release:	1
License:	BSD
URL:		http://download.oracle.com/berkeley-db/
Group:		LFS/Base
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
export CFLAGS="%{optflags} -fno-strict-aliasing " CXXFLAGS="%{optflags}"
../dist/configure \
	--prefix=%{_prefix} \
	--docdir=%{_defaultdocdir}/%{name}-%{version} \
	--enable-compat185 \
	--enable-dbm \
	--disable-static \
	--enable-cxx \
	--disable-atomicsupport
make %{?_smp_mflags} LIB=-lpthread
%install
rm -rf %{buildroot}
cd build_unix
make DESTDIR=%{buildroot} docdir=%{_defaultdocdir}/%{name}-%{version} fmode=644 install
find %{buildroot}%{_libdir} -name '*.la' -delete
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%attr(555, root, root) %{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_defaultdocdir}/%{name}-%{version}/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 5.3.21-1
-	Initial build.	First version
