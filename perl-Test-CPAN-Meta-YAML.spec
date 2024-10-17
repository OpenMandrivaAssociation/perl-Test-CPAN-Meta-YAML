%define upstream_name    Test-CPAN-Meta-YAML
%define upstream_version 0.22

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Validate META.json elements
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-CPAN-Meta-YAML-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::YAML::Valid)
BuildArch:	noarch

%description
This module was written to ensure that a META.yml file, provided with a
standard distribution uploaded to CPAN, meets the specifications that
slowly being introduced to module uploads, via the use of the
ExtUtils::MakeMaker manpage, the Module::Build manpage and the
Module::Install manpage.

See the CPAN::Meta manpage for further details of the CPAN Meta
Specification.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun May 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.170.0-1mdv2011.0
+ Revision: 674855
- import perl-Test-CPAN-Meta-YAML



