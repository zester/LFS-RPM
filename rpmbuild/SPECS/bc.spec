Summary:	precision numeric processing language
Name:		bc
Version:	1.06.95
Release:	1
License:	GPLv2
URL:		http://alpha.gnu.org/gnu/bc/
Group:		LFS
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://alpha.gnu.org/gnu/bc/%{name}-%{version}.tar.bz2
%description
The Bc package contains an arbitrary precision numeric processing language.
%prep
%setup -q

%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--with-readline
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/info
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post
/sbin/ldconfig
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%{_bindir}/*
%{_mandir}/man1/*
%changelog
*	Fri May 10 2013 baho-utot <baho-utot@columbus.rr.com> 1.06.95-1
-	Initial build.	First version