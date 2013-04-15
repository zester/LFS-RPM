Summary:	Programming language
Name:		lua
Version:	5.1.5
Release:	1
License:	MIT
URL:		http://www.lua.org
Group:		Development/Tools
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{tarball}
Patch0:		lua-arch.patch
Patch1:		lua-5.1-cflags.diff
%description
Lua is a powerful, light-weight programming language designed for extending
applications. Lua is also frequently used as a general-purpose, stand-alone
language. Lua is free software
%define tarball	%{name}-%{version}.tar.gz
%define pkgdir	%{_builddir}/%{name}-%{version}
%prep
rm -rf %{pkgdir}
%setup -q
cd %{pkgdir}
patch -Np1 -i %{_sourcedir}/lua-arch.patch
patch -Np1 -i %{_sourcedir}/lua-5.1-cflags.diff
%build
cd %{pkgdir}
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
make %{?_smp_mflags} \
	INSTALL_DATA="cp -d" \
	TO_LIB="liblua.a liblua.so liblua.so.5.1" \
	INSTALL_TOP="%{buildroot}/usr" \
	INSTALL_MAN="%{buildroot}/usr/share/man/man1" \
	linux
make %{?_smp_mflags} \
	INSTALL_DATA="cp -d" \
	TO_LIB="liblua.a liblua.so liblua.so.5.1 liblua.so.%{version}" \
	INSTALL_TOP="%{buildroot}/usr" \
	INSTALL_MAN="%{buildroot}/usr/share/man/man1" \
	install
install -D -m644 etc/lua.pc "%{buildroot}/usr/lib/pkgconfig/lua.pc"
find %{buildroot}//usr/lib -name '*.a' -delete
%install
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
#	Binaries
/usr/bin/lua
/usr/bin/luac
#	Headers	
/usr/include/lauxlib.h
/usr/include/lua.h
/usr/include/lua.hpp
/usr/include/luaconf.h
/usr/include/lualib.h
#	Libraries
/usr/lib/liblua.so
/usr/lib/liblua.so.5.1
/usr/lib/liblua.so.5.1.5
/usr/lib/pkgconfig/lua.pc
#	Documentation
%doc /usr/share/man/man1/lua.1.gz
%doc /usr/share/man/man1/luac.1.gz

%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 0:5.1.5-0
-	Initial build.	First version
