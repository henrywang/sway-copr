Name:		kanshi
Version:	1.0.0
Release:	1%{?dist}
Summary:	Wayland equivalent for autorandr

License:	MIT
URL:		https://github.com/emersion/kanshi
Source0:	%{url}/archive/v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson >= 0.47.0
BuildRequires: 	pkgconfig(wayland-client)
BuildRequires:	scdoc >= 1.9.2
Recommends:	sway

%description
kanshi allows you to define output profiles that are automatically enabled and disabled on hotplug.

%prep
%autosetup -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/kanshi
%{_mandir}/man1/kanshi*.1*
%{_mandir}/man5/kanshi*.5*

%changelog
* Mon Feb 17 2020 Xiaofeng Wang <hernywangxf@me.com> 1.0.0-1
- Initial RPM release
