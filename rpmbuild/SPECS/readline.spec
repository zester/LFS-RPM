Summary:	Command-line editing and history capabilities
Name:		readline
Version:	6.2
Release:	1
License:	GPLv3
URL:		http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/readline/%{name}-%{version}.tar.gz
Patch:		http://www.linuxfromscratch.org/patches/lfs/7.2/readline-6.2-fixes-1.patch
%description
The Readline package is a set of libraries that offers command-line
editing and history capabilities.
%prep
%setup -q
sed -i '/MV.*old/d' Makefile.in
sed -i '/{OLDSUFF}/c:' support/shlib-install
%patch -p1
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=/lib
make %{?_smp_mflags} SHLIB_LIBS=-lncurses
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}%{_libdir}
mv -v %{buildroot}/lib/lib{readline,history}.a %{buildroot}%{_libdir}
rm -v %{buildroot}/lib/lib{readline,history}.so
ln -sfv ../../lib/libreadline.so.6	%{buildroot}%{_libdir}/libreadline.so
ln -sfv ../../lib/libhistory.so.6	%{buildroot}%{_libdir}/libhistory.so
install -vdm 755 %{buildroot}%{_defaultdocdir}/%{name}-%{version}
install -v -m644 doc/*.{ps,pdf,html,dvi} \
		 %{buildroot}%{_defaultdocdir}/%{name}-%{version}
rm -rf %{buildroot}%{_infodir}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/lib/*
%{_includedir}/*
%{_libdir}/*
%{_mandir}/*/*
%{_defaultdocdir}/%{name}-%{version}/*
%{_datarootdir}/%{name}/*
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 0:6.2-0
-	Initial build.	First version
