# TODO
# - translations to system dir
%define		status		stable
%define		pearname	Horde_Exception
Summary:	%{pearname} - Horde Exception Handler
Name:		php-horde-Horde_Exception
Version:	1.0.9
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	1463e8ab83849911687105f02aad7863
URL:		https://github.com/horde/horde/tree/master/framework/Exception/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.593
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides the default exception handlers for the Horde
Application Framework.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Exception.php
%{php_pear_dir}/Horde/Exception
%{php_pear_dir}/data/Horde_Exception
