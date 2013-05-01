Name:		elfutils
Summary:	A collection of utilities and DSOs to handle compiled objects
Version:	0.155
Release:	1
URL:		https://fedorahosted.org/elfutils/
License:	GPLv3+ and (GPLv2+ or LGPLv3+)
Group:		Development/Tools
Source:		http://fedorahosted.org/releases/e/l/elfutils/%{version}/%{name}-%{version}.tar.bz2
Patch0:		elfutils-portability.patch
Patch1:		elfutils-robustify.patch
#BuildRequires: bison >= 1.875
#BuildRequires: flex >= 2.5.4a
#BuildRequires: bzip2
#BuildRequires: gcc >= 3.4
#BuildRequires: zlib >= 1.2.2.3
#BuildRequires: xz
%description
Elfutils is a collection of utilities, including ld (a linker),
nm (for listing symbols from object files), size (for listing the
section sizes of an object or archive file), strip (for discarding
symbols), readelf (to see the raw ELF file structures), and elflint
(to check for well-formed ELF files).
%prep
%setup -q
%patch0	-p1
%patch1 -p1
%build
#	CFLAGS+=" -g"  # required for test-suite success
./configure  CFLAGS="%{optflags} -g" CXXFLAGS="%{optflags} -g " \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--disable-werror \
	--program-prefix="eu-" || {
	cat config.log
	exit 2
	}
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
chmod +x %{buildroot}%{_libdir}/lib*.so*
chmod +x %{buildroot}%{_libdir}/elfutils/lib*.so*
#	XXX Nuke unpackaged files
find %{buildroot} -name eu-ld -delete
find %{buildroot}%{_libdir} -name '*.la' -delete
find %{buildroot}%{_libdir} -name '*.a' -delete
%find_lang %{name}
%check
make -s check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files	 -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 0.155-1
-	Initial build.	First version
