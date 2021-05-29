%global commit cd266fa22fc2dd848943542686fc7c31bb03bd96
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global upstream_github gnachman
%global upstream_name iterm2-website

Name:           iterm2-utilities
Version:        0
Release:        0.1.20210529git%{shortcommit}%{?dist}
Summary:        iTerm2 Shell Utilities
License:        GPLv2
URL:            https://iterm2.com/documentation-utilities.html
BuildArch:      noarch
Source0:        https://github.com/%{upstream_github}/%{upstream_name}/archive/%{commit}/%{upstream_name}-%{shortcommit}.tar.gz


%description
Collection of shell scripts that help you take advantage of
some of unique features of iTerm2.


%prep
%autosetup -n %{upstream_name}-%{commit}


%build
# nothing to do

%install
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}
%{__install} -m755 source/utilities/* $RPM_BUILD_ROOT%{_bindir}


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/*


%changelog
* Fri May 28 2021 Danila Vershinin <info@getpagespeed.com> 0-0.1.20210528gitcd266fa
- Initial packaging