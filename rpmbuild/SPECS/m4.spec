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
	--prefix=/usr 
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/share/info
%check
sed -i -e '41s/ENOENT/& || errno == EINVAL/' tests/test-readlink.h
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
/usr/bin/*
/usr/share/man/*/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 0:1.4.16-0
-	Initial build.	First version
