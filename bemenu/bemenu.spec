Name:		bemenu
Version:	0.3.0
Release:	1%{?dist}
Summary:	Dynamic menu library and client program inspired by dmenu

Group:		User Interface
License:	GPLv3
URL:		https://github.com/Cloudef/bemenu
Source0:	%{url}/archive/%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	cmake
BuildRequires:	doxygen
# Curses deps
BuildRequires:	pkgconfig(ncursesw)
# Wayland Deps
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(xkbcommon)
# X11 deps
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
# Common deps
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)

%description
%{summary}

#0.3.0 uses cmake, future versions will only use make
%prep
%autosetup

%build
%cmake -DBEMENU_WAYLAND_RENDERER=ON .
make
#make doxygen

%install
%make_install

%files
%license LICENSE-CLIENT LICENSE-LIB
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-run
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.3.0
%{_mandir}/man1/%{name}*.1*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{name}-renderer-curses.so
%{_libdir}/%{name}/%{name}-renderer-wayland.so
%{_libdir}/%{name}/%{name}-renderer-x11.so
%exclude %{_includedir}/%{name}.h

%changelog
* Mon Feb 17 2020 Xiaofeng Wang <henrywangxf@me.com> 0.3.0-1
- Initial RPM Release
