%define build_mysql 1
%{?_with_mysql: %global build_mysql 1}
%define build_freetds 0
%{?_with_freetds: %global build_freetds 1}
%define build_mdb 0
%{?_with_mdb: %global build_mdb 1}

#gw check fails in the BS in 4.1.3
%define enable_test 1
%{?_with_mdb: %global enable_test 1}


%define api		4.0
%define	major 		4
%define pkgname 	libgda
%define oname 		gda

%define libname		%mklibname %{oname} %{api} %major 
%define develname	%mklibname -d %{oname} %{api}

Summary:	GNU Data Access
Name: 		%{pkgname}%{api}
Version:	4.2.13
Release:	1
License: 	GPLv2+ and LGPLv2+
Group: 		Databases
URL: 		http://www.gnome-db.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.xz
Patch0:		libgda-4.2.12-fix-linking.patch

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	iso-codes
BuildRequires:	db-devel
BuildRequires:	gdbm-devel
BuildRequires:	ncurses-devel
BuildRequires:	openldap2-devel
BuildRequires:	postgresql-devel
BuildRequires:	readline-devel
BuildRequires:	unixODBC-devel
BuildRequires:	xbase-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(unique-1.0)
%ifnarch %arm %mips
BuildRequires:	java-1.6.0-devel
%endif
%if %{build_mysql}
BuildRequires:	mysql-devel
%endif
%if %{build_freetds}
BuildRequires:	freetds-devel
%endif
%if %{enable_test}
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(check)
%endif

Requires:	iso-codes

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
This package contains the shared library for %{name}.

%package -n	%{develname}
Summary:	GNU Data Access Development
Group: 		Development/Databases
Requires:	%{libname} = %{version}
Provides:	gda4.0-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the development files for %{name}.

%package	postgres
Summary:	GDA PostgreSQL Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	postgres
This package includes the GDA PostgreSQL provider

%package	mysql
Summary:	GDA MySQL Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	mysql
This package includes the GDA MySQL provider

%package	bdb
Summary:	GDA Berkeley Database Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	bdb
This package includes the GDA Berkeley Database provider.

%if %{build_freetds}
%package	freetds
Summary:	GDA FreeTDS Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	freetds
This package includes the GDA FreeTDS provider.
%endif

%if %{build_mdb}
BuildRequires:	libmdbtools-devel
%package	mdb
Summary:	GDA MDB Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	mdb
This package includes the GDA MDB provider, which can access
Microsoft Access databases.
%endif

%package	sqlite
Summary:	GDA sqlite Provider
Group:		Databases
Requires:	%{name} = %{version}
Obsoletes:      gda3.0-sqlite

%description	sqlite
This package includes the GDA sqlite provider

%ifnarch %arm %mips
%package        jdbc
Summary:	GDA Java Database Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	jdbc
This package includes the GDA Java Database provider.
%endif

%package	ldap
Summary:	GDA LDAP Provider
Group:		Databases
Requires:	%{name} = %{version}

%description	ldap
This package includes the GDA LDAP provider

%prep
%setup -qn %{pkgname}-%{version}
%apply_patches

%build
#gw patch0:
autoreconf -fi
%configure2_5x \
	--disable-static \
%if %build_mysql
	--with-mysql=yes \
%endif
%if !%{build_freetds}
	--with-tds=no \
%endif
%if !%{build_mdb}
	--with-mdb=no \
%endif
	--without-firebird \
	--with-bdb=%_prefix \
	--with-bdb-libdir-name=%_lib

%make

%install
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}%{_libdir}/libgda-%{api}/*/*.la

%find_lang %{pkgname}-%{api} --with-gnome

%if %{enable_test}
%check
make check
%endif

%files -f %{pkgname}-%{api}.lang
%doc AUTHORS COPYING README
%dir %{_sysconfdir}/libgda-%{api}
%config(noreplace) %_sysconfdir/libgda-%{api}/sales_test.db
%config(noreplace) %{_sysconfdir}/libgda-%{api}/config
%{_bindir}/*
%{_datadir}/applications/gda-browser-%{api}.desktop
%{_datadir}/applications/gda-control-center-%{api}.desktop
%{_datadir}/pixmaps/gda*
%{_datadir}/icons/hicolor/*/apps/gda-control-center.*
%{_datadir}/libgda-%{api}
%dir %{_libdir}/libgda-%{api}
%dir %{_libdir}/libgda-%{api}/plugins
%dir %{_libdir}/libgda-%{api}/providers
%{_libdir}/libgda-%{api}/plugins/*.xml
%{_libdir}/libgda-%{api}/plugins/libgda-ui-plugins.so
%{_libdir}/libgda-%{api}/providers/libgda-web.so
%{_libdir}/libgda-%{api}/providers/libgda-sqlcipher.so
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libgda-%{api}.so.%{major}*
%{_libdir}/libgda-report-%{api}.so.%{major}*
%{_libdir}/libgda-ui-%{api}.so.%{major}*
%{_libdir}/libgda-xslt-%{api}.so.%{major}*
%{_libdir}/girepository-1.0/Gda-%{api}.typelib
%{_libdir}/girepository-1.0/Gdaui-%{api}.typelib

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/libgda-%{api}/
%doc %{_datadir}/gtk-doc/html/gda-browser
%{_libdir}/libgda-%{api}.so
%{_libdir}/libgda-report-%{api}.so
%{_libdir}/libgda-ui-%{api}.so
%{_libdir}/libgda-xslt-%{api}.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gir-1.0/Gda-%{api}.gir
%{_datadir}/gir-1.0/Gdaui-%{api}.gir
%{_datadir}/gnome/help/gda-browser

%files sqlite
%{_libdir}/libgda-%{api}/providers/libgda-sqlite.so

%files postgres
%{_libdir}/libgda-%{api}/providers/libgda-postgres.so

%files bdb
%{_libdir}/libgda-%{api}/providers/libgda-bdb.so

%if %{build_mysql}
%files mysql
%{_libdir}/libgda-%{api}/providers/libgda-mysql.so
%endif

%if %{build_freetds}
%files freetds
%{_libdir}/libgda-%{api}/providers/libgda-freetds.so
%endif

%if %{build_mdb}
%files mdb
%{_libdir}/libgda-%{api}/providers/libgda-mdb.so
%endif

%ifnarch %arm %mips
%files jdbc
%{_libdir}/libgda-%{api}/providers/libgda-jdbc.so
%{_libdir}/libgda-%{api}/providers/gdaprovider-4.0.jar
%endif

%files ldap
%{_libdir}/libgda-%{api}/providers/libgda-ldap.so

