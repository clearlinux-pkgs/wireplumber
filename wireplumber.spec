#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wireplumber
Version  : 0.4.11
Release  : 2
URL      : https://gitlab.freedesktop.org/pipewire/wireplumber/-/archive/0.4.11/wireplumber-0.4.11.tar.gz
Source0  : https://gitlab.freedesktop.org/pipewire/wireplumber/-/archive/0.4.11/wireplumber-0.4.11.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: wireplumber-bin = %{version}-%{release}
Requires: wireplumber-data = %{version}-%{release}
Requires: wireplumber-lib = %{version}-%{release}
Requires: wireplumber-license = %{version}-%{release}
Requires: wireplumber-locales = %{version}-%{release}
Requires: wireplumber-services = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : doxygen
BuildRequires : glib-dev
BuildRequires : gobject-introspection
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libspa-0.2)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(lua)
BuildRequires : pkgconfig(systemd)
BuildRequires : pypi-sphinx
BuildRequires : valgrind
Patch1: 0001-Fix-lua-version-search.patch

%description
WirePlumber
===========
.. image:: https://gitlab.freedesktop.org/pipewire/wireplumber/badges/master/pipeline.svg
:alt: Pipeline status

%package bin
Summary: bin components for the wireplumber package.
Group: Binaries
Requires: wireplumber-data = %{version}-%{release}
Requires: wireplumber-license = %{version}-%{release}
Requires: wireplumber-services = %{version}-%{release}

%description bin
bin components for the wireplumber package.


%package data
Summary: data components for the wireplumber package.
Group: Data

%description data
data components for the wireplumber package.


%package dev
Summary: dev components for the wireplumber package.
Group: Development
Requires: wireplumber-lib = %{version}-%{release}
Requires: wireplumber-bin = %{version}-%{release}
Requires: wireplumber-data = %{version}-%{release}
Provides: wireplumber-devel = %{version}-%{release}
Requires: wireplumber = %{version}-%{release}

%description dev
dev components for the wireplumber package.


%package lib
Summary: lib components for the wireplumber package.
Group: Libraries
Requires: wireplumber-data = %{version}-%{release}
Requires: wireplumber-license = %{version}-%{release}

%description lib
lib components for the wireplumber package.


%package license
Summary: license components for the wireplumber package.
Group: Default

%description license
license components for the wireplumber package.


%package locales
Summary: locales components for the wireplumber package.
Group: Default

%description locales
locales components for the wireplumber package.


%package services
Summary: services components for the wireplumber package.
Group: Systemd services

%description services
services components for the wireplumber package.


%prep
%setup -q -n wireplumber-0.4.11
cd %{_builddir}/wireplumber-0.4.11
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657035403
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dsystem-lua=true \
-Delogind=disabled  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/wireplumber
cp %{_builddir}/wireplumber-0.4.11/LICENSE %{buildroot}/usr/share/package-licenses/wireplumber/eba84e7971aadceae1afd0226007498a4c1ed96b
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang wireplumber

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wireplumber
/usr/bin/wpctl
/usr/bin/wpexec

%files data
%defattr(-,root,root,-)
/usr/share/wireplumber/bluetooth.conf
/usr/share/wireplumber/bluetooth.lua.d/00-functions.lua
/usr/share/wireplumber/bluetooth.lua.d/30-bluez-monitor.lua
/usr/share/wireplumber/bluetooth.lua.d/50-bluez-config.lua
/usr/share/wireplumber/bluetooth.lua.d/90-enable-all.lua
/usr/share/wireplumber/common/00-functions.lua
/usr/share/wireplumber/main.conf
/usr/share/wireplumber/main.lua.d/00-functions.lua
/usr/share/wireplumber/main.lua.d/20-default-access.lua
/usr/share/wireplumber/main.lua.d/30-alsa-monitor.lua
/usr/share/wireplumber/main.lua.d/30-libcamera-monitor.lua
/usr/share/wireplumber/main.lua.d/30-v4l2-monitor.lua
/usr/share/wireplumber/main.lua.d/40-device-defaults.lua
/usr/share/wireplumber/main.lua.d/40-stream-defaults.lua
/usr/share/wireplumber/main.lua.d/50-alsa-config.lua
/usr/share/wireplumber/main.lua.d/50-default-access-config.lua
/usr/share/wireplumber/main.lua.d/50-libcamera-config.lua
/usr/share/wireplumber/main.lua.d/50-v4l2-config.lua
/usr/share/wireplumber/main.lua.d/90-enable-all.lua
/usr/share/wireplumber/policy.conf
/usr/share/wireplumber/policy.lua.d/00-functions.lua
/usr/share/wireplumber/policy.lua.d/10-default-policy.lua
/usr/share/wireplumber/policy.lua.d/50-endpoints-config.lua
/usr/share/wireplumber/policy.lua.d/90-enable-all.lua
/usr/share/wireplumber/scripts/access/access-default.lua
/usr/share/wireplumber/scripts/access/access-portal.lua
/usr/share/wireplumber/scripts/create-item.lua
/usr/share/wireplumber/scripts/fallback-sink.lua
/usr/share/wireplumber/scripts/intended-roles.lua
/usr/share/wireplumber/scripts/monitors/alsa-midi.lua
/usr/share/wireplumber/scripts/monitors/alsa.lua
/usr/share/wireplumber/scripts/monitors/bluez.lua
/usr/share/wireplumber/scripts/monitors/libcamera.lua
/usr/share/wireplumber/scripts/monitors/v4l2.lua
/usr/share/wireplumber/scripts/policy-bluetooth.lua
/usr/share/wireplumber/scripts/policy-device-profile.lua
/usr/share/wireplumber/scripts/policy-device-routes.lua
/usr/share/wireplumber/scripts/policy-endpoint-client-links.lua
/usr/share/wireplumber/scripts/policy-endpoint-client.lua
/usr/share/wireplumber/scripts/policy-endpoint-device.lua
/usr/share/wireplumber/scripts/policy-node.lua
/usr/share/wireplumber/scripts/restore-stream.lua
/usr/share/wireplumber/scripts/static-endpoints.lua
/usr/share/wireplumber/scripts/suspend-node.lua
/usr/share/wireplumber/wireplumber.conf

%files dev
%defattr(-,root,root,-)
/usr/include/wireplumber-0.4/wp/client.h
/usr/include/wireplumber-0.4/wp/component-loader.h
/usr/include/wireplumber-0.4/wp/core.h
/usr/include/wireplumber-0.4/wp/dbus.h
/usr/include/wireplumber-0.4/wp/defs.h
/usr/include/wireplumber-0.4/wp/device.h
/usr/include/wireplumber-0.4/wp/endpoint.h
/usr/include/wireplumber-0.4/wp/error.h
/usr/include/wireplumber-0.4/wp/factory.h
/usr/include/wireplumber-0.4/wp/global-proxy.h
/usr/include/wireplumber-0.4/wp/iterator.h
/usr/include/wireplumber-0.4/wp/link.h
/usr/include/wireplumber-0.4/wp/log.h
/usr/include/wireplumber-0.4/wp/metadata.h
/usr/include/wireplumber-0.4/wp/module.h
/usr/include/wireplumber-0.4/wp/node.h
/usr/include/wireplumber-0.4/wp/object-interest.h
/usr/include/wireplumber-0.4/wp/object-manager.h
/usr/include/wireplumber-0.4/wp/object.h
/usr/include/wireplumber-0.4/wp/plugin.h
/usr/include/wireplumber-0.4/wp/port.h
/usr/include/wireplumber-0.4/wp/properties.h
/usr/include/wireplumber-0.4/wp/proxy-interfaces.h
/usr/include/wireplumber-0.4/wp/proxy.h
/usr/include/wireplumber-0.4/wp/session-item.h
/usr/include/wireplumber-0.4/wp/si-factory.h
/usr/include/wireplumber-0.4/wp/si-interfaces.h
/usr/include/wireplumber-0.4/wp/spa-json.h
/usr/include/wireplumber-0.4/wp/spa-pod.h
/usr/include/wireplumber-0.4/wp/spa-type.h
/usr/include/wireplumber-0.4/wp/state.h
/usr/include/wireplumber-0.4/wp/transition.h
/usr/include/wireplumber-0.4/wp/wp.h
/usr/include/wireplumber-0.4/wp/wpenums.h
/usr/include/wireplumber-0.4/wp/wpversion.h
/usr/lib64/libwireplumber-0.4.so
/usr/lib64/pkgconfig/wireplumber-0.4.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwireplumber-0.4.so.0
/usr/lib64/libwireplumber-0.4.so.0.4.11
/usr/lib64/wireplumber-0.4/libwireplumber-module-default-nodes-api.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-default-nodes.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-default-profile.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-file-monitor-api.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-logind.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-lua-scripting.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-metadata.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-mixer-api.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-portal-permissionstore.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-reserve-device.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-si-audio-adapter.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-si-audio-endpoint.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-si-node.so
/usr/lib64/wireplumber-0.4/libwireplumber-module-si-standard-link.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wireplumber/eba84e7971aadceae1afd0226007498a4c1ed96b

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/wireplumber.service
/usr/lib/systemd/user/wireplumber@.service

%files locales -f wireplumber.lang
%defattr(-,root,root,-)

