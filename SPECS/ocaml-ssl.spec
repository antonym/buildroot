%global debug_package %{nil}

Name:           ocaml-ssl
Version:        0.4.6
Release:        1%{?dist}
Summary:        Use OpenSSL from OCaml
License:        LGPL
Group:          Development/Libraries
URL:            http://downloads.sourceforge.net/project/savonet/ocaml-ssl
Source0:        http://downloads.sourceforge.net/project/savonet/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  openssl-devel

%description
Use OpenSSL from OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       openssl-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
./configure
# --disable-ldconf
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=%{buildroot}


%files
#This space intentionally left blank

%files devel
%doc CHANGES COPYING README
%{_libdir}/ocaml/ssl/*
%{_libdir}/ocaml/stublibs/dllssl_stubs.so
%{_libdir}/ocaml/stublibs/dllssl_stubs.so.owner

%{_libdir}/ocaml/stublibs/dllssl_threads_stubs.so
%{_libdir}/ocaml/stublibs/dllssl_threads_stubs.so.owner

%changelog
* Sun Jun  2 2013 David Scott <dave.scott@eu.citrix.com> - 0.4.6-1
- Initial package

