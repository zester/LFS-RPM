Summary:	Kernel
Name:		linux
Version:	3.5.2
Release:	1
License:	GPLv2
URL:		http://www.kernel.org/
Group:		System Environment/Kernel
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.kernel.org/pub/linux/kernel/v3.x/%{name}-%{version}.tar.xz
%description
The Linux package contains the Linux kernel.
%prep
%setup -q
%build
make mrproper
%ifarch i386 i486 i586 i686
cp %{_sourcedir}/config-3.5.2-i686 .config
%endif
%ifarch x86_64
cp %{_sourcedir}/config-3.5.2-x86_64 .config
%endif
make LC_ALL= silentoldconfig
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
install -vdm 755 %{buildroot}/etc
install -vdm 755 %{buildroot}/boot
install -vdm 755 %{buildroot}/usr/share/doc/%{name}-%{version}
install -vdm 755 %{buildroot}/etc/modprobe.d
make INSTALL_MOD_PATH=%{buildroot} modules_install
cp -v arch/x86/boot/bzImage	%{buildroot}/boot/vmlinuz-3.5.2
cp -v System.map		%{buildroot}/boot/System.map-3.5.2
cp -v .config			%{buildroot}/boot/config-3.5.2
cp -r Documentation/*		%{buildroot}//usr/share/doc/%{name}-%{version}
cat > %{buildroot}/etc/modprobe.d/usb.conf << "EOF"
# Begin /etc/modprobe.d/usb.conf

install ohci_hcd /sbin/modprobe ehci_hcd ; /sbin/modprobe -i ohci_hcd ; true
install uhci_hcd /sbin/modprobe ehci_hcd ; /sbin/modprobe -i uhci_hcd ; true

# End /etc/modprobe.d/usb.conf
EOF
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
/boot/System.map-3.5.2
/boot/config-3.5.2
/boot/vmlinuz-3.5.2
%config(noreplace)/etc/modprobe.d/usb.conf
/lib/firmware/*
/lib/modules/*
/usr/share/doc/%{name}-%{version}/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:3.5.2-0
-	Initial build.	First version
