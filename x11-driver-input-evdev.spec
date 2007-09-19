Name: x11-driver-input-evdev
Version: 1.1.5
Release: %mkrel 2
Summary: X.org input driver for Linux generic event devices
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-evdev-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
Patch1: xf86-input-evdev-1.1.2-have-HWheelRelativeAxisButtons-7-6-by-default.patch
Patch2: xf86-input-evdev-1.1.2-skip-HWheelRelativeAxisButtons-even-if-unused.patch
Patch3: 0003-FixDuplicateArrayEntry-KeyPressedBitTests-XkbDefaults.patch

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

%description
Evdev is an Xorg input driver for Linux's generic event devices.
It therefore supports all input devices that the kernel knows about,
including most mice and keyboards.

%prep
%setup -q -n xf86-input-evdev-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .DuplicateEntry-Bits-Kxb

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

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


