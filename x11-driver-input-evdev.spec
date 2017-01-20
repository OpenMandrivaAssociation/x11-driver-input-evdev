Name:		x11-driver-input-evdev
Version:	2.10.5
Release:	1
Summary:	X.org input driver for Linux generic event devices
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	ftp://ftp.x.org/pub/individual/driver/xf86-input-evdev-%{version}.tar.bz2
Source1:	11-evdev-trackpoint.conf
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.18
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(dri)
BuildRequires:	pkgconfig(udev) >= 186
BuildRequires:	pkgconfig(libevdev)
BuildRequires:	pkgconfig(mtdev)
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)
Conflicts:	x11-server < 1.4
Obsoletes:	imwheel
%rename		evdev
%rename		x11-driver-input-keyboard

%description
Evdev is an Xorg input driver for Linux's generic event devices.
It therefore supports all input devices that the kernel knows about,
including most mice and keyboards.

%package	devel
Summary:	Development files for %{name}
Group:		Development/X11

%description	devel
Development files for %{name}.

%prep
%setup -qn xf86-input-evdev-%{version}

%build
%define _disable_ld_no_undefined 1

%configure
%make

%install
%makeinstall_std

# Add scrolling support for TrackPoint and similar devices
install -m644 %{SOURCE1} -D %{buildroot}%{_datadir}/X11/xorg.conf.d/11-evdev-trackpoint.conf

%files
%{_libdir}/xorg/modules/input/evdev_drv.so
%{_mandir}/man4/evdev.*
%{_datadir}/X11/xorg.conf.d/*.conf

%files devel
%{_includedir}/xorg/evdev-properties.h
%{_libdir}/pkgconfig/xorg-evdev.pc
