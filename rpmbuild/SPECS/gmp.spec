Summary:	Math libraries
Name:		gmp
Version:	5.1.1
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/gmp
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/gmp/%{name}-%{version}.tar.xz
%description
The GMP package contains math libraries. These have useful functions
for arbitrary precision arithmetic.
%prep
%setup -q
%build
%ifarch i386 i486 i586 i686
	ABI=32 ./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--enable-cxx \
	--enable-mpbsd
%else
	./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--enable-cxx \
	--enable-mpbsd
%endif
make %{?_smp_mflags}
%install
rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}%{_defaultdocdir}/%{name}-%{version}
cp    -v doc/{isa_abi_headache,configuration} doc/*.html \
	%{buildroot}%{_defaultdocdir}/%{name}-%{version}
find %{buildroot}%{_libdir} -name '*.a' -delete
find %{buildroot}%{_libdir} -name '*.la' -delete
rm -rf %{buildroot}%{_infodir}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_defaultdocdir}/%{name}-%{version}/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 5.1.1-1
-	Upgrade version
