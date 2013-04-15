Summary:	Basic system utilities
Name:		coreutils
Version:	8.21
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/coreutils
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://ftp.gnu.org/gnu/coreutils/%{name}-%{version}.tar.xz
Patch0:		http://www.linuxfromscratch.org/patches/lfs/7.3/coreutils-8.21-i18n-1.patch
%description
The Coreutils package contains utilities for showing and setting
the basic system
%prep
%setup -q
%patch0 -p1
%build
FORCE_UNSAFE_CONFIGURE=1  ./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr \
	--libexecdir=/usr/lib \
	--enable-no-install-program=kill,uptime
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
install -vdm 755 %{buildroot}/bin
install -vdm 755 %{buildroot}/usr/sbin
install -vdm 755 %{buildroot}/usr/share/man/man8
mv -v %{buildroot}/usr/bin/{cat,chgrp,chmod,chown,cp,date,dd,df,echo} %{buildroot}/bin
mv -v %{buildroot}/usr/bin/{false,ln,ls,mkdir,mknod,mv,pwd,rm} %{buildroot}/bin
mv -v %{buildroot}/usr/bin/{rmdir,stty,sync,true,uname,test,[} %{buildroot}/bin
mv -v %{buildroot}/usr/bin/chroot %{buildroot}/usr/sbin
mv -v %{buildroot}/usr/share/man/man1/chroot.1 %{buildroot}/usr/share/man/man8/chroot.8
sed -i s/\"1\"/\"8\"/1 %{buildroot}/usr/share/man/man8/chroot.8
mv -v %{buildroot}/usr/bin/{head,sleep,nice} %{buildroot}/bin
rm -rf %{buildroot}/usr/share/info
%find_lang %{name}
%check
make -k  NON_ROOT_USERNAME=nobody check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files -f %{name}.lang
%defattr(-,root,root)
/bin/*
/usr/lib/*
/usr/bin/*
/usr/sbin/*
/usr/share/man/*/*
%changelog
*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 0:8.21-1
-	Upgrade version
