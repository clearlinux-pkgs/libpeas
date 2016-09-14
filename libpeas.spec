#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libpeas
Version  : 1.18.0
Release  : 1
URL      : https://download.gnome.org/core/3.20/3.20.2/sources/libpeas-1.18.0.tar.xz
Source0  : https://download.gnome.org/core/3.20/3.20.2/sources/libpeas-1.18.0.tar.xz
Summary  : libpeas-gtk, a GObject plugins library (Gtk widgets)
Group    : Development/Tools
License  : LGPL-2.1
Requires: libpeas-bin
Requires: libpeas-lib
Requires: libpeas-data
Requires: libpeas-doc
Requires: libpeas-locales
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : valgrind

%description
Introducing libpeas
===================
libpeas is a gobject-based plugins engine, and is targetted at giving every
application the chance to assume its own extensibility. It is currently used by
several Gnome applications like gedit and Totem.

%package bin
Summary: bin components for the libpeas package.
Group: Binaries
Requires: libpeas-data

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
Requires: libpeas-lib
Requires: libpeas-bin
Requires: libpeas-data
Provides: libpeas-devel

%description dev
dev components for the libpeas package.


%package doc
Summary: doc components for the libpeas package.
Group: Documentation

%description doc
doc components for the libpeas package.


%package lib
Summary: lib components for the libpeas package.
Group: Libraries
Requires: libpeas-data

%description lib
lib components for the libpeas package.


%package locales
Summary: locales components for the libpeas package.
Group: Default

%description locales
locales components for the libpeas package.


%prep
%setup -q -n libpeas-1.18.0

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang libpeas

%files
%defattr(-,root,root,-)
/usr/lib64/peas-demo/plugins/helloworld/helloworld.plugin
/usr/lib64/peas-demo/plugins/secondtime/secondtime.plugin

%files bin
%defattr(-,root,root,-)
/usr/bin/peas-demo

%files data
%defattr(-,root,root,-)
/usr/share/gir-1.0/Peas-1.0.gir
/usr/share/gir-1.0/PeasGtk-1.0.gir
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
/usr/include/libpeas-1.0/libpeas/peas.h
/usr/lib64/*.so
/usr/lib64/girepository-1.0/Peas-1.0.typelib
/usr/lib64/girepository-1.0/PeasGtk-1.0.typelib
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/libpeas/PeasActivatable.html
/usr/share/gtk-doc/html/libpeas/PeasEngine.html
/usr/share/gtk-doc/html/libpeas/PeasExtensionBase.html
/usr/share/gtk-doc/html/libpeas/PeasExtensionSet.html
/usr/share/gtk-doc/html/libpeas/PeasGtkConfigurable.html
/usr/share/gtk-doc/html/libpeas/PeasGtkPluginManager.html
/usr/share/gtk-doc/html/libpeas/PeasGtkPluginManagerView.html
/usr/share/gtk-doc/html/libpeas/PeasObjectModule.html
/usr/share/gtk-doc/html/libpeas/PeasPluginInfo.html
/usr/share/gtk-doc/html/libpeas/annotation-glossary.html
/usr/share/gtk-doc/html/libpeas/api-index-1-14.html
/usr/share/gtk-doc/html/libpeas/api-index-1-18.html
/usr/share/gtk-doc/html/libpeas/api-index-1-2.html
/usr/share/gtk-doc/html/libpeas/api-index-1-4.html
/usr/share/gtk-doc/html/libpeas/api-index-1-6.html
/usr/share/gtk-doc/html/libpeas/api-index-deprecated.html
/usr/share/gtk-doc/html/libpeas/api-index-full.html
/usr/share/gtk-doc/html/libpeas/ch01.html
/usr/share/gtk-doc/html/libpeas/ch02.html
/usr/share/gtk-doc/html/libpeas/ch03.html
/usr/share/gtk-doc/html/libpeas/home.png
/usr/share/gtk-doc/html/libpeas/index.html
/usr/share/gtk-doc/html/libpeas/left-insensitive.png
/usr/share/gtk-doc/html/libpeas/left.png
/usr/share/gtk-doc/html/libpeas/libpeas-PeasExtension.html
/usr/share/gtk-doc/html/libpeas/libpeas.devhelp2
/usr/share/gtk-doc/html/libpeas/peas-gtk-plugin-manager.png
/usr/share/gtk-doc/html/libpeas/pt01.html
/usr/share/gtk-doc/html/libpeas/right-insensitive.png
/usr/share/gtk-doc/html/libpeas/right.png
/usr/share/gtk-doc/html/libpeas/style.css
/usr/share/gtk-doc/html/libpeas/up-insensitive.png
/usr/share/gtk-doc/html/libpeas/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/peas-demo/plugins/helloworld/libhelloworld.so
/usr/lib64/peas-demo/plugins/secondtime/libsecondtime.so

%files locales -f libpeas.lang 
%defattr(-,root,root,-)

