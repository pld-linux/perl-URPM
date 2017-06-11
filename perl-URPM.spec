#
# Conditional build:
%bcond_with	tests	# perform "make test" (these fail on PLD)
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	URPM
%define		pdir	perl-URPM
Summary:	URPM - manipulate and manage rpm files, hdlist files and rpm header files
Summary(pl.UTF-8):	URPM - manipulowanie i zarządzanie plikami rpm, hdlist i nagłówkami rpm
Name:		perl-URPM
Version:	4.43
Release:	9
License:	GPL v2+ or Artistic
Group:		Development/Languages/Perl
Source0:	%{pnam}-%{version}.tar.xz
# Source0-md5:	3a7d80c2f708339fef0055cae9b0f799
URL:		https://abf.rosalinux.ru/omv_software/perl-URPM
BuildRequires:	bzip2-devel
BuildRequires:	perl-MDV-Packdrakeng
BuildRequires:	perl-List-MoreUtils >= 0.32
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-devel >= 5.4
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	rpm
Requires:	perl(MDV::Packdrakeng)
Conflicts:	rpm < 5.3
Conflicts:	urpmi < 6.44
Provides:	perl(URPM::Build) = %{version}-%{release}
Provides:	perl(URPM::Resolve) = %{version}-%{release}
Provides:	perl(URPM::Signature) = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The URPM module allows you to manipulate rpm files, rpm header files,
hdlist files and manage them in memory.

%description -l pl.UTF-8
Moduł URPM pozwala na manipulowanie plikami rpm, nagłówkami plików
rpm, plikami hdlist oraz zarządzanie nimi w pamięci.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
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
