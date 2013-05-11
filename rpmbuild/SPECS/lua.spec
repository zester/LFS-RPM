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
sed -e 's:llua:llua5.1:' -e 's:/include:/include/lua5.1:' -i etc/lua.pc
sed -r -e '/^LUA_(SO|A|T)=/ s/lua/lua5.1/' -e '/^LUAC_T=/ s/luac/luac5.1/' -i src/Makefile
make %{?_smp_mflags} MYCFLAGS="$CFLAGS" MYLDFLAGS="$LDFLAGS" linux
#make %{?_smp_mflags} \
#	TO_BIN="lua5.1 luac5.1" \
#	TO_LIB="liblua5.1.a liblua5.1.so liblua5.1.so.5.1 liblua5.1.so.5" \
#	INSTALL_DATA="cp -d" \
#	INSTALL_TOP="%{buildroot}/usr" \
#	INSTALL_MAN="%{buildroot}/usr/share/man/man1" \
#	linux
%install
make %{?_smp_mflags} \
	INSTALL_DATA="cp -d" \
	TO_LIB="liblua.a liblua.so liblua.so.5.1 liblua.so.%{version}" \
	INSTALL_TOP="%{buildroot}/usr" \
	INSTALL_INC="%{buildroot}/usr/include/lua5.1" \
	INSTALL_MAN="%{buildroot}/usr/share/man/man1" \
	install
install -D -m644 etc/lua.pc "%{buildroot}/usr/lib/pkgconfig/lua.pc"
install -D -m644 etc/lua.pc "%{buildroot}/usr/lib/pkgconfig/lua5.1.pc"
# fixups
ln -s liblua5.1.so "%{buildroot}/usr/lib/liblua.so.5.1"
ln -s liblua5.1.so "$pkgdir/usr/lib/liblua.so.%{version}"   
find %{buildroot}//usr/lib -name '*.a' -delete
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
%{_libdir}/pkgconfig/lua.pc
#	Documentation
%{_mandir}/man1/lua.1.gz
%{_mandir}/man1/luac.1.gz
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 5.1.5-1
-	Initial build.	First version
