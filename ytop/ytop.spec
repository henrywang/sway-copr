Name:		ytop
Version:	0.5.1
Release:	1%{?dist}
Summary:	TUI based system monitor in Rust

Group: 		Applications/System
License:	MIT
URL:		https://github.com/cjbassi/ytop
Source0:	%{url}/archive/%{version}.tar.gz


BuildRequires:  cargo

%description
%{summary}

%prep
%autosetup

%build
cargo build --release --locked --all-features

%files

%changelog
* Mon Feb 17 2020 Xiaofeng Wang <hernywangxf@me.com> 0.5.1-1
- Initial RPM release
