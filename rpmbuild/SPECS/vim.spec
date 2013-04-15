Summary:	Text editor
Name:		vim
Version:	7.3
Release:	1
License:	Charityware
URL:		http://www.vim.org
Group:		Applications/Editors
Vendor:		Bildanet
Distribution:	Octothorpe
Source0:	ftp://ftp.vim.org/pub/vim/unix/%{name}-%{version}.tar.bz2
%description
The Vim package contains a powerful text editor.
%prep
rm -rf %{_builddir}/*
cd %{_builddir}
tar xvf %{_sourcedir}/%{name}-%{version}.tar.bz2
cd %{_builddir}/%{name}73
echo '#define SYS_VIMRC_FILE "/etc/vimrc"' >> src/feature.h
%build
cd %{_builddir}/%{name}73
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=/usr \
	--enable-multibyte
make %{?_smp_mflags}
%install
cd %{_builddir}/%{name}73
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
ln -sv %{buildroot}/usr/bin/vi
install -vdm 755 %{buildroot}/etc
cat > %{buildroot}/etc/vimrc << "EOF"
" Begin /etc/vimrc

set nocompatible
set backspace=2
set ruler
syntax on
if (&term == "iterm") || (&term == "putty")
  set background=dark
endif

" End /etc/vimrc
EOF
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root)
%config(noreplace) /etc/vimrc
/usr/bin/*
/usr/share/man/*/*
/usr/share/vim
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 0:73-0
-	Initial build.	First version
