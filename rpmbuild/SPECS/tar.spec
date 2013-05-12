Summary:	Archiving program
Name:		tar
Version:	1.26
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/tar
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://ftp.gnu.org/gnu/tar/%{name}-%{version}.tar.bz2
%description
Contains GNU archiving program
%prep
%setup -q
sed -i -e '/gets is a/d' gnu/stdio.in.h
%build
FORCE_UNSAFE_CONFIGURE=1  ./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--bindir=/bin \
	--libexecdir=%{_sbindir}
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
install -vdm 755 %{buildroot}%{_sbindir}
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} -C doc install-html docdir=%{_defaultdocdir}/%{name}-%{version}
rm -rf %{buildroot}%{_infodir}
%find_lang %{name}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%files -f %{name}.lang
%defattr(-,root,root)
/bin/tar
%{_sbindir}/rmt
%{_defaultdocdir}/%{name}-%{version}/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 1.26-1
-	Initial build.	First version
