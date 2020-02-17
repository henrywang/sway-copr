%define debug_package %{nil}
%define waybar_dir Waybar-%{version}

Name:       waybar
Version:    0.9.1
Release:    1%{?dist}
Summary:    Highly customizable Wayland bar for Sway and Wlroots based compositors.
License:    MIT
Group:      System/GUI/Other
URL:        https://github.com/Alexays/Waybar
Source0:    %{url}/archive/%{version}.tar.gz

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
%set_build_flags
%{shrink:%{__meson} --buildtype=plain --prefix=%{_prefix} --libdir=%{_libdir} --libexecdir=%{_libexecdir} --bindir=%{_bindir} --sbindir=%{_sbindir} --includedir=%{_includedir} --datadir=%{_datadir} --mandir=%{_mandir} --infodir=%{_infodir} --localedir=%{_datadir}/locale --sysconfdir=%{_sysconfdir} --localstatedir=%{_localstatedir} --sharedstatedir=%{_sharedstatedir} --auto-features=%{__meson_auto_features} %{_vpath_srcdir} %{_vpath_builddir} %{nil}}
%meson_build

%install
%meson_install

%post
rm -rf %{_sysconfdir}/xdg/%{name}
rm -f %{_userunitdir}/%{name}.service

# Do not start from systemd, so do not need .service file
# Do not put default style and config in /etc/waybar/
%files
%license LICENSE
%doc README.md
%{_mandir}/man5/waybar*.5*
%{_sysconfdir}/xdg/%{name}
%config(noreplace) %{_sysconfdir}/xdg/%{name}/config
%config(noreplace) %{_sysconfdir}/xdg/%{name}/style.css
%{_bindir}/%{name}
%{_userunitdir}/%{name}.service

%changelog
* Mon Feb 17 2020 Xiaofeng Wang <hernywangxf@me.com> 0.9.1-1
- https://github.com/Alexays/Waybar/releases/tag/0.9.1
* Mon Feb 17 2020 Xiaofeng Wang <hernywangxf@me.com> 0.9.0-1
- Initial RPM release
