#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	URPM
Summary:	URPM module for perl
Name:		perl-URPM
Version:	1.24
Release:	0.1
License:	GPL or Artistic
Group:		Development/Languages/Perl
# downloaded from http://fr2.rpmfind.net/linux/MandrakeCooker/cooker/SRPMS/main/
Source0:	%{pnam}-%{version}.tar.bz2
# Source0-md5:	c7c66a97aa64eac5371cdd1af7c82439
URL:		http://cvs.mandriva.com/cgi-bin/cvsweb.cgi/soft/perl-URPM/
BuildRequires:	bzip2-devel
BuildRequires:	rpm-devel >= 4.2.3
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	packdrake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The URPM module allows you to manipulate rpm files, rpm header files
and hdlist files and manage them in memory.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
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
%{perl_vendorarch}/auto/URPM/URPM.so
%{perl_vendorarch}/auto/URPM/URPM.bs
