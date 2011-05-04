%define upstream_name 	 XML-Stream
%define upstream_version 1.23

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 2

Summary:	%{upstream_name} perl module
License: 	LGPL
Group:		Development/Perl
Url:		http://www.cpan.org/
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires:	perl-Unicode-String
BuildRequires:	perl-Authen-SASL
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides you with access to XML Streams.  An XML Stream
is just that.  A stream of XML over a connection between two computers.

%prep
%setup -q  -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%{__make}

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES
%{_mandir}/*/*
%{perl_vendorlib}/XML/*
