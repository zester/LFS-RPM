Summary:	Linux Api header files
Name:		linux-api-headers
Version:	3.8.3
Release:	1
License:	GPLv2
URL:		http://www.kernel.org/
Group:		System Environment/Kernel
Vendor:		Bildanet
Distribution:	Octothorpe
Source:		http://www.kernel.org/pub/linux/kernel/v3.x/linux-%{version}.tar.xz
BuildArch: 	noarch
%description
The Linux API Headers expose the kernel's API for use by Glibc.
%define pkgdir	%{_builddir}/linux-%{version}
%prep
setup -q
%build
make mrproper
make headers_check
%install
rm -rf %{buildroot}/*
make INSTALL_HDR_PATH=dest headers_install
find dest/include \( -name .install -o -name ..install.cmd \) -delete
install -vdm 755 %{buildroot}/usr/include
cp -rv dest/include/* %{buildroot}/usr/include
%clean
rm -rf %{buildroot} %{_builddir}/*
%files
%defattr(-,root,root)
/usr/include/*
%changelog
*	Sun Mar 24 2013 GangGreene <GangGreene@bildanet.com> 3.8.3-1
-	Update version to 3.8.3

*	Sun Mar 24 2013 GangGreene <GangGreene@bildanet.com> 3.8.1-1
-	Update version

*	Wed Jan 30 2013 GangGreene <GangGreene@bildanet.com> 3.5.2-1
-	Initial build.	First version
