Name:   	grim
Version:	1.3.0
Release:	1%{?dist}
Summary:	Grab images from a Wayland compositor

Group:		User Interface/X
License:	MIT
URL:		https://github.com/emersion/grim
Source0:	%{url}/archive/v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:  meson >= 0.48.0
BuildRequires:  scdoc
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(cairo)
Recommends:     sway
Recommends:     slurp

%description
Grab images from a Wayland compositor. Works great with slurp and with sway >= 1.0.

%prep
%autosetup -p 1 -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/grim
%{_mandir}/man1/grim*.1*

%changelog
* Mon Feb 17 2020 Xiaofeng Wang <hernywangxf@me.com> 1.3.0-1
- Initial RPM release
