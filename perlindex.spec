%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	perlindex
Summary:	Text::German - German grundform reduction
Summary(pl):	Text::German - redukcja niemieckich "Grundformen"
Name:		perlindex
Version:	1.301
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	82e49be7a6e630c4267696ee2f3a27d8
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/Text/English.pm
%{_mandir}/man*/*
