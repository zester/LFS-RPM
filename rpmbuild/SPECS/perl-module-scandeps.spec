Summary:	Scans potential modules used by perl programs
Name:		Module-ScanDeps
Version:	1.10
Release:	1
License:	Artistic
URL:		http://www.cpan.org
Group:		Perl/Module
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	Module-ScanDeps-%{version}.tar.gz
%description
An application of Module::ScanDeps is to generate executables from scripts
that contains necessary modules; this module supports two such projects,
PAR and App::Packer.  Please see their respective documentations on CPAN
for further information.
%prep
%setup -q
%build
perl Makefile.PL
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
rm -rf inc
make DESTDIR=%{buildroot} install
%check
make -k test |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot} %{pkgdir}
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%changelog
*	Thu May 16 2013 baho-utot <baho-utot@columbus.rr.com> 1.10-1
-	Initial build.	First version