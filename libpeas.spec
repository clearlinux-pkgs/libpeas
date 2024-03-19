#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v4
# autospec commit: f4bef72
#
Name     : libpeas
Version  : 2.0.2
Release  : 39
URL      : https://download.gnome.org/sources/libpeas/2.0/libpeas-2.0.2.tar.xz
Source0  : https://download.gnome.org/sources/libpeas/2.0/libpeas-2.0.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: libpeas-data = %{version}-%{release}
Requires: libpeas-lib = %{version}-%{release}
Requires: libpeas-license = %{version}-%{release}
Requires: libpeas-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gjs-dev
BuildRequires : pkgconfig(gi-docgen)
BuildRequires : pkgconfig(gjs-1.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Introducing libpeas
libpeas is a gobject-based plugins engine, and is targetted at giving every
application the chance to assume its own extensibility. It is currently used by
several Gnome applications like gedit and Totem.

%package data
Summary: data components for the libpeas package.
Group: Data

%description data
data components for the libpeas package.


%package dev
Summary: dev components for the libpeas package.
Group: Development
Requires: libpeas-lib = %{version}-%{release}
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
%setup -q -n libpeas-2.0.2
cd %{_builddir}/libpeas-2.0.2
pushd ..
cp -a libpeas-2.0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710884364
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dgtk_doc=false \
-Dlua51=false  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dgtk_doc=false \
-Dlua51=false  builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/libpeas
cp %{_builddir}/libpeas-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libpeas/3704f4680301a60004b20f94e0b5b8c7ff1484a9 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang libpeas-2
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Peas-2.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/libpeas-2/libpeas.h
/usr/include/libpeas-2/peas-engine.h
/usr/include/libpeas-2/peas-extension-base.h
/usr/include/libpeas-2/peas-extension-set.h
/usr/include/libpeas-2/peas-object-module.h
/usr/include/libpeas-2/peas-plugin-info.h
/usr/include/libpeas-2/peas-version-macros.h
/usr/include/libpeas-2/peas-version.h
/usr/lib64/libpeas-2.so
/usr/lib64/pkgconfig/libpeas-2.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libpeas-2.so.0.0.2
/V3/usr/lib64/libpeas-2/loaders/libgjsloader.so
/V3/usr/lib64/libpeas-2/loaders/libpythonloader.so
/usr/lib64/libpeas-2.so.0
/usr/lib64/libpeas-2.so.0.0.2
/usr/lib64/libpeas-2/loaders/libgjsloader.so
/usr/lib64/libpeas-2/loaders/libpythonloader.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libpeas/3704f4680301a60004b20f94e0b5b8c7ff1484a9

%files locales -f libpeas-2.lang
%defattr(-,root,root,-)

