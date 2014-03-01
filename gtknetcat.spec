%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Easy-to-use and handy GUI frontend of netcat (nc) command
Name:		gtknetcat
Version:	0.1
Release:	6
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxde.sourceforge.net/
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.gz
BuildRequires:	intltool
BuildRequires:	pkgconfig(gnome-python-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
Requires:	gnome-python
Requires:	netcat
Requires:	pygtk2.0-libglade

%description
Easy-to-use and handy GUI frontend of netcat (nc) command letting you
transfer files to another computer via direct wired connection.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libdir}/*.py
%{_datadir}/applications/*.desktop
%{python_sitelib}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

