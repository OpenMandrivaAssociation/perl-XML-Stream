%define modname	XML-Stream
%define modver	1.23

Summary:	%{modname} perl module
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	18
License:	LGPLv2
Group:		Development/Perl
Url:		http://www.cpan.org/
Source0:	http://www.cpan.org/modules/by-module/XML/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-Unicode-String
BuildRequires:	perl-Authen-SASL
BuildRequires:	perl(Test::More)

%description
This module provides you with access to XML Streams.  An XML Stream
is just that.  A stream of XML over a connection between two computers.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor 
%make_build

%check
make test

%install
%make_install

%files
%doc README CHANGES
%{perl_vendorlib}/XML/*
%doc %{_mandir}/man3/*
