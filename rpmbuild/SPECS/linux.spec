Summary:	Kernel
Name:		linux
Version:	3.8.5
Release:	1
License:	GPLv2
URL:		http://www.kernel.org/
Group:		System Environment/Kernel
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	http://www.kernel.org/pub/linux/kernel/v3.x/%{name}-%{version}.tar.xz
Source1:	config-%{version}-i686
Source2:	config-%{version}-x86_64
%description
The Linux package contains the Linux kernel.
%prep
%setup -q
%build
make mrproper
%ifarch i386 i486 i586 i686
cp %{SOURCE1} .config
%endif
%ifarch x86_64
cp %{SOURCE2} .config
%endif
make LC_ALL= silentoldconfig
#make LC=ALL= oldconfig
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
install -vdm 755 %{buildroot}/etc
install -vdm 755 %{buildroot}/boot
install -vdm 755 %{buildroot}%{_defaultdocdir}/%{name}-%{version}
install -vdm 755 %{buildroot}/etc/modprobe.d
make INSTALL_MOD_PATH=%{buildroot} modules_install
cp -v arch/x86/boot/bzImage	%{buildroot}/boot/vmlinuz-%{version}
cp -v System.map		%{buildroot}/boot/System.map-%{version}
cp -v .config			%{buildroot}/boot/config-%{version}
cp -r Documentation/*		%{buildroot}%{_defaultdocdir}/%{name}-%{version}

cat > %{buildroot}/etc/modprobe.d/usb.conf << "EOF"
# Begin /etc/modprobe.d/usb.conf

install ohci_hcd /sbin/modprobe ehci_hcd ; /sbin/modprobe -i ohci_hcd ; true
install uhci_hcd /sbin/modprobe ehci_hcd ; /sbin/modprobe -i uhci_hcd ; true

# End /etc/modprobe.d/usb.conf
EOF
#	Cleanup dangling symlinks
rm -rf %{buildroot}/lib/modules/3.8.5/source
rm -rf %{buildroot}/lib/modules/3.8.5/build
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
/boot/System.map-%{version}
/boot/config-%{version}
/boot/vmlinuz-%{version}
%config(noreplace)/etc/modprobe.d/usb.conf
/lib/firmware/*
/lib/modules/*
%{_defaultdocdir}/%{name}-%{version}/*
%changelog
*	Mon Apr 1  2013 baho-utot <baho-utot@columbus.rr.com> 3.8.5-1
-	Upgrade version to 3.8.5

*	Wed Mar 21 2013 baho-utot <baho-utot@columbus.rr.com> 3.8.1-1
-	Upgrade version
