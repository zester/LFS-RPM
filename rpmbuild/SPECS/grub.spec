Summary:	GRand Unified Bootloader
Name:		grub
Version:	2.00
Release:	1
License:	GPLv3
URL:		http://www.gnu.org/software/grub
Group:		Applications/System
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://ftp.gnu.org/gnu/grub/%{name}-%{version}.tar.xz
%description
The GRUB package contains the GRand Unified Bootloader.
%prep
%setup -q
sed -i -e '/gets is a/d' grub-core/gnulib/stdio.in.h
%build
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr \
	--sysconfdir=/etc \
	--disable-grub-emu-usb \
	--disable-efiemu \
	--disable-werror
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/share/info
%find_lang %{name}
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%clean
rm -rf %{buildroot}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files -f %{name}.lang
%defattr(-,root,root)
%dir /etc/grub.d
%config(noreplace) /etc/bash_completion.d/grub
%config(noreplace) /etc/grub.d/00_header
%config(noreplace) /etc/grub.d/10_linux
%config(noreplace) /etc/grub.d/20_linux_xen
%config(noreplace) /etc/grub.d/30_os-prober
%config(noreplace) /etc/grub.d/40_custom
%config(noreplace) /etc/grub.d/41_custom
%config(noreplace) /etc/grub.d/README
/usr/bin/*
/usr/lib/*
/usr/sbin/*
/usr/share/%{name}/*
%changelog
*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 0:2.00-0
-	Initial build.	First version
