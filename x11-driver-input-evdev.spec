Name: x11-driver-input-evdev
Version: 1.2.0
Release: %mkrel 2
Summary: X.org input driver for Linux generic event devices
Group: System/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-evdev xorg/drivers/xf86-input-evdev
# cd xorg/drivers/xf86-input/evdev
# git-archive --format=tar --prefix=xf86-input-evdev-1.2.0/ xf86-input-evdev-1.2.0 | bzip2 -9 > xf86-input-evdev-1.2.0.tar.bz2
########################################################################
Source0: xf86-input-evdev-%{version}.tar.bz2
########################################################################
# git-format-patch xf86-input-evdev-1.2.0..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
Patch2: 0002-Ensure-buttons-6-and-7-are-HWheel.patch
########################################################################
License: MIT
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.1.5-4mdk
Conflicts: x11-server < 1.4

%description
Evdev is an Xorg input driver for Linux's generic event devices.
It therefore supports all input devices that the kernel knows about,
including most mice and keyboards.

%prep
%setup -q -n xf86-input-evdev-%{version}

%patch1 -p1
%patch2 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/input/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/evdev_drv.so
%{_mandir}/man4/evdev.*
