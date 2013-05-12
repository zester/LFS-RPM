Summary:	Contains the GNU compiler collection
Name:		gcc
Version:	4.8.0
Release:	1
License:	GPLv2
URL:		http://gcc.gnu.org
Group:		Development/Tools
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/gcc/%{name}-%{version}/%{name}-%{version}.tar.bz2
%description
The GCC package contains the GNU compiler collection,
which includes the C and C++ compilers.
%prep
%setup -q
case `uname -m` in
	i?86) sed -i 's/^T_CFLAGS =$/& -fomit-frame-pointer/' gcc/Makefile.in ;;
esac
sed -i 's/install_to_$(INSTALL_DEST) //' libiberty/Makefile.in
sed -i -e /autogen/d -e /check.sh/d fixincludes/Makefile.in
mv -v libmudflap/testsuite/libmudflap.c++/pass41-frag.cxx{,.disable}
#sed -i 's/BUILD_INFO=info/BUILD_INFO=/' gcc/configure
install -vdm 755 ../gcc-build
%build
cd ../gcc-build
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
../%{name}-%{version}/configure \
	--prefix=%{_prefix} \
	--libexecdir=%{_libexecdir} \
	--enable-shared \
	--enable-threads=posix \
	--enable-__cxa_atexit \
	--enable-clocale=gnu \
	--enable-languages=c,c++ \
	--disable-multilib \
	--disable-bootstrap \
	--disable-install-libiberty \
	--with-system-zlib
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd ../gcc-build
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/lib
ln -sv ..%{_bindir}/cpp %{buildroot}/lib
ln -sv gcc %{buildroot}%{_bindir}/cc
install -vdm 755 %{buildroot}%{_datarootdir}/gdb/auto-load%{_libdir}
mv -v %{buildroot}%{_libdir}/*gdb.py %{buildroot}%{_datarootdir}/gdb/auto-load%{_libdir}
find %{buildroot}%{_libdir} -name '*.la' -delete
find %{buildroot}%{_libexecdir} -name '*.la' -delete
rm -rf %{buildroot}%{_infodir}
%check
cd ../gcc-build
ulimit -s 32768
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/lib/cpp
#	Executables
%{_bindir}/c++
%{_bindir}/cc
%{_bindir}/cpp
%{_bindir}/g++
%{_bindir}/gcc
%{_bindir}/gcc-ar
%{_bindir}/gcc-nm
%{_bindir}/gcc-ranlib
%{_bindir}/gcov
%{_bindir}/i686-pc-linux-gnu-c++
%{_bindir}/i686-pc-linux-gnu-g++
%{_bindir}/i686-pc-linux-gnu-gcc
%{_bindir}/i686-pc-linux-gnu-gcc-4.8.0
%{_bindir}/i686-pc-linux-gnu-gcc-ar
%{_bindir}/i686-pc-linux-gnu-gcc-nm
%{_bindir}/i686-pc-linux-gnu-gcc-ranlib
#	Includes
%{_includedir}/c++/4.8.0/*.h
%{_includedir}/c++/4.8.0/algorithm
%{_includedir}/c++/4.8.0/array
%{_includedir}/c++/4.8.0/atomic
%{_includedir}/c++/4.8.0/backward/*.h
%{_includedir}/c++/4.8.0/backward/hash_map
%{_includedir}/c++/4.8.0/backward/hash_set
%{_includedir}/c++/4.8.0/backward/strstream
%{_includedir}/c++/4.8.0/bitset
%{_includedir}/c++/4.8.0/bits/*.h
%{_includedir}/c++/4.8.0/bits/*.tcc
%{_includedir}/c++/4.8.0/cassert
%{_includedir}/c++/4.8.0/ccomplex
%{_includedir}/c++/4.8.0/cctype
%{_includedir}/c++/4.8.0/cerrno
%{_includedir}/c++/4.8.0/cfenv
%{_includedir}/c++/4.8.0/cfloat
%{_includedir}/c++/4.8.0/chrono
%{_includedir}/c++/4.8.0/cinttypes
%{_includedir}/c++/4.8.0/ciso646
%{_includedir}/c++/4.8.0/climits
%{_includedir}/c++/4.8.0/clocale
%{_includedir}/c++/4.8.0/cmath
%{_includedir}/c++/4.8.0/complex
%{_includedir}/c++/4.8.0/condition_variable
%{_includedir}/c++/4.8.0/csetjmp
%{_includedir}/c++/4.8.0/csignal
%{_includedir}/c++/4.8.0/cstdalign
%{_includedir}/c++/4.8.0/cstdarg
%{_includedir}/c++/4.8.0/cstdbool
%{_includedir}/c++/4.8.0/cstddef
%{_includedir}/c++/4.8.0/cstdint
%{_includedir}/c++/4.8.0/cstdio
%{_includedir}/c++/4.8.0/cstdlib
%{_includedir}/c++/4.8.0/cstring
%{_includedir}/c++/4.8.0/ctgmath
%{_includedir}/c++/4.8.0/ctime
%{_includedir}/c++/4.8.0/cwchar
%{_includedir}/c++/4.8.0/cwctype
%{_includedir}/c++/4.8.0/debug/array
%{_includedir}/c++/4.8.0/debug/bitset
%{_includedir}/c++/4.8.0/debug/deque
%{_includedir}/c++/4.8.0/debug/forward_list
%{_includedir}/c++/4.8.0/debug/*.h
%{_includedir}/c++/4.8.0/debug/list
%{_includedir}/c++/4.8.0/debug/map
%{_includedir}/c++/4.8.0/debug/set
%{_includedir}/c++/4.8.0/debug/string
%{_includedir}/c++/4.8.0/debug/*.tcc
%{_includedir}/c++/4.8.0/debug/unordered_map
%{_includedir}/c++/4.8.0/debug/unordered_set
%{_includedir}/c++/4.8.0/debug/vector
%{_includedir}/c++/4.8.0/decimal/decimal
%{_includedir}/c++/4.8.0/decimal/decimal.h
%{_includedir}/c++/4.8.0/deque
%{_includedir}/c++/4.8.0/exception
%{_includedir}/c++/4.8.0/ext/algorithm
%{_includedir}/c++/4.8.0/ext/cmath
%{_includedir}/c++/4.8.0/ext/functional
%{_includedir}/c++/4.8.0/ext/*.h
%{_includedir}/c++/4.8.0/ext/hash_map
%{_includedir}/c++/4.8.0/ext/hash_set
%{_includedir}/c++/4.8.0/ext/iterator
%{_includedir}/c++/4.8.0/ext/memory
%{_includedir}/c++/4.8.0/ext/numeric
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/binary_heap_/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/binomial_heap_base_/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/binomial_heap_/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/bin_search_tree_/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/branch_policy/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/cc_hash_table_map_/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/eq_fn/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/gp_hash_table_map_/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/hash_fn/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/left_child_next_sibling_heap_/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/list_update_map_/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/list_update_policy/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/ov_tree_map_/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/pairing_heap_/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/pat_trie_/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/rb_tree_map_/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/rc_binomial_heap_/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/resize_policy/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/splay_tree_/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/thin_heap_/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/tree_policy/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/trie_policy/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/detail/unordered_iterator/*.hpp
%{_includedir}/c++/4.8.0/ext/pb_ds/*.hpp
%{_includedir}/c++/4.8.0/ext/random
%{_includedir}/c++/4.8.0/ext/rb_tree
%{_includedir}/c++/4.8.0/ext/rope
%{_includedir}/c++/4.8.0/ext/slist
%{_includedir}/c++/4.8.0/ext/*.tcc
%{_includedir}/c++/4.8.0/forward_list
%{_includedir}/c++/4.8.0/fstream
%{_includedir}/c++/4.8.0/functional
%{_includedir}/c++/4.8.0/future
%{_includedir}/c++/4.8.0/i686-pc-linux-gnu/bits/*.h
%{_includedir}/c++/4.8.0/initializer_list
%{_includedir}/c++/4.8.0/iomanip
%{_includedir}/c++/4.8.0/ios
%{_includedir}/c++/4.8.0/iosfwd
%{_includedir}/c++/4.8.0/iostream
%{_includedir}/c++/4.8.0/istream
%{_includedir}/c++/4.8.0/iterator
%{_includedir}/c++/4.8.0/limits
%{_includedir}/c++/4.8.0/list
%{_includedir}/c++/4.8.0/locale
%{_includedir}/c++/4.8.0/map
%{_includedir}/c++/4.8.0/memory
%{_includedir}/c++/4.8.0/mutex
%{_includedir}/c++/4.8.0/new
%{_includedir}/c++/4.8.0/numeric
%{_includedir}/c++/4.8.0/ostream
%{_includedir}/c++/4.8.0/parallel/algorithm
%{_includedir}/c++/4.8.0/parallel/*.h
%{_includedir}/c++/4.8.0/parallel/numeric
%{_includedir}/c++/4.8.0/profile/*.h
%{_includedir}/c++/4.8.0/profile/array
%{_includedir}/c++/4.8.0/profile/bitset
%{_includedir}/c++/4.8.0/profile/deque
%{_includedir}/c++/4.8.0/profile/forward_list
%{_includedir}/c++/4.8.0/profile/impl/*.h
%{_includedir}/c++/4.8.0/profile/list
%{_includedir}/c++/4.8.0/profile/map
%{_includedir}/c++/4.8.0/profile/set
%{_includedir}/c++/4.8.0/profile/unordered_map
%{_includedir}/c++/4.8.0/profile/unordered_set
%{_includedir}/c++/4.8.0/profile/vector
%{_includedir}/c++/4.8.0/queue
%{_includedir}/c++/4.8.0/random
%{_includedir}/c++/4.8.0/ratio
%{_includedir}/c++/4.8.0/regex
%{_includedir}/c++/4.8.0/scoped_allocator
%{_includedir}/c++/4.8.0/set
%{_includedir}/c++/4.8.0/sstream
%{_includedir}/c++/4.8.0/stack
%{_includedir}/c++/4.8.0/stdexcept
%{_includedir}/c++/4.8.0/streambuf
%{_includedir}/c++/4.8.0/string
%{_includedir}/c++/4.8.0/system_error
%{_includedir}/c++/4.8.0/thread
%{_includedir}/c++/4.8.0/tr1/array
%{_includedir}/c++/4.8.0/tr1/ccomplex
%{_includedir}/c++/4.8.0/tr1/cctype
%{_includedir}/c++/4.8.0/tr1/cfenv
%{_includedir}/c++/4.8.0/tr1/cfloat
%{_includedir}/c++/4.8.0/tr1/cinttypes
%{_includedir}/c++/4.8.0/tr1/climits
%{_includedir}/c++/4.8.0/tr1/cmath
%{_includedir}/c++/4.8.0/tr1/complex
%{_includedir}/c++/4.8.0/tr1/cstdarg
%{_includedir}/c++/4.8.0/tr1/cstdbool
%{_includedir}/c++/4.8.0/tr1/cstdint
%{_includedir}/c++/4.8.0/tr1/cstdio
%{_includedir}/c++/4.8.0/tr1/cstdlib
%{_includedir}/c++/4.8.0/tr1/ctgmath
%{_includedir}/c++/4.8.0/tr1/ctime
%{_includedir}/c++/4.8.0/tr1/cwchar
%{_includedir}/c++/4.8.0/tr1/cwctype
%{_includedir}/c++/4.8.0/tr1/functional
%{_includedir}/c++/4.8.0/tr1/*.h
%{_includedir}/c++/4.8.0/tr1/memory
%{_includedir}/c++/4.8.0/tr1/random
%{_includedir}/c++/4.8.0/tr1/regex
%{_includedir}/c++/4.8.0/tr1/*.tcc
%{_includedir}/c++/4.8.0/tr1/tuple
%{_includedir}/c++/4.8.0/tr1/type_traits
%{_includedir}/c++/4.8.0/tr1/unordered_map
%{_includedir}/c++/4.8.0/tr1/unordered_set
%{_includedir}/c++/4.8.0/tr1/utility
%{_includedir}/c++/4.8.0/tr2/bool_set
%{_includedir}/c++/4.8.0/tr2/bool_set.tcc
%{_includedir}/c++/4.8.0/tr2/dynamic_bitset
%{_includedir}/c++/4.8.0/tr2/ratio
%{_includedir}/c++/4.8.0/tr2/type_traits
%{_includedir}/c++/4.8.0/tuple
%{_includedir}/c++/4.8.0/typeindex
%{_includedir}/c++/4.8.0/typeinfo
%{_includedir}/c++/4.8.0/type_traits
%{_includedir}/c++/4.8.0/unordered_map
%{_includedir}/c++/4.8.0/unordered_set
%{_includedir}/c++/4.8.0/utility
%{_includedir}/c++/4.8.0/valarray
%{_includedir}/c++/4.8.0/vector
#	Libraries
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_libdir}/*.o
%{_libdir}/*.spec
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/*.a
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/*.o
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/finclude
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/include/*.h
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/include-fixed/README
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/include-fixed/*.h
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/include/ssp/*.h
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/install-tools/*.h
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/install-tools/fixinc_list
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/install-tools/include/README
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/install-tools/include/limits.h
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/install-tools/macro_list
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/install-tools/mkheaders.conf
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/plugin/gtype.state
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/plugin/include/*.h
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/plugin/include/*.def
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/plugin/include/ada/gcc-interface/ada-tree.def
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/plugin/include/b-header-vars
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/plugin/include/c-family/c-common.def
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/plugin/include/c-family/*.h
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/plugin/include/config/*.h
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/plugin/include/config/i386/*.h
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/plugin/include/cp/*.def
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/plugin/include/cp/*.h
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/plugin/include/objc/objc-tree.def
%{_libdir}/gcc/i686-pc-linux-gnu/4.8.0/plugin/include/java/java-tree.def

#	Library executables
%{_libexecdir}/gcc/i686-pc-linux-gnu/4.8.0/cc1
%{_libexecdir}/gcc/i686-pc-linux-gnu/4.8.0/cc1plus
%{_libexecdir}/gcc/i686-pc-linux-gnu/4.8.0/collect2
%{_libexecdir}/gcc/i686-pc-linux-gnu/4.8.0/install-tools/fixinc.sh
%{_libexecdir}/gcc/i686-pc-linux-gnu/4.8.0/install-tools/fixincl
%{_libexecdir}/gcc/i686-pc-linux-gnu/4.8.0/install-tools/mkheaders
%{_libexecdir}/gcc/i686-pc-linux-gnu/4.8.0/install-tools/mkinstalldirs
%{_libexecdir}/gcc/i686-pc-linux-gnu/4.8.0/*.so
%{_libexecdir}/gcc/i686-pc-linux-gnu/4.8.0/*.so.*
%{_libexecdir}/gcc/i686-pc-linux-gnu/4.8.0/lto-wrapper
%{_libexecdir}/gcc/i686-pc-linux-gnu/4.8.0/lto1
%{_libexecdir}/gcc/i686-pc-linux-gnu/4.8.0/plugin/gengtype
#	Python files
%{_datarootdir}/gcc-4.8.0/python/libstdcxx/__init__.py
%{_datarootdir}/gcc-4.8.0/python/libstdcxx/v6/__init__.py
%{_datarootdir}/gcc-4.8.0/python/libstdcxx/v6/printers.py
%{_datarootdir}/gdb/auto-load/usr/lib/libstdc++.so.6.0.18-gdb.py
#	Internationalization
%lang(be)%{_datarootdir}/locale/be/LC_MESSAGES/*.mo
%lang(ca)%{_datarootdir}/locale/ca/LC_MESSAGES/*.mo
%lang(da)%{_datarootdir}/locale/da/LC_MESSAGES/*.mo
%lang(de)%{_datarootdir}/locale/de/LC_MESSAGES/*.mo
%lang(el)%{_datarootdir}/locale/el/LC_MESSAGES/*.mo
%lang(eo)%{_datarootdir}/locale/eo/LC_MESSAGES/*.mo
%lang(es)%{_datarootdir}/locale/es/LC_MESSAGES/*.mo
%lang(fi)%{_datarootdir}/locale/fi/LC_MESSAGES/*.mo
%lang(fr)%{_datarootdir}/locale/fr/LC_MESSAGES/*.mo
%lang(hr)%{_datarootdir}/locale/hr/LC_MESSAGES/*.mo
%lang(id)%{_datarootdir}/locale/id/LC_MESSAGES/*.mo
%lang(ja)%{_datarootdir}/locale/ja/LC_MESSAGES/*.mo
%lang(nl)%{_datarootdir}/locale/nl/LC_MESSAGES/*.mo
%lang(ru)%{_datarootdir}/locale/ru/LC_MESSAGES/*.mo
%lang(sr)%{_datarootdir}/locale/sr/LC_MESSAGES/*.mo
%lang(sv)%{_datarootdir}/locale/sv/LC_MESSAGES/*.mo
%lang(tr)%{_datarootdir}/locale/tr/LC_MESSAGES/*.mo
%lang(uk)%{_datarootdir}/locale/uk/LC_MESSAGES/*.mo
%lang(vi)%{_datarootdir}/locale/vi/LC_MESSAGES/*.mo
%lang(zh_CN)%{_datarootdir}/locale/zh_CN/LC_MESSAGES/*.mo
%lang(zh_TW)%{_datarootdir}/locale/zh_TW/LC_MESSAGES/*.mo
#	Man pages
%{_mandir}/man1/*.gz
%{_mandir}/man7/*.gz

%changelog
*	Mon Apr 1 2013 baho-utot <baho-utot@columbus.rr.com> 4.8.0-1
-	Upgrade version 4.8.0
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 4.7.2-1
-	Upgrade version
