Name:           wlroots
Version:        0.10.0
Release:        1%{?dist}
Summary:        A modular Wayland compositor library

License:        MIT
URL:            https://github.com/swaywm/%{name}
Source0:        %{url}/archive/%{version}.tar.gz

# Build Deps

BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  git
BuildRequires:  meson >= 0.51.2
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdrm) >= 2.4.95
BuildRequires:  pkgconfig(libinput) >= 1.9.0
BuildRequires:  pkgconfig(libsystemd) >= 237
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(wayland-server) >= 1.16
BuildRequires:  pkgconfig(xkbcommon)
#BuildRequires:  pkgconfig(xcb-errors)
#BuildRequires:  pkgconfig(freerdp2)

# Runtime Deps

Requires:       libwayland-client >= 1.16
Requires:       libwayland-server >= 1.16
Requires:       libwayland-egl >= 1.16

# Packages provided

Provides:       wlroots = %{version}-%{release}

%description
Pluggable, composable, unopinionated modules for building a Wayland compositor;
or about 50,000 lines of code you were going to write anyway.

%package     devel
Summary:     Development files of wlroots

Requires:    %{name}%{?_isa} == %{version}-%{release}
Requires:    wayland-devel
Requires:    wayland-protocols-devel
Requires:    egl-wayland-devel
Requires:    mesa-libEGL-devel
Requires:    mesa-libGLES-devel
Requires:    mesa-libgbm-devel
Requires:    libdrm-devel
Requires:    libinput-devel
Requires:    libxkbcommon-devel
Requires:    libgudev-devel
Requires:    pixman-devel
Requires:    systemd-devel

Provides:    pkgconfig(wlroots) = %{version}

%description devel
Pluggable, composable, unopinionated modules for building a Wayland compositor;
or about 50,000 lines of code you were going to write anyway.

%prep
%autosetup -v -n %{name}-%{version}

# Remove all .gitignore files
%{_bindir}/find %{_builddir}/%{name}-%{version} -name '.gitignore' -delete

%build
%meson -Dwerror=false -Dxcb-errors=disabled
%meson_build


%install
%meson_install

# %%doc && examples.
%{__mkdir} -p %{buildroot}%{_pkgdocdir}
%{__cp} -pr README.md examples %{buildroot}%{_pkgdocdir}

# Cleanup.
for f in '.*ignore*' meson.build; do
  %{_bindir}/find %{buildroot} -type f -name "$f" -print -delete
done


%check
%meson_test


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.md
%license LICENSE
%{_libdir}/lib%{name}.so.*

%license LICENSE
%doc README.md


%files          devel
%doc %{_pkgdocdir}/examples
%{_includedir}/wlr
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon Feb 17 2020 Xiaofeng Wang <hernywangxf@me.com> 0.10.0-1
- Initial RPM release
