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
tar xvf %{SOURCE0}
cd %{_builddir}/%{name}73
echo '#define SYS_VIMRC_FILE "/etc/vimrc"' >> src/feature.h
%build
cd %{_builddir}/%{name}73
./configure \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--enable-multibyte
make %{?_smp_mflags}
%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
cd %{_builddir}/%{name}73
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
ln -sv %{buildroot}%{_bindir}/vi
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
%{_bindir}/*
%{_mandir}/*/
%{_datarootdir}/vim/vim73/autoload/*
%{_datarootdir}/vim/vim73/bugreport.vim
%{_datarootdir}/vim/vim73/colors/*
%{_datarootdir}/vim/vim73/compiler/*
%{_datarootdir}/vim/vim73/delmenu.vim
%doc %{_datarootdir}/vim/vim73/doc/*
%{_datarootdir}/vim/vim73/evim.vim
%{_datarootdir}/vim/vim73/filetype.vim
%{_datarootdir}/vim/vim73/ftoff.vim
%{_datarootdir}/vim/vim73/ftplugin.vim
%{_datarootdir}/vim/vim73/ftplugin/*
%{_datarootdir}/vim/vim73/ftplugof.vim
%{_datarootdir}/vim/vim73/gvimrc_example.vim
%{_datarootdir}/vim/vim73/indent.vim
%{_datarootdir}/vim/vim73/indent/*
%{_datarootdir}/vim/vim73/indoff.vim
%{_datarootdir}/vim/vim73/keymap/*
%{_datarootdir}/vim/vim73/macros/*
%{_datarootdir}/vim/vim73/menu.vim
%{_datarootdir}/vim/vim73/mswin.vim
%{_datarootdir}/vim/vim73/optwin.vim
%{_datarootdir}/vim/vim73/plugin/*
%{_datarootdir}/vim/vim73/synmenu.vim
%{_datarootdir}/vim/vim73/vimrc_example.vim
%{_datarootdir}/vim/vim73/print/*
%{_datarootdir}/vim/vim73/scripts.vim
%{_datarootdir}/vim/vim73/spell/*
%{_datarootdir}/vim/vim73/syntax/*
%{_datarootdir}/vim/vim73/tools/*
%{_datarootdir}/vim/vim73/tutor/*
%lang(af) %{_datarootdir}/vim/vim73/lang/af/LC_MESSAGES/vim.mo
%lang(ca) %{_datarootdir}/vim/vim73/lang/ca/LC_MESSAGES/vim.mo
%lang(cs) %{_datarootdir}/vim/vim73/lang/cs/LC_MESSAGES/vim.mo
%lang(de) %{_datarootdir}/vim/vim73/lang/de/LC_MESSAGES/vim.mo
%lang(eb_GB) %{_datarootdir}/vim/vim73/lang/en_GB/LC_MESSAGES/vim.mo
%lang(eo) %{_datarootdir}/vim/vim73/lang/eo/LC_MESSAGES/vim.mo
%lang(es) %{_datarootdir}/vim/vim73/lang/es/LC_MESSAGES/vim.mo
%lang(fi) %{_datarootdir}/vim/vim73/lang/fi/LC_MESSAGES/vim.mo
%lang(fr) %{_datarootdir}/vim/vim73/lang/fr/LC_MESSAGES/vim.mo
%lang(ga) %{_datarootdir}/vim/vim73/lang/ga/LC_MESSAGES/vim.mo
%lang(it) %{_datarootdir}/vim/vim73/lang/it/LC_MESSAGES/vim.mo
%lang(ja) %{_datarootdir}/vim/vim73/lang/ja/LC_MESSAGES/vim.mo
%lang(ko.UTF-8) %{_datarootdir}/vim/vim73/lang/ko.UTF-8/LC_MESSAGES/vim.mo
%lang(ko) %{_datarootdir}/vim/vim73/lang/ko/LC_MESSAGES/vim.mo
%lang(nb) %{_datarootdir}/vim/vim73/lang/nb/LC_MESSAGES/vim.mo
%lang(no) %{_datarootdir}/vim/vim73/lang/no/LC_MESSAGES/vim.mo
%lang(pl) %{_datarootdir}/vim/vim73/lang/pl/LC_MESSAGES/vim.mo
%lang(pt_BR) %{_datarootdir}/vim/vim73/lang/pt_BR/LC_MESSAGES/vim.mo
%lang(ru) %{_datarootdir}/vim/vim73/lang/ru/LC_MESSAGES/vim.mo
%lang(sk) %{_datarootdir}/vim/vim73/lang/sk/LC_MESSAGES/vim.mo
%lang(sv) %{_datarootdir}/vim/vim73/lang/sv/LC_MESSAGES/vim.mo
%lang(uk) %{_datarootdir}/vim/vim73/lang/uk/LC_MESSAGES/vim.mo
%lang(vi) %{_datarootdir}/vim/vim73/lang/vi/LC_MESSAGES/vim.mo
%lang(zh_CN.UTF-8) %{_datarootdir}/vim/vim73/lang/zh_CN.UTF-8/LC_MESSAGES/vim.mo
%lang(zh_CN) %{_datarootdir}/vim/vim73/lang/zh_CN/LC_MESSAGES/vim.mo
%lang(zh_TW.UTF-8) %{_datarootdir}/vim/vim73/lang/zh_TW.UTF-8/LC_MESSAGES/vim.mo
%lang(zh_TW) %{_datarootdir}/vim/vim73/lang/zh_TW/LC_MESSAGES/vim.mo
%{_datarootdir}/vim/vim73/lang/*.vim
%doc %{_datarootdir}/vim/vim73/lang/*.txt
%changelog
*	Wed Jan 30 2013 baho-utot <baho-utot@columbus.rr.com> 7.3-1
-	Initial build.	First version
