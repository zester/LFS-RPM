Summary:	Contains programs for manipulating text files
Name:		gawk
Version:	4.0.2
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/gawk
Group:		Applications/File
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/gawk/%{name}-%{version}.tar.xz
%description
The Gawk package contains programs for manipulating text files.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libexecdir=%{_libexecdir}
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}%{_defaultdocdir}/%{name}-%{version}
cp -v doc/{awkforai.txt,*.{eps,pdf,jpg}} %{buildroot}%{_defaultdocdir}/%{name}-%{version}
rm -rf %{buildroot}%{_infodir}
%find_lang %{name}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_datarootdir}/awk/*
%{_defaultdocdir}/%{name}-%{version}/*
%{_mandir}/*/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:4.0.2-1
-	Upgrade version
