Name:           swaylock
Version:        1.5
Release:        1%{?dist}
Summary:        Screen locker for Wayland

License:        MIT
URL:            https://github.com/swaywm/swaylock
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  clang
BuildRequires:  meson >= 0.48.0
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pam-devel
BuildRequires:  scdoc

Requires:       cairo
Requires:       gdk-pixbuf2


%description
swaylock is a screen locking utility for Wayland compositors.


%prep
%autosetup


%build
%meson -Dwerror=false -Dfish-completions=false
%meson_build


%install
%meson_install


%check
%meson_test

%files
%license LICENSE
%doc README.*
%{_bindir}/swaylock
%{_datadir}/bash-completion/completions/swaylock
%exclude %{_datadir}/fish/completions/swaylock.fish
%{_datadir}/zsh/site-functions/_swaylock
%{_mandir}/man1/swaylock.1.gz
%config %{_sysconfdir}/pam.d/swaylock


%changelog
* Thu Jan 30 2020 João Pinto <jpinto@barcodeu.com> 1.5-1
- Initial RPM release