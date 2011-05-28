%define		syntax	iptables
Summary:	Vim syntax: %{syntax}
Name:		vim-syntax-%{syntax}
Version:	1.08
Release:	0.1
License:	Charityware ??
Group:		Applications/Editors/Vim
# Taken from: http://www.vim.org/scripts/script.php?script_id=1425
Source0:	http://www.vim.org/scripts/download_script.php?src_id=15041
# Source0-md5:	cf681cf2095e7978b1a9e49b5292a070
Source1:	vim-ftdetect-%{syntax}.vim
# for _vimdatadir existence
Requires:	vim-rt >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
This vim syntax script highlights files iptables-save and iptables-restore
utilities.

%prep
%setup -q -n syntax

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
install %{syntax}.vim $RPM_BUILD_ROOT%{_vimdatadir}/syntax/%{syntax}.vim
install %{SOURCE1} $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{syntax}.vim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/%{syntax}.vim
%{_vimdatadir}/ftdetect/%{syntax}.vim
