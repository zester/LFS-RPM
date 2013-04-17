Summary:	Stream editor
Name:		sed
Version:	4.2.2
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/sed
Group:		Applications/Editors
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/sed/%{name}-%{version}.tar.bz2
%description
The Sed package contains a stream editor.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--bindir=/bin \
	--libdir=%{_libdir} \
	--htmldir=%{_defaultdocdir}/%{name}-%{version}
make %{?_smp_mflags}
%install
rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_infodir}
%find_lang %{name}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}/*
%files -f %{name}.lang
%defattr(-,root,root)
/bin/*
%{_mandir}/*/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:4.2.1-1
-	Upgrade version
