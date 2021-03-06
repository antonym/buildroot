%global debug_package %{nil}

Name:           ocaml-yojson
Version:        1.1.6
Release:        1%{?dist}
Summary:        A JSON parser and priter for OCaml
License:        BSD3
Group:          Development/Libraries
URL:            http://mjambon.com/yojson.html
Source0:        http://mjambon.com/releases/yojson/yojson-%{version}.tar.gz
BuildRequires:  cppo
BuildRequires:  ocaml
BuildRequires:  ocaml-biniou-devel
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-findlib

%description
A JSON parser and printer for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-biniou-devel%{?_isa}
Requires:       ocaml-easy-format-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n yojson-%{version}

%build
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_bindir}
make install DESTDIR=%{buildroot} BINDIR=%{buildroot}/%{_bindir}


%files
#This space intentionally left blank

%files devel
%doc README.md LICENSE
%{_libdir}/ocaml/yojson/*
%{_bindir}/ydump

%changelog
* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 1.1.6-1
- Initial package

