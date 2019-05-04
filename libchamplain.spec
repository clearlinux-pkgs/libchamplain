#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libchamplain
Version  : 0.12.19
Release  : 4
URL      : https://download.gnome.org/sources/libchamplain/0.12/libchamplain-0.12.19.tar.xz
Source0  : https://download.gnome.org/sources/libchamplain/0.12/libchamplain-0.12.19.tar.xz
Summary  : A map widget
Group    : Development/Tools
License  : LGPL-2.1
Requires: libchamplain-data = %{version}-%{release}
Requires: libchamplain-lib = %{version}-%{release}
Requires: libchamplain-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(clutter-1.0)
BuildRequires : pkgconfig(clutter-gtk-1.0)
BuildRequires : pkgconfig(gdk-3.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : vala

%description
libchamplain - a map widget
===========================
libchamplain is a Gtk widget displaying zoomable and pannable maps that can be
loaded from various network sources. It supports overlay layers, markers, and
custom elements displayed on top of the maps. The library is written in C but
other language mappings are also available thanks to GObject-Introspection.

%package data
Summary: data components for the libchamplain package.
Group: Data

%description data
data components for the libchamplain package.


%package dev
Summary: dev components for the libchamplain package.
Group: Development
Requires: libchamplain-lib = %{version}-%{release}
Requires: libchamplain-data = %{version}-%{release}
Provides: libchamplain-devel = %{version}-%{release}
Requires: libchamplain = %{version}-%{release}

%description dev
dev components for the libchamplain package.


%package lib
Summary: lib components for the libchamplain package.
Group: Libraries
Requires: libchamplain-data = %{version}-%{release}
Requires: libchamplain-license = %{version}-%{release}

%description lib
lib components for the libchamplain package.


%package license
Summary: license components for the libchamplain package.
Group: Default

%description license
license components for the libchamplain package.


%prep
%setup -q -n libchamplain-0.12.19

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557014049
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libchamplain
cp COPYING %{buildroot}/usr/share/package-licenses/libchamplain/COPYING
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Champlain-0.12.typelib
/usr/lib64/girepository-1.0/GtkChamplain-0.12.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/champlain-0.12.deps
/usr/share/vala/vapi/champlain-0.12.vapi
/usr/share/vala/vapi/champlain-gtk-0.12.deps
/usr/share/vala/vapi/champlain-gtk-0.12.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/champlain-0.12/champlain-gtk/champlain-gtk.h
/usr/include/champlain-0.12/champlain-gtk/gtk-champlain-embed.h
/usr/include/champlain-0.12/champlain/champlain-adjustment.h
/usr/include/champlain-0.12/champlain/champlain-bounding-box.h
/usr/include/champlain-0.12/champlain/champlain-coordinate.h
/usr/include/champlain-0.12/champlain/champlain-custom-marker.h
/usr/include/champlain-0.12/champlain/champlain-defines.h
/usr/include/champlain-0.12/champlain/champlain-enum-types.h
/usr/include/champlain-0.12/champlain/champlain-error-tile-renderer.h
/usr/include/champlain-0.12/champlain/champlain-exportable.h
/usr/include/champlain-0.12/champlain/champlain-features.h
/usr/include/champlain-0.12/champlain/champlain-file-cache.h
/usr/include/champlain-0.12/champlain/champlain-file-tile-source.h
/usr/include/champlain-0.12/champlain/champlain-image-renderer.h
/usr/include/champlain-0.12/champlain/champlain-kinetic-scroll-view.h
/usr/include/champlain-0.12/champlain/champlain-label.h
/usr/include/champlain-0.12/champlain/champlain-layer.h
/usr/include/champlain-0.12/champlain/champlain-license.h
/usr/include/champlain-0.12/champlain/champlain-location.h
/usr/include/champlain-0.12/champlain/champlain-map-source-chain.h
/usr/include/champlain-0.12/champlain/champlain-map-source-desc.h
/usr/include/champlain-0.12/champlain/champlain-map-source-factory.h
/usr/include/champlain-0.12/champlain/champlain-map-source.h
/usr/include/champlain-0.12/champlain/champlain-marker-layer.h
/usr/include/champlain-0.12/champlain/champlain-marker.h
/usr/include/champlain-0.12/champlain/champlain-memory-cache.h
/usr/include/champlain-0.12/champlain/champlain-network-bbox-tile-source.h
/usr/include/champlain-0.12/champlain/champlain-network-tile-source.h
/usr/include/champlain-0.12/champlain/champlain-null-tile-source.h
/usr/include/champlain-0.12/champlain/champlain-path-layer.h
/usr/include/champlain-0.12/champlain/champlain-point.h
/usr/include/champlain-0.12/champlain/champlain-renderer.h
/usr/include/champlain-0.12/champlain/champlain-scale.h
/usr/include/champlain-0.12/champlain/champlain-tile-cache.h
/usr/include/champlain-0.12/champlain/champlain-tile-source.h
/usr/include/champlain-0.12/champlain/champlain-tile.h
/usr/include/champlain-0.12/champlain/champlain-version.h
/usr/include/champlain-0.12/champlain/champlain-view.h
/usr/include/champlain-0.12/champlain/champlain-viewport.h
/usr/include/champlain-0.12/champlain/champlain.h
/usr/lib64/libchamplain-0.12.so
/usr/lib64/libchamplain-gtk-0.12.so
/usr/lib64/pkgconfig/champlain-0.12.pc
/usr/lib64/pkgconfig/champlain-gtk-0.12.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libchamplain-0.12.so.0
/usr/lib64/libchamplain-0.12.so.0.11.9
/usr/lib64/libchamplain-gtk-0.12.so.0
/usr/lib64/libchamplain-gtk-0.12.so.0.11.9

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libchamplain/COPYING
