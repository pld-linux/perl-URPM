#
# Conditional build:
%bcond_with	tests	# perform "make test" (these fail on PLD)
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	URPM
%define		pdir	perl-URPM
Summary:	URPM - manipulate and manage rpm files, hdlist files and rpm header files
Summary(pl):	URPM - manipulowanie i zarz±dzanie plikami rpm, hdlist i nag³ówkami rpm
Name:		perl-URPM
Version:	1.47
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RG/RGARCIA/%{pnam}-%{version}.tar.gz
# Source0-md5:	aac0b2a6274dfbf4c1acdd59d30f7c8c
URL:		http://search.cpan.org/dist/URPM/
BuildRequires:	bzip2-devel
BuildRequires:	packdrake
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-devel >= 4.2.3
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The URPM module allows you to manipulate rpm files, rpm header files,
hdlist files and manage them in memory.

%description -l pl
Modu³ URPM pozwala na manipulowanie plikami rpm, nag³ówkami plików
rpm, plikami hdlist oraz zarz±dzanie nimi w pamiêci.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%{_mandir}/man3/*
%{perl_vendorarch}/URPM
%{perl_vendorarch}/URPM.pm
%dir %{perl_vendorarch}/auto/URPM
%attr(755,root,root) %{perl_vendorarch}/auto/URPM/URPM.so
%{perl_vendorarch}/auto/URPM/URPM.bs
