Summary:	Math libraries
Name:		gmp
Version:	5.0.5
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
	--prefix=/usr \
	--enable-cxx \
	--enable-mpbsd
%else
	./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr \
	--enable-cxx \
	--enable-mpbsd
%endif
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/usr/share/doc/%{name}-%{version}
cp    -v doc/{isa_abi_headache,configuration} doc/*.html \
	%{buildroot}/usr/share/doc/%{name}-%{version}
#find %{buildroot}/usr/lib -name '*.a'  -delete
find %{buildroot}/usr/lib -name '*.la' -delete
rm -rf %{buildroot}/usr/share/info
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/usr/lib/*
/usr/include/*
/usr/share/doc/%{name}-%{version}/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 5.0.5-0
-	Initial build.	First version
