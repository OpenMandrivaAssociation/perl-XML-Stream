%define upstream_name 	 XML-Stream
%define upstream_version 1.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	%{upstream_name} perl module
License: 	LGPL
Group:		Development/Perl
Url:		http://www.cpan.org/
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-Unicode-String
BuildRequires:	perl-Authen-SASL
BuildArch:	noarch

%description
This module provides you with access to XML Streams.  An XML Stream
is just that.  A stream of XML over a connection between two computers.

%prep
%setup -q  -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor 
make

%check
make test

%install
%makeinstall_std

%files
%doc README CHANGES
%{_mandir}/*/*
%{perl_vendorlib}/XML/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.230.0-4mdv2012.0
+ Revision: 765854
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.230.0-2
+ Revision: 667459
- mass rebuild

* Fri Jan 08 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.230.0-1mdv2011.0
+ Revision: 487478
- update to 1.23

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.220.0-1mdv2010.0
+ Revision: 401851
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.22-6mdv2009.1
+ Revision: 351659
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.22-5mdv2009.0
+ Revision: 224665
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.22-4mdv2008.1
+ Revision: 180661
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.22-3mdv2008.0
+ Revision: 23245
- rebuild


* Sun Nov 28 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.22-2mdk
- add BuildRequires: perl-Authen-SASL (for tests)

* Wed Nov 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.22-1mdk
- 1.22

* Tue Apr 20 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.21-2mdk
- fix license

* Mon Apr 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.21-1mdk
- 1.21
- drop PREFIX and use %%makeinstall_std macro
- change license to GNU Library GPL

* Tue Aug 12 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.16-3mdk
- rebuild

* Sun Jul 27 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 1.16-2mdk
- rebuild for new rpm provides computation

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.16-1mdk
- update for Net::Jabber

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.15-5mdk
- rebuild for new auto{prov,req}

* Mon May 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.15-4mdk
- buildrequires

* Thu Jan 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.15-3mdk
- rebuild

* Wed Jul 10 2002 Pixel <pixel@mandrakesoft.com> 1.15-2mdk
- rebuild for perl 5.8.0

* Tue Jun 18 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.15-1mdk
- updated by David Walser <luigiwalser@yahoo.com> :
	- 1.15

* Mon Mar 04 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.14-1mdk
- 1.14

* Wed Aug 29 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.12-2mdk
- add buildrequires ( Christian Zoffoli )

* Thu Aug 23 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.12-1mdk
- updated to 1.12

* Tue Feb 20 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.11-1mdk
- added in contribs by Christian Zoffoli <czoffoli@linux-mandrake.com> :
	- First Mandrake Release

