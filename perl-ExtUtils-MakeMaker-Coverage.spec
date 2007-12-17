%define module	ExtUtils-MakeMaker-Coverage
%define name	perl-%{module}
%define version 0.05
%define release %mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Add a Makefile target to determine test coverage using Devel::Cover
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/S/SM/SMPETERS/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildArch:	noarch
Requires:	perl-Devel-Cover
BuildRequires:	perl-Devel-Cover
BuildRequires:	perl-Object-Accessor
BuildRequires:	perl-Test-Differences
BuildRequires:	perl-Test-Pod-Coverage
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Requires:	perl-Object-Accessor


%description
This module adds an additional target to the Makefile generated by
ExtUtils::MakeMaker. The target, testcover, calls cover, the command-line
script to generate test coverage statistics, to clean up any data from a
previous run. It then runs the tests, as if make test was run, then calls cover
again to generate the coverage statistics.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/ExtUtils
%{_mandir}/*/*
%{_bindir}/*

