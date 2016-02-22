%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global npm_name has-ansi

Summary:       Check if a string has ANSI escape codes
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       2.0.0
Release:       5%{?dist}
License:       MIT
URL:           https://github.com/sindresorhus/has-ansi
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs010-runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Check if a string has ANSI escape codes

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%files
%doc license readme.md
%{nodejs_sitelib}/%{npm_name}

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-5
- rebuilt

* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-4
- Invoke find_provides_and_requires macro

* Mon Jan 11 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-3
- Enable scl macros

* Mon Sep 14 2015 Troy Dawson <tdawson@redhat.com> - 2.0.0-1
- Initial package
