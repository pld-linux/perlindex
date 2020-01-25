#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Text
%define		pnam	perlindex
Summary:	perlindex - a program to index and search the Perl documentation
Summary(pl.UTF-8):	perlindex - program do indeksowania i przeszukiwania dokumentacji Perla
Name:		perlindex
Version:	1.606
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pnam}-%{version}.tar.gz
# Source0-md5:	a46ad625934bab8cbb1d7d20b1d5e131
URL:		http://search.cpan.org/dist/perlindex/
BuildRequires:	perl-Term-ReadKey
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
perlindex - a program to index and search the Perl documentation.

%description -l pl.UTF-8
perlindex - program do indeksowania i przeszukiwania dokumentacji
Perla.

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
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Text/English.pm
%{_mandir}/man*/*
