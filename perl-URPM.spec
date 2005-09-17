#
# Conditional build:
%bcond_with	tests	# perform "make test" (these fail on PLD)
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	URPM
Summary:	URPM - module for Perl
Summary(pl):	URPM - modu³ dla Perla
Name:		perl-URPM
Version:	1.27
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
# downloaded from http://fr2.rpmfind.net/linux/MandrakeCooker/cooker/SRPMS/main/
Source0:	%{pnam}-%{version}.tar.bz2
# Source0-md5:	9e63bc780c9582d6c01cba335b182f96
URL:		http://cvs.mandriva.com/cgi-bin/cvsweb.cgi/soft/perl-URPM/
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
%{__make}
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
