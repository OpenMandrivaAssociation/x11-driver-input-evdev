Name:		x11-driver-input-evdev
Version:	2.7.3
Release:	1
Summary:	X.org input driver for Linux generic event devices
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	ftp://ftp.x.org/pub/individual/driver/xf86-input-evdev-%{version}.tar.bz2
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.12
BuildRequires:	x11-util-macros >= 1.0.1
%if %mdvver >= 201200
BuildRequires: pkgconfig(udev) >= 186
%else
BuildRequires: pkgconfig(udev)
%endif
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)
Conflicts:	x11-server < 1.4
Obsoletes:	imwheel

%description
Evdev is an Xorg input driver for Linux's generic event devices.
It therefore supports all input devices that the kernel knows about,
including most mice and keyboards.

%package devel
Summary:	Development files for %{name}
Group:		Development/X11

%description devel
Development files for %{name}.

%prep
%setup -qn xf86-input-evdev-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/input/evdev_drv.so
%{_mandir}/man4/evdev.*

%files devel
%{_includedir}/xorg/evdev-properties.h
%{_libdir}/pkgconfig/xorg-evdev.pc
