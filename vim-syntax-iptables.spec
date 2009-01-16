%define		syntax	iptables
Summary:	Vim syntax: %{syntax}
Name:		vim-syntax-%{syntax}
Version:	1.06
Release:	0.9
License:	Charityware ??
Group:		Applications/Editors/Vim
# Taken from: http://www.vim.org/scripts/script.php?script_id=1425
Source0:	%{syntax}.vim
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
%setup -qcT
rev=$(awk '/^".*Version:/{print $3}' %{SOURCE0})
if [ "$rev" != "%{version}" ]; then
	: Update version $rev, and retry
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
install %{SOURCE0} $RPM_BUILD_ROOT%{_vimdatadir}/syntax/%{syntax}.vim
install %{SOURCE1} $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{syntax}.vim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/%{syntax}.vim
%{_vimdatadir}/ftdetect/%{syntax}.vim
