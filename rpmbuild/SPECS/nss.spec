Summary:	Security client
Name:		nss
Version:	3.14.3
Release:	1
License:	MPLv2.0
URL:		http://ftp.mozilla.org/pub/mozilla.org/security/nss
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/NSS_3_14_3_RTM/src/nss-3.14.3.tar.gz
Patch:		http://www.linuxfromscratch.org/patches/blfs/svn/nss-3.14.3-standalone-1.patch
%description
 The Network Security Services (NSS) package is a set of libraries
 designed to support cross-platform development of security-enabled
 client and server applications. Applications built with NSS can
 support SSL v2 and v3, TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12,
 S/MIME, X.509 v3 certificates, and other security standards.
 This is useful for implementing SSL and S/MIME or other Internet
 security standards into an application.
%prep
rm -rf %{_builddir}/*
%setup -q
%patch -p1
%build
cd mozilla/security/nss
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
make nss_build_all BUILD_OPT=1 \
	NSPR_INCLUDE_DIR=%{_includedir}/nspr \
	USE_SYSTEM_ZLIB=1 \
	ZLIB_LIBS=-lz \
	$([ $(uname -m) = x86_64 ] && echo USE_64=1) \
	$([ -f %{_includedir}/sqlite3.h ] && echo NSS_USE_SYSTEM_SQLITE=1)
%install
rm -rf %{buildroot}
cd mozilla/security/nss
cd ../../dist
install -vdm 755 %{buildroot}%{_bindir}
install -vdm 755 %{buildroot}%{_includedir}/nss
install -vdm 755 %{buildroot}%{_libdir}
install -v -m755 Linux*/lib/*.so %{buildroot}%{_libdir}
install -v -m644 Linux*/lib/{*.chk,libcrmf.a} %{buildroot}%{_libdir}
cp -v -RL {public,private}/nss/* %{buildroot}%{_includedir}/nss
chmod 644 %{buildroot}%{_includedir}/nss/*
install -v -m755 Linux*/bin/{certutil,nss-config,pk12util} %{buildroot}%{_bindir}
install -vdm 755 %{buildroot}%{_libdir}/pkgconfig
install -vm 644 Linux*/lib/pkgconfig/nss.pc %{buildroot}%{_libdir}/pkgconfig
find %{buildroot}%{_libdir} -name '*.a' -delete
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 3.14.3-1
-	Upgrade version
