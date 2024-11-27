Name:           snpguest
Version:        0.8.0
Release:        1%{?dist}
Summary:        CLI tool for interacting with SEV-SNP guest environment

License:        ASL 2.0
URL:            https://github.com/virtee/snpguest

# snpguest sources
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}-vendor.tar.gz

ExclusiveArch:  x86_64
BuildRequires:  rust-toolset
BuildRequires:  openssl-devel

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}
%cargo_prep -V 1

%build
%cargo_build

%install
%cargo_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Tue Nov 26 2024 Tyler Fanelli <tfanelli@redhat.com>
- Initial package
