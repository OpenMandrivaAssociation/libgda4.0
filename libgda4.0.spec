%define api 4.0
%define pkgname libgda
%define name %{pkgname}%{api}

%define build_mysql 1
%{?_with_mysql: %global build_mysql 1}
%define build_freetds 0
%{?_with_freetds: %global build_freetds 1}
%define build_mdb 0
%{?_with_mdb: %global build_mdb 1}

#gw check fails in the BS in 4.1.3
%define enable_test 1
%{?_with_mdb: %global enable_test 1}


%define dirver %api
%define oname gda
%define	major 4

%define libname %mklibname %{oname}%{api}_ %major 
%define develname %mklibname -d %{oname}%{api}

Summary:	GNU Data Access
Name: 		%{name}
Version:	4.2.12
Release:	1
License: 	GPLv2+ and LGPLv2+
Group: 		Databases
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.xz
Patch0: libgda-4.2.10-fix-linking.patch

BuildRequires:	bison
BuildRequires:	db-devel
BuildRequires:	flex
BuildRequires:	gdbm-devel
BuildRequires:  gtk+2-devel
BuildRequires:  unique-devel
%if %enable_test
#gw only for make check:
BuildRequires:  libjson-glib-devel
BuildRequires: check-devel
#BuildRequires:  %name
%endif
BuildRequires:	libxslt-devel >= 1.0.9
BuildRequires:	ncurses-devel
BuildRequires:  openldap2-devel
BuildRequires:	intltool
BuildRequires:	popt-devel
BuildRequires:	postgresql-devel
BuildRequires:  gnome-vfs2-devel
BuildRequires:	readline-devel
#BuildRequires:	scrollkeeper
BuildRequires:  sqlite3-devel
BuildRequires:  unixODBC-devel
BuildRequires:	xbase-devel
BuildRequires:  libsoup-devel
BuildRequires:  iso-codes
BuildRequires:  gobject-introspection-devel
%ifnarch %arm %mips
BuildRequires: java-1.6.0-devel
%endif
BuildRequires: automake1.8
%if %build_mysql
BuildRequires:	mysql-devel
%endif
%if %build_freetds
BuildRequires:	freetds-devel
%endif
BuildRequires:	gtk-doc
BuildRequires:	gnome-doc-utils
#Requires(post):		scrollkeeper
#Requires(postun):	scrollkeeper
URL: 		http://www.gnome-db.org/
Requires: iso-codes

%description
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

Drivers for the supported databases are included in the libgda4.0-* packages.

%package -n	%{libname}
Summary:	GNU Data Access Development
Group: 		System/Libraries

%description -n	%{libname}
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

%package -n	%{develname}
Summary:	GNU Data Access Development
Group: 		Development/Databases
Requires:	%{libname} = %{version}
Provides:	gda4.0-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
%define _requires_exceptions ^devel.libgda-

%description -n	%{develname}
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

%package	postgres
Summary:	GDA PostgreSQL Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	postgres
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

This package includes the GDA PostgreSQL provider

%package	mysql
Summary:	GDA MySQL Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	mysql
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

This package includes the GDA MySQL provider

%package	bdb
Summary:	GDA Berkeley Database Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	bdb
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

This package includes the GDA Berkeley Database provider.

%if %build_freetds
%package	freetds
Summary:	GDA FreeTDS Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	freetds
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

This package includes the GDA FreeTDS provider.
%endif

%if %build_mdb
BuildRequires:	libmdbtools-devel
%package	mdb
Summary:	GDA MDB Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	mdb
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

This package includes the GDA MDB provider, which can access
Microsoft Access databases.
%endif

%package	sqlite
Summary:	GDA sqlite Provider
Group:		Databases
Requires:	%{name} = %{version}
Obsoletes:      gda3.0-sqlite

%description	sqlite
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

This package includes the GDA sqlite provider

%ifnarch %arm %mips
%package        jdbc
Summary:	GDA Java Database Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	jdbc
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

This package includes the GDA Java Database provider.
%endif

%package	ldap
Summary:	GDA LDAP Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	ldap
GNU Data Access is an attempt to provide uniform access to
different kinds of data sources (databases, information
servers, mail spools, etc).
It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project
(http://www.gnome-db.org/), but has been
separated from it to allow non-GNOME applications to be
developed based on it.

This package includes the GDA LDAP provider

%prep
%setup -q -n %{pkgname}-%{version}
%apply_patches

%build
#gw patch0:
autoreconf -fi
%configure2_5x \
	--disable-static \
%if %build_mysql
	--with-mysql=yes \
%endif
%if !%build_freetds
	--with-tds=no \
%endif
%if !%build_mdb
	--with-mdb=no \
%endif
	--without-firebird --with-bdb=%_prefix --with-bdb-libdir-name=%_lib

make

%install
rm -rf %{buildroot}

%{makeinstall_std}

# remove unneeded files
rm -f %{buildroot}%{_libdir}/libgda-%dirver/*/*.{a,la}

%{find_lang} %{pkgname}-%{api} --with-gnome

%if %enable_test
%check
make check
%endif

%files -f %{pkgname}-%{api}.lang
%doc AUTHORS COPYING README
%{_bindir}/*
%_mandir/man1/*
%dir %{_sysconfdir}/libgda-%dirver
%config(noreplace) %_sysconfdir/libgda-%dirver/sales_test.db
%config(noreplace) %{_sysconfdir}/libgda-%dirver/config
%{_datadir}/applications/gda-browser-%api.desktop
%{_datadir}/applications/gda-control-center-%api.desktop
%{_datadir}/pixmaps/gda*
%{_datadir}/icons/hicolor/*/apps/gda-control-center.*
%{_datadir}/libgda-%dirver
%dir %{_libdir}/libgda-%dirver
%dir %{_libdir}/libgda-%dirver/plugins
%dir %{_libdir}/libgda-%dirver/providers
%{_libdir}/libgda-%dirver/plugins/*.xml
%{_libdir}/libgda-%dirver/plugins/libgda-ui-plugins.so
%{_libdir}/libgda-%dirver/providers/libgda-web.so
%{_libdir}/libgda-%dirver/providers/libgda-sqlcipher.so

%files -n %{libname}
%{_libdir}/libgda-%{api}.so.%{major}*
%{_libdir}/libgda-report-%{api}.so.%{major}*
%{_libdir}/libgda-ui-%{api}.so.%{major}*
%{_libdir}/libgda-xslt-%{api}.so.%{major}*
%{_libdir}/girepository-1.0/Gda-%{api}.typelib
%{_libdir}/girepository-1.0/Gdaui-%{api}.typelib

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/libgda-%dirver/
%doc %{_datadir}/gtk-doc/html/gda-browser
%{_libdir}/libgda-%{api}.so
%{_libdir}/libgda-report-%{api}.so
%{_libdir}/libgda-ui-%{api}.so
%{_libdir}/libgda-xslt-%{api}.so
%attr(644,root,root) %{_libdir}/lib*.la
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gir-1.0/Gda-%api.gir
%{_datadir}/gir-1.0/Gdaui-%api.gir
%{_datadir}/gnome/help/gda-browser

%files sqlite
%{_libdir}/libgda-%dirver/providers/libgda-sqlite.so

%files postgres
%{_libdir}/libgda-%dirver/providers/libgda-postgres.so

%files bdb
%{_libdir}/libgda-%dirver/providers/libgda-bdb.so

%if %build_mysql
%files mysql
%{_libdir}/libgda-%dirver/providers/libgda-mysql.so
%endif

%if %build_freetds
%files freetds
%{_libdir}/libgda-%dirver/providers/libgda-freetds.so
%endif

%if %build_mdb
%files mdb
%{_libdir}/libgda-%dirver/providers/libgda-mdb.so
%endif

%ifnarch %arm %mips
%files jdbc
%{_libdir}/libgda-%dirver/providers/libgda-jdbc.so
%{_libdir}/libgda-%dirver/providers/gdaprovider-4.0.jar
%endif

%files ldap
%{_libdir}/libgda-%dirver/providers/libgda-ldap.so

