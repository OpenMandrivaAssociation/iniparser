%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	C library for parsing "INI-style" files
Name:		iniparser
Version:	4.1
Release:	1
License:	MIT
Group:		System/Libraries
Url:		http://ndevilla.free.fr/iniparser/
Source0:	https://github.com/ndevilla/iniparser/archive/v%{version}.tar.gz
Patch0:		iniparser-3.1-makefile.patch

%description
iniParser is an ANSI C library to parse "INI-style" files, often used to
hold application configuration information.


%package -n %{libname}
Summary:	C library for parsing "INI-style" files
Group:		System/Libraries

%description -n %{libname}
iniParser is an ANSI C library to parse "INI-style" files, often used to
hold application configuration information.

%package -n %{devname}
Summary:	Header files, libraries and development documentation for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q

%build
%setup_compile_flags
%make_build

%install
# iniParser doesn't have a 'make install' of its own :(
install -d %{buildroot}%{_includedir} %{buildroot}%{_libdir}
install -m 644 -t %{buildroot}%{_includedir}/ src/dictionary.h src/iniparser.h
install -m 755 -t %{buildroot}%{_libdir}/ libiniparser.so.%{major}
ln -s libiniparser.so.%{major} %{buildroot}%{_libdir}/libiniparser.so

%files -n %{libname}
%{_libdir}/libiniparser.so.%{major}*

%files -n %{devname}
%doc LICENSE
%{_libdir}/libiniparser.so
%{_includedir}/*.h

