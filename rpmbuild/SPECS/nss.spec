Summary:	Security client
Name:		nss
Version:	3.14.3
Release:	1
License:	MPLv2.0
URL:		http://ftp.mozilla.org/pub/mozilla.org/security/nss
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/NSS_3_14_RTM/src/%{name}-%{version}.tar.gz
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
#patch -Np1 -i %{_sourcedir}/nss-3.14.3-standalone-1.patch
%build
cd mozilla/security/nss
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
make nss_build_all BUILD_OPT=1 \
	NSPR_INCLUDE_DIR=/usr/include/nspr \
	USE_SYSTEM_ZLIB=1 \
	ZLIB_LIBS=-lz \
	$([ $(uname -m) = x86_64 ] && echo USE_64=1) \
	$([ -f /usr/include/sqlite3.h ] && echo NSS_USE_SYSTEM_SQLITE=1)
%install
rm -rf %{buildroot}
cd mozilla/security/nss
cd ../../dist
install -vdm 755 %{buildroot}/usr/bin
install -vdm 755 %{buildroot}/usr/include/nss
install -vdm 755 %{buildroot}/usr/lib
install -v -m755 Linux*/lib/*.so %{buildroot}/usr/lib
install -v -m644 Linux*/lib/{*.chk,libcrmf.a} %{buildroot}/usr/lib
cp -v -RL {public,private}/nss/* %{buildroot}/usr/include/nss
chmod 644 %{buildroot}/usr/include/nss/*
install -v -m755 Linux*/bin/{certutil,nss-config,pk12util} %{buildroot}/usr/bin
install -vdm 755 %{buildroot}/usr/lib/pkgconfig
install -vm 644 Linux*/lib/pkgconfig/nss.pc %{buildroot}/usr/lib/pkgconfig
find %{buildroot}/usr/lib/ -name '*.a' -delete
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%files
%defattr(-,root,root)
/usr/bin/*
/usr/include/*
/usr/lib/*
%changelog
*	Wed Mar 21 2013 GangGreene <GangGreene@bildanet.com> 0:3.14.3-1
-	Upgrade version
