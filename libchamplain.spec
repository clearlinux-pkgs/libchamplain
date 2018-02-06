#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libchamplain
Version  : 0.12.16
Release  : 1
URL      : https://download.gnome.org/sources/libchamplain/0.12/libchamplain-0.12.16.tar.xz
Source0  : https://download.gnome.org/sources/libchamplain/0.12/libchamplain-0.12.16.tar.xz
Summary  : Gtk+ Widget wrapper for libchamplain
Group    : Development/Tools
License  : LGPL-2.1
Requires: libchamplain-lib
Requires: libchamplain-doc
Requires: libchamplain-data
BuildRequires : docbook-xml
BuildRequires : gobject-introspection-dev
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

%description
=========================
libchamplain is a Clutter based widget to display rich, eye-candy and
interactive maps.

%package data
Summary: data components for the libchamplain package.
Group: Data

%description data
data components for the libchamplain package.


%package dev
Summary: dev components for the libchamplain package.
Group: Development
Requires: libchamplain-lib
Requires: libchamplain-data
Provides: libchamplain-devel

%description dev
dev components for the libchamplain package.


%package doc
Summary: doc components for the libchamplain package.
Group: Documentation

%description doc
doc components for the libchamplain package.


%package lib
Summary: lib components for the libchamplain package.
Group: Libraries
Requires: libchamplain-data

%description lib
lib components for the libchamplain package.


%prep
%setup -q -n libchamplain-0.12.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517954791
%configure --disable-static --disable-memphis
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1517954791
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Champlain-0.12.typelib
/usr/lib64/girepository-1.0/GtkChamplain-0.12.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/champlain-0.12.vapi
/usr/share/vala/vapi/champlain-gtk-0.12.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libchamplain-0.12/champlain/champlain-adjustment.h
/usr/include/libchamplain-0.12/champlain/champlain-bounding-box.h
/usr/include/libchamplain-0.12/champlain/champlain-coordinate.h
/usr/include/libchamplain-0.12/champlain/champlain-custom-marker.h
/usr/include/libchamplain-0.12/champlain/champlain-defines.h
/usr/include/libchamplain-0.12/champlain/champlain-enum-types.h
/usr/include/libchamplain-0.12/champlain/champlain-error-tile-renderer.h
/usr/include/libchamplain-0.12/champlain/champlain-exportable.h
/usr/include/libchamplain-0.12/champlain/champlain-features.h
/usr/include/libchamplain-0.12/champlain/champlain-file-cache.h
/usr/include/libchamplain-0.12/champlain/champlain-file-tile-source.h
/usr/include/libchamplain-0.12/champlain/champlain-image-renderer.h
/usr/include/libchamplain-0.12/champlain/champlain-kinetic-scroll-view.h
/usr/include/libchamplain-0.12/champlain/champlain-label.h
/usr/include/libchamplain-0.12/champlain/champlain-layer.h
/usr/include/libchamplain-0.12/champlain/champlain-license.h
/usr/include/libchamplain-0.12/champlain/champlain-location.h
/usr/include/libchamplain-0.12/champlain/champlain-map-source-chain.h
/usr/include/libchamplain-0.12/champlain/champlain-map-source-desc.h
/usr/include/libchamplain-0.12/champlain/champlain-map-source-factory.h
/usr/include/libchamplain-0.12/champlain/champlain-map-source.h
/usr/include/libchamplain-0.12/champlain/champlain-marker-layer.h
/usr/include/libchamplain-0.12/champlain/champlain-marker.h
/usr/include/libchamplain-0.12/champlain/champlain-marshal.h
/usr/include/libchamplain-0.12/champlain/champlain-memory-cache.h
/usr/include/libchamplain-0.12/champlain/champlain-network-bbox-tile-source.h
/usr/include/libchamplain-0.12/champlain/champlain-network-tile-source.h
/usr/include/libchamplain-0.12/champlain/champlain-null-tile-source.h
/usr/include/libchamplain-0.12/champlain/champlain-path-layer.h
/usr/include/libchamplain-0.12/champlain/champlain-point.h
/usr/include/libchamplain-0.12/champlain/champlain-renderer.h
/usr/include/libchamplain-0.12/champlain/champlain-scale.h
/usr/include/libchamplain-0.12/champlain/champlain-tile-cache.h
/usr/include/libchamplain-0.12/champlain/champlain-tile-source.h
/usr/include/libchamplain-0.12/champlain/champlain-tile.h
/usr/include/libchamplain-0.12/champlain/champlain-version.h
/usr/include/libchamplain-0.12/champlain/champlain-view.h
/usr/include/libchamplain-0.12/champlain/champlain-viewport.h
/usr/include/libchamplain-0.12/champlain/champlain.h
/usr/include/libchamplain-gtk-0.12/champlain-gtk/champlain-gtk-enum-types.h
/usr/include/libchamplain-gtk-0.12/champlain-gtk/champlain-gtk-marshal.h
/usr/include/libchamplain-gtk-0.12/champlain-gtk/champlain-gtk.h
/usr/include/libchamplain-gtk-0.12/champlain-gtk/gtk-champlain-embed.h
/usr/lib64/libchamplain-0.12.so
/usr/lib64/libchamplain-gtk-0.12.so
/usr/lib64/pkgconfig/champlain-0.12.pc
/usr/lib64/pkgconfig/champlain-gtk-0.12.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainBoundingBox.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainCoordinate.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainCustomMarker.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainErrorTileRenderer.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainExportable.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainFileCache.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainFileTileSource.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainImageRenderer.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainLabel.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainLayer.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainLicense.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainLocation.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainMapSource.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainMapSourceChain.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainMapSourceDesc.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainMapSourceFactory.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainMarker.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainMarkerLayer.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainMemoryCache.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainNetworkBboxTileSource.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainNetworkTileSource.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainNullTileSource.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainPathLayer.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainPoint.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainRenderer.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainScale.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainTile.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainTileCache.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainTileSource.html
/usr/share/gtk-doc/html/libchamplain-0.12/ChamplainView.html
/usr/share/gtk-doc/html/libchamplain-0.12/annotation-glossary.html
/usr/share/gtk-doc/html/libchamplain-0.12/ch01.html
/usr/share/gtk-doc/html/libchamplain-0.12/ch02.html
/usr/share/gtk-doc/html/libchamplain-0.12/ch03.html
/usr/share/gtk-doc/html/libchamplain-0.12/ch04.html
/usr/share/gtk-doc/html/libchamplain-0.12/ch05.html
/usr/share/gtk-doc/html/libchamplain-0.12/ch06.html
/usr/share/gtk-doc/html/libchamplain-0.12/home.png
/usr/share/gtk-doc/html/libchamplain-0.12/index.html
/usr/share/gtk-doc/html/libchamplain-0.12/ix01.html
/usr/share/gtk-doc/html/libchamplain-0.12/ix02.html
/usr/share/gtk-doc/html/libchamplain-0.12/ix03.html
/usr/share/gtk-doc/html/libchamplain-0.12/ix04.html
/usr/share/gtk-doc/html/libchamplain-0.12/ix05.html
/usr/share/gtk-doc/html/libchamplain-0.12/ix06.html
/usr/share/gtk-doc/html/libchamplain-0.12/ix07.html
/usr/share/gtk-doc/html/libchamplain-0.12/ix08.html
/usr/share/gtk-doc/html/libchamplain-0.12/ix09.html
/usr/share/gtk-doc/html/libchamplain-0.12/left-insensitive.png
/usr/share/gtk-doc/html/libchamplain-0.12/left.png
/usr/share/gtk-doc/html/libchamplain-0.12/libchamplain-0.12.devhelp2
/usr/share/gtk-doc/html/libchamplain-0.12/libchamplain-ChamplainVersion.html
/usr/share/gtk-doc/html/libchamplain-0.12/pt01.html
/usr/share/gtk-doc/html/libchamplain-0.12/pt02.html
/usr/share/gtk-doc/html/libchamplain-0.12/pt03.html
/usr/share/gtk-doc/html/libchamplain-0.12/pt04.html
/usr/share/gtk-doc/html/libchamplain-0.12/pt05.html
/usr/share/gtk-doc/html/libchamplain-0.12/pt06.html
/usr/share/gtk-doc/html/libchamplain-0.12/pt07.html
/usr/share/gtk-doc/html/libchamplain-0.12/right-insensitive.png
/usr/share/gtk-doc/html/libchamplain-0.12/right.png
/usr/share/gtk-doc/html/libchamplain-0.12/style.css
/usr/share/gtk-doc/html/libchamplain-0.12/up-insensitive.png
/usr/share/gtk-doc/html/libchamplain-0.12/up.png
/usr/share/gtk-doc/html/libchamplain-gtk-0.12/GtkChamplainEmbed.html
/usr/share/gtk-doc/html/libchamplain-gtk-0.12/annotation-glossary.html
/usr/share/gtk-doc/html/libchamplain-gtk-0.12/home.png
/usr/share/gtk-doc/html/libchamplain-gtk-0.12/index.html
/usr/share/gtk-doc/html/libchamplain-gtk-0.12/left-insensitive.png
/usr/share/gtk-doc/html/libchamplain-gtk-0.12/left.png
/usr/share/gtk-doc/html/libchamplain-gtk-0.12/libchamplain-gtk-0.12.devhelp2
/usr/share/gtk-doc/html/libchamplain-gtk-0.12/pt01.html
/usr/share/gtk-doc/html/libchamplain-gtk-0.12/right-insensitive.png
/usr/share/gtk-doc/html/libchamplain-gtk-0.12/right.png
/usr/share/gtk-doc/html/libchamplain-gtk-0.12/style.css
/usr/share/gtk-doc/html/libchamplain-gtk-0.12/up-insensitive.png
/usr/share/gtk-doc/html/libchamplain-gtk-0.12/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libchamplain-0.12.so.0
/usr/lib64/libchamplain-0.12.so.0.10.0
/usr/lib64/libchamplain-gtk-0.12.so.0
/usr/lib64/libchamplain-gtk-0.12.so.0.10.0
