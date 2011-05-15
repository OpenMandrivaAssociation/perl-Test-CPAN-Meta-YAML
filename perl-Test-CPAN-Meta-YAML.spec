%define upstream_name    Test-CPAN-Meta-YAML
%define upstream_version 0.17

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Validate META.json elements
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::YAML::Valid)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*


