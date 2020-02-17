Name:		slurp
Version:	1.2.0
Release:	1%{?dist}
Summary:	Select a region in a Wayland compositor

Group:		User Interface/X
License:	MIT
URL:		https://github.com/emersion/slurp
Source0:	%{url}/archive/v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:  meson >= 0.48.0
BuildRequires:  scdoc
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(cairo)
Recommends:     sway
Recommends:     grim

%description
Select a region in a Wayland compositor and print it to the standard output.

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
%{_bindir}/slurp
%{_mandir}/man1/slurp*.1*

%changelog
* Mon Feb 17 2020 Xiaofeng Wang <hernywangxf@me.com> 1.2.0-1
- Initial RPM release
