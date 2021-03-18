#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Module-Starter
Version  : 1.77
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Module-Starter-1.77.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Module-Starter-1.77.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmodule-starter-perl/libmodule-starter-perl_1.750+dfsg-1.debian.tar.xz
Summary  : 'a simple starter kit for any module'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Module-Starter-bin = %{version}-%{release}
Requires: perl-Module-Starter-man = %{version}-%{release}
Requires: perl-Module-Starter-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Runtime)
BuildRequires : perl-Software-License

%description
NAME
Module::Starter - a simple starter kit for any module
Module::Starter is used to create a skeletal CPAN distribution,
including basic builder scripts, tests, documentation, and module code.

%package bin
Summary: bin components for the perl-Module-Starter package.
Group: Binaries

%description bin
bin components for the perl-Module-Starter package.


%package dev
Summary: dev components for the perl-Module-Starter package.
Group: Development
Requires: perl-Module-Starter-bin = %{version}-%{release}
Provides: perl-Module-Starter-devel = %{version}-%{release}
Requires: perl-Module-Starter = %{version}-%{release}

%description dev
dev components for the perl-Module-Starter package.


%package man
Summary: man components for the perl-Module-Starter package.
Group: Default

%description man
man components for the perl-Module-Starter package.


%package perl
Summary: perl components for the perl-Module-Starter package.
Group: Default
Requires: perl-Module-Starter = %{version}-%{release}

%description perl
perl components for the perl-Module-Starter package.


%prep
%setup -q -n Module-Starter-1.77
cd %{_builddir}
tar xf %{_sourcedir}/libmodule-starter-perl_1.750+dfsg-1.debian.tar.xz
cd %{_builddir}/Module-Starter-1.77
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Module-Starter-1.77/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/module-starter

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::Starter.3
/usr/share/man/man3/Module::Starter::App.3
/usr/share/man/man3/Module::Starter::BuilderSet.3
/usr/share/man/man3/Module::Starter::Plugin.3
/usr/share/man/man3/Module::Starter::Plugin::Template.3
/usr/share/man/man3/Module::Starter::Simple.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/module-starter.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Module/Starter.pm
/usr/lib/perl5/vendor_perl/5.32.1/Module/Starter/App.pm
/usr/lib/perl5/vendor_perl/5.32.1/Module/Starter/BuilderSet.pm
/usr/lib/perl5/vendor_perl/5.32.1/Module/Starter/Plugin.pod
/usr/lib/perl5/vendor_perl/5.32.1/Module/Starter/Plugin/Template.pm
/usr/lib/perl5/vendor_perl/5.32.1/Module/Starter/Simple.pm
