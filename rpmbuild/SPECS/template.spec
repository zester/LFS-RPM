Summary:	
Name:		
Version:	
Release:	1
License:
URL:		
Group:		
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{name}-%{version}.tar.gz
Patch0:		
%description

%prep
%setup -q
%patch0 -p0

%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--htmldir=%{_docdir}/%{name}-%{version}
	--docdir=%{_docdir}/%{name}-%{version}

./configure CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--exec-prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--sysconfdir=/etc \
	--datadir=/%{_datadir} \
	--includedir=%{_includedir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--localstatedir=%{_localstatedir}
	--sharedstatedir=%{_sharedstatedir} \
	--mandir=%{_mandir} \
	--infodir=/%{_infodir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
#make PREFIX=%{buildroot}/usr install
find %{buildroot}/%{_libdir} -name '*.a'  -delete
find %{buildroot}/%{_libdir} -name '*.la' -delete
rm %{buildroot}/%{_infodir}/dir

%find_lang %{name}

%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}

%post
/sbin/ldconfig
/usr/bin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir || :
list=({,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11})
if [ -e /usr/bin/install-info ]; then
	for file in ${list[@]}; do
		/usr/bin/install-info %{_infodir}/${file}.gz %{_infodir}/dir 2> /dev/null
	done
fi
exit 0

%postun
/sbin/ldconfig
/usr/bin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir || :
list=({,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11})
if [ -x /usr/bin/install-info ] ; then
	for file in ${list[@]}; do
		/usr/bin/install-info --delete %{_infodir}/${file}.gz %{_infodir}/dir 2> /dev/null
	done
fi
exit 0

%clean
	rm -rf %{buildroot} %{pkgdir}

%files -f %{name}.lang
%defattr(-,root,root)

%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_datadir}/
%{_docdir}/%{name}-%{version}/*
%{_infodir}/*
%{_mandir}/*/*

%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 0:-0
-	Initial build.	First version