%define		modname ldap_integration
Summary:	Drupal LDAP Integration Module
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.1
License:	?
Group:		Applications/WWW
Source0:	http://wiki.pablobm.com/images/5/51/Ldap_integration-%{version}.tar.gz
# Source0-md5:	ab190ffb43d8365de411b17354e94bb1
URL:		http://drupal.org/node/15109
Requires:	drupal >= 4.6.0
Requires:	php-ldap
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/drupal
%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules

%description
This module allows users to authenticate against a LDAP directory.
Additionally, users can read and modify their data in the LDAP directory, being
the administrator able to limit it.

%prep
%setup -q -n %{modname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_moddir}

cp -a *.module $RPM_BUILD_ROOT%{_moddir}
cp -a %{modname} $RPM_BUILD_ROOT%{_moddir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_moddir}/*.module
%{_moddir}/%{modname}
