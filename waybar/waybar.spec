%define debug_package %{nil}
%define waybar_dir Waybar-%{version}

Name:       waybar
Version:    0.9.1
Release:    1%{?dist}
Summary:    Highly customizable Wayland bar for Sway and Wlroots based compositors.
License:    MIT
Group:      System/GUI/Other
URL:        https://github.com/Alexays/Waybar
Source0:	%{url}/archive/%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	meson
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(gtkmm-3.0) >= 3.22.0
BuildRequires:	pkgconfig(jsoncpp)
BuildRequires:	pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(sigc++-2.0)
BuildRequires:	pkgconfig(libnl-3.0)
BuildRequires:	pkgconfig(libnl-genl-3.0)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(fmt) >= 5.3.0
BuildRequires:	pkgconfig(libmpdclient)
BuildRequires:	git
BuildRequires:	pkgconfig(spdlog) >= 1.3.1
BuildRequires:	pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  scdoc >= 1.9.2
Recommends:     sway
Recommends:     fontawesome-fonts

%description
Highly customizable Wayland bar for Sway and Wlroots based compositors.

%prep
%autosetup -n %{waybar_dir}

%build
%meson
%meson_build

%install
%meson_install
# disable systemd user service by default
%{__mkdir_p} %{buildroot}/%{_userpresetdir}
echo 'disable %{name}.service' >%{buildroot}/%{_userpresetdir}/90-%{name}.preset

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license LICENSE
%doc README.md
%{_mandir}/man5/waybar*.5*
%{_sysconfdir}/xdg/%{name}
%config(noreplace) %{_sysconfdir}/xdg/%{name}/config
%config(noreplace) %{_sysconfdir}/xdg/%{name}/style.css
%{_bindir}/%{name}
%{_userunitdir}/%{name}.service
%{_userpresetdir}/90-%{name}.preset


%changelog
* Mon Feb 17 2020 Xiaofeng Wang <hernywangxf@me.com> 0.9.1-1
- Initial RPM release
