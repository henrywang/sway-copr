Name:		wofi
Version:	1.0
Release:	1%{?dist}
Summary:	Wofi is a launcher/menu program for wlroots based wayland compositors

Group:		User Interface/X
License:	MIT
URL:		https://hg.sr.ht/~scoopta/wofi
Source0:	%{url}/archive/v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:  hg
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(wayland-client)


%description
%{summary}

%prep
%autosetup -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%{_bindir}/wofi
%exclude %{_exec_prefix}/lib/debug/usr/bin/*.debug

%changelog
* Mon Feb 17 2020 Xiaofeng Wang <hernywangxf@me.com> 1.0-1
- Initial RPM release
