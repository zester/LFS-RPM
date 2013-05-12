Summary:	Programming language
Name:		lua
Version:	5.1.5
Release:	1
License:	MIT
URL:		http://www.lua.org
Group:		Development/Tools
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	ttp://www.lua.org/ftp/%{name}-%{version}.tar.gz
Patch0:		lua-arch.patch
Patch1:		lua-5.1-cflags.diff
%description
Lua is a powerful, light-weight programming language designed for extending
applications. Lua is also frequently used as a general-purpose, stand-alone
language. Lua is free software
%prep
%setup -q
patch -Np1 -i %{_sourcedir}/lua-arch.patch
patch -Np1 -i %{_sourcedir}/lua-5.1-cflags.diff
%build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
make %{?_smp_mflags} MYCFLAGS="$CFLAGS" MYLDFLAGS="$LDFLAGS" linux
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make %{?_smp_mflags} \
	INSTALL_DATA="cp -d" \
	TO_LIB="liblua.a liblua.so liblua.so.5.1 liblua.so.%{version}" \
	INSTALL_TOP="%{buildroot}/usr" \
	INSTALL_INC="%{buildroot}/usr/include/" \
	INSTALL_MAN="%{buildroot}/usr/share/man/man1" \
	install
install -D -m644 etc/lua.pc "%{buildroot}/usr/lib/pkgconfig/lua.pc"
find %{buildroot}/usr/lib -name '*.a' -delete
rm -rf %{buildroot}/%{_libdir}/lua
rm -rf %{buildroot}/%{_datarootdir}/lua

%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
#	Binaries
%{_bindir}/lua
%{_bindir}/luac
#	Headers	
%{_includedir}/lauxlib.h
%{_includedir}/lua.h
%{_includedir}/lua.hpp
%{_includedir}/luaconf.h
%{_includedir}/lualib.h
#	Libraries
%{_libdir}/liblua.so
%{_libdir}/liblua.so.5.1
%{_libdir}/liblua.so.5.1.5
%{_libdir}/pkgconfig/lua.pc
#	Documentation
%{_mandir}/man1/lua.1.gz
%{_mandir}/man1/luac.1.gz
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 5.1.5-1
-	Initial build.	First version
