Summary:	Easy-to-use and handy GUI frontend of netcat (nc) command
Name:     	gtknetcat
Version:	0.1
Release:	%mkrel 3
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
URL:		http://lxde.sourceforge.net/
Requires:	netcat
Requires:	libglade2.0
Requires:	gnome-python
%py_requires
BuildRequires:	gnome-python-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Easy-to-use and handy GUI frontend of netcat (nc) command letting you
transfer files to another computer via direct wired connection.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/%name
%{python_sitelib}/%name
%{_libdir}/*.py
%{_datadir}/applications/*.desktop
