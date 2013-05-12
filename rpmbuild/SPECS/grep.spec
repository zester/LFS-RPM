Summary:	Programs for searching through files
Name:		grep
Version:	2.14
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/grep
Group:		Applications/File
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/grep/%{name}-%{version}.tar.xz
%description
The Grep package contains programs for searching through files.
%prep
%setup -q
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--bindir=/bin 
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_infodir}
%find_lang %{name}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%files -f %{name}.lang
%defattr(-,root,root)
/bin/*
%{_mandir}/*/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 2.14-1
-	Initial build.	First version
