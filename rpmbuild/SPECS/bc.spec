Summary:	precision numeric processing language
Name:		bc
Version:	1.0.6.95
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
find %{buildroot}/%{_libdir} -name '*.a'  -delete
find %{buildroot}/%{_libdir} -name '*.la' -delete
rm %{buildroot}/%{_infodir}/dir
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%post
/sbin/ldconfig
%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)

#%{_bindir}/*
#%{_libdir}/*
#%{_includedir}/*
#%{_datarootdir}/
#%{_docdir}/%{name}-%{version}/*
#%{_infodir}/*
#%{_mandir}/*/*
%changelog
*	Fri May 10 2013 baho-utot <baho-utot@columbus.rr.com> 1.06.95-1
-	Initial build.	First version