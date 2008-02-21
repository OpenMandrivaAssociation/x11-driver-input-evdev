Name: x11-driver-input-evdev
Version: 1.2.0
Release: %mkrel 5
Summary: X.org input driver for Linux generic event devices
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-evdev-%{version}.tar.bz2

Patch1: 0001-Don-t-flush-buttons-on-init-bug-12630.patch
Patch2: 0002-Initialise-b_map_data-to-correct-size.-Bug-13991.patch

# ensure:
# - button 6 is "Wheel Left"
# - button 7 is "Wheel Right"
# - button 8 is BTN_SIDE
# - button 9 is BTN_EXTRA
# by skipping buttons 6&7 if the mouse doesn't have a hwheel
Patch3: 0003-Ensure-buttons-6-and-7-are-HWheel.patch

Patch4: 0004-More-accurate-error-messages-on-device-open-fail.patch

License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: x11-server < 1.4

%description
Evdev is an Xorg input driver for Linux's generic event devices.
It therefore supports all input devices that the kernel knows about,
including most mice and keyboards.

%prep
%setup -q -n xf86-input-evdev-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/evdev_drv.la
%{_libdir}/xorg/modules/input/evdev_drv.so
%{_mandir}/man4/evdev.*
