Name:           swayidle
Version:        1.6
Release:        1%{?dist}
Summary:        Idle management daemon for Wayland

License:        MIT
URL:            https://github.com/swaywm/swayidle
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  meson >= 0.48.0
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  scdoc


%description
This is sway's idle management daemon, swayidle. It is compatible
with any Wayland compositor which implements the KDE idle protocol.

%prep
%autosetup


%build
%meson -Dwerror=false -Dfish-completions=false -Dlogind-provider=systemd
%meson_build

%install
%meson_install


%check
%meson_test


%files
%license LICENSE
%doc README.*
%{_bindir}/swayidle
%{_datadir}/bash-completion/completions/swayidle
%exclude %{_datadir}/fish/completions/swayidle.fish
%{_datadir}/zsh/site-functions/_swayidle

%{_mandir}/man1/swayidle.1.gz

%changelog
* Mon Feb 17 2020 Xiaofeng Wang <hernywangxf@me.com> 1.6-1
- Initial RPM release
