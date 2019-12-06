#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libpeas
Version  : 1.24.1
Release  : 16
URL      : https://download.gnome.org/sources/libpeas/1.24/libpeas-1.24.1.tar.xz
Source0  : https://download.gnome.org/sources/libpeas/1.24/libpeas-1.24.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: libpeas-bin = %{version}-%{release}
Requires: libpeas-data = %{version}-%{release}
Requires: libpeas-lib = %{version}-%{release}
Requires: libpeas-license = %{version}-%{release}
Requires: libpeas-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gtk-doc-dev
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gtk-doc)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : pkgconfig(python3)

%description
Introducing libpeas
===================
libpeas is a gobject-based plugins engine, and is targetted at giving every
application the chance to assume its own extensibility. It is currently used by
several Gnome applications like gedit and Totem.

%package bin
Summary: bin components for the libpeas package.
Group: Binaries
Requires: libpeas-data = %{version}-%{release}
Requires: libpeas-license = %{version}-%{release}

%description bin
bin components for the libpeas package.


%package data
Summary: data components for the libpeas package.
Group: Data

%description data
data components for the libpeas package.


%package dev
Summary: dev components for the libpeas package.
Group: Development
Requires: libpeas-lib = %{version}-%{release}
Requires: libpeas-bin = %{version}-%{release}
Requires: libpeas-data = %{version}-%{release}
Provides: libpeas-devel = %{version}-%{release}
Requires: libpeas = %{version}-%{release}

%description dev
dev components for the libpeas package.


%package lib
Summary: lib components for the libpeas package.
Group: Libraries
Requires: libpeas-data = %{version}-%{release}
Requires: libpeas-license = %{version}-%{release}

%description lib
lib components for the libpeas package.


%package license
Summary: license components for the libpeas package.
Group: Default

%description license
license components for the libpeas package.


%package locales
Summary: locales components for the libpeas package.
Group: Default

%description locales
locales components for the libpeas package.


%prep
%setup -q -n libpeas-1.24.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572448961
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libpeas
cp %{_builddir}/libpeas-1.24.1/COPYING %{buildroot}/usr/share/package-licenses/libpeas/3704f4680301a60004b20f94e0b5b8c7ff1484a9
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang libpeas-1.0

%files
%defattr(-,root,root,-)
/usr/lib64/peas-demo/plugins/helloworld/helloworld.plugin
/usr/lib64/peas-demo/plugins/pythonhello/pythonhello.plugin
/usr/lib64/peas-demo/plugins/pythonhello/pythonhello.py
/usr/lib64/peas-demo/plugins/secondtime/secondtime.plugin

%files bin
%defattr(-,root,root,-)
/usr/bin/peas-demo

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Peas-1.0.typelib
/usr/lib64/girepository-1.0/PeasGtk-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/icons/hicolor/16x16/actions/libpeas-plugin.png
/usr/share/icons/hicolor/22x22/actions/libpeas-plugin.png
/usr/share/icons/hicolor/32x32/actions/libpeas-plugin.png
/usr/share/icons/hicolor/scalable/actions/libpeas-plugin.svg

%files dev
%defattr(-,root,root,-)
/usr/include/libpeas-1.0/libpeas-gtk/peas-gtk-autocleanups.h
/usr/include/libpeas-1.0/libpeas-gtk/peas-gtk-configurable.h
/usr/include/libpeas-1.0/libpeas-gtk/peas-gtk-plugin-manager-view.h
/usr/include/libpeas-1.0/libpeas-gtk/peas-gtk-plugin-manager.h
/usr/include/libpeas-1.0/libpeas-gtk/peas-gtk.h
/usr/include/libpeas-1.0/libpeas/peas-activatable.h
/usr/include/libpeas-1.0/libpeas/peas-autocleanups.h
/usr/include/libpeas-1.0/libpeas/peas-engine.h
/usr/include/libpeas-1.0/libpeas/peas-extension-base.h
/usr/include/libpeas-1.0/libpeas/peas-extension-set.h
/usr/include/libpeas-1.0/libpeas/peas-extension.h
/usr/include/libpeas-1.0/libpeas/peas-object-module.h
/usr/include/libpeas-1.0/libpeas/peas-plugin-info.h
/usr/include/libpeas-1.0/libpeas/peas-version-macros.h
/usr/include/libpeas-1.0/libpeas/peas-version.h
/usr/include/libpeas-1.0/libpeas/peas.h
/usr/lib64/libpeas-1.0.so
/usr/lib64/libpeas-gtk-1.0.so
/usr/lib64/pkgconfig/libpeas-1.0.pc
/usr/lib64/pkgconfig/libpeas-gtk-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpeas-1.0.so.0
/usr/lib64/libpeas-1.0.so.0.2400.1
/usr/lib64/libpeas-1.0/loaders/libpython3loader.so
/usr/lib64/libpeas-gtk-1.0.so.0
/usr/lib64/libpeas-gtk-1.0.so.0.2400.1
/usr/lib64/peas-demo/plugins/helloworld/libhelloworld.so
/usr/lib64/peas-demo/plugins/secondtime/libsecondtime.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libpeas/3704f4680301a60004b20f94e0b5b8c7ff1484a9

%files locales -f libpeas-1.0.lang
%defattr(-,root,root,-)

