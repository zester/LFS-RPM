Summary:	Contains the utilities for the ext2 file system
Name:		e2fsprogs
Version:	1.42.7
Release:	1
License:	GPLv2
URL:		http://e2fsprogs.sourceforge.net
Group:		LFS/Base
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://prdownloads.sourceforge.net/e2fsprogs/%{name}-%{version}.tar.gz
%description
The E2fsprogs package contains the utilities for handling
the ext2 file system.
%prep
%setup -q
install -vdm 755 build
%build
cd build
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
../configure \
--prefix=%{_prefix} \
--libdir=%{_libdir} \
--with-root-prefix='' \
--enable-elf-shlibs \
--disable-libblkid \
--disable-libuuid \
--disable-uuidd \
--disable-fsck
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
cd build
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install-libs
find %{buildroot}%{_libdir} -name '*.a' -delete
rm -rf %{buildroot}%{_infodir}
%check
cd build
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%config /etc/mke2fs.conf
/sbin/*
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/*
%{_includedir}/*
%lang(ca) %{_datarootdir}/locale/ca/LC_MESSAGES/e2fsprogs.mo
%lang(cs) %{_datarootdir}/locale/cs/LC_MESSAGES/e2fsprogs.mo
%lang(de) %{_datarootdir}/locale/de/LC_MESSAGES/e2fsprogs.mo
%lang(es) %{_datarootdir}/locale/es/LC_MESSAGES/e2fsprogs.mo
%lang(fr) %{_datarootdir}/locale/fr/LC_MESSAGES/e2fsprogs.mo
%lang(id) %{_datarootdir}/locale/id/LC_MESSAGES/e2fsprogs.mo
%lang(it) %{_datarootdir}/locale/it/LC_MESSAGES/e2fsprogs.mo
%lang(nl) %{_datarootdir}/locale/nl/LC_MESSAGES/e2fsprogs.mo
%lang(pl) %{_datarootdir}/locale/pl/LC_MESSAGES/e2fsprogs.mo
%lang(sv) %{_datarootdir}/locale/sv/LC_MESSAGES/e2fsprogs.mo
%lang(tr) %{_datarootdir}/locale/tr/LC_MESSAGES/e2fsprogs.mo
%lang(vi) %{_datarootdir}/locale/vi/LC_MESSAGES/e2fsprogs.mo
%lang(zh_CN) %{_datarootdir}/locale/zh_CN/LC_MESSAGES/e2fsprogs.mo
%{_datarootdir}/et/*
%{_datarootdir}/ss/*
%{_mandir}/*/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 1.42.7-1
-	Upgrade version
