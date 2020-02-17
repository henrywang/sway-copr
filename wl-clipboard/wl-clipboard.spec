Name:           wl-clipboard
Version:        2.0.0
Release:        1%{?dist}
Summary:        Wayland clipboard utilities
Group:          User Interface/X
License:        GPL-3.0
URL:            https://github.com/bugaevc/wl-clipboard
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.12
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(libevdev)
Recommends:     xdg-utils
Recommends:     mailcap

%description
wl-clipboard provides two command-line Wayland clipboard utilities, wl-copy and wl-paste, that let you easily copy data between the clipboard and Unix pipes, sockets, files and so on.

%prep
%autosetup -p 1 -n %{name}-%{version}
mkdir %{_target_Platform}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/wl-copy
%{_bindir}/wl-paste
%{_mandir}/man1/*
%{_datadir}/bash-completion/completions/wl-copy
%{_datadir}/bash-completion/completions/wl-paste
%{_datadir}/zsh/site-functions/_wl-copy
%{_datadir}/zsh/site-functions/_wl-paste

%changelog
* Mon Feb 17 2020 Xiaofeng Wang <hernywangxf@me.com> 2.0.0-1
- Initial RPM release
