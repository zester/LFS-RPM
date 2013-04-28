Summary:	Programming language
Name:		lua
Version:	5.2.2
Release:	1
License:	MIT
URL:		http://www.lua.org
Group:		Development/Tools
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	%{tarball}
Source1:	lua.pc
Patch0:		liblua.so.patch

%description
Lua is a powerful, light-weight programming language designed for extending
applications. Lua is also frequently used as a general-purpose, stand-alone
language. Lua is free software
%define tarball	%{name}-%{version}.tar.gz
%define pkgdir	%{_builddir}/%{name}-%{version}
%prep
%setup -q
%patch -p1
%build
cd %{pkgdir}
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
make %{?_smp_mflags} \
	MYCFLAGS="$CFLAGS" \
	MYLDFLAGS="$LDFLAGS" \
	linux
sed "s/%VER%/5.2.2}/g;s/%REL%/1/g" ../lua.pc > lua.pc
install -D -m644 etc/lua.pc "%{buildroot}/usr/lib/pkgconfig/lua.pc"
find %{buildroot}/usr/lib -name '*.a' -delete
find %{buildroot}/usr/lib -name '*.la' -delete
%install
	make \
	TO_LIB="liblua.a liblua.so liblua.so.5.2 liblua.so.5.2.1" \
	INSTALL_DATA="cp -d" \
	INSTALL_TOP="$pkgdir/usr" \
	INSTALL_MAN="$pkgdir/usr/share/man/man1" \
	install
	install -Dm644 lua.pc "$pkgdir/usr/lib/pkgconfig/lua.pc"
#	Install the documentation
	install -d "$pkgdir/usr/share/doc/lua"
	install -m644 doc/*.{gif,png,css,html} "$pkgdir/usr/share/doc/lua"
	install -D -m644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
#	Binaries
#/usr/bin/lua
#/usr/bin/luac
#	Headers	
#/usr/include/lauxlib.h
#/usr/include/lua.h
#/usr/include/lua.hpp
#/usr/include/luaconf.h
#/usr/include/lualib.h
#	Libraries
#/usr/lib/liblua.so
#/usr/lib/liblua.so.5.1
#/usr/lib/liblua.so.5.1.5
#/usr/lib/pkgconfig/lua.pc
#	Documentation
#%doc /usr/share/man/man1/lua.1.gz
#%doc /usr/share/man/man1/luac.1.gz

%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 0:5.1.5-0
-	Initial build.	First version
