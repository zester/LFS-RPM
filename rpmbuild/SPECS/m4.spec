Summary:	A macro processor
Name:		m4
Version:	1.4.16
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/m4
Group:		Development/Tools
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/m4/%{name}-%{version}.tar.bz2
%description
The M4 package contains a macro processor
%prep
%setup -q
sed -i -e '/gets is a/d' lib/stdio.in.h
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_infodir}
%check
sed -i -e '41s/ENOENT/& || errno == EINVAL/' tests/test-readlink.h
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 1.4.16-1
-	Initial build.	First version
