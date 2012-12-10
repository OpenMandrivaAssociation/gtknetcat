Summary:	Easy-to-use and handy GUI frontend of netcat (nc) command
Name:     	gtknetcat
Version:	0.1
Release:	%mkrel 5
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


%changelog
* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 0.1-5mdv2011.0
+ Revision: 593900
- rebuild for py2.7

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.1-4mdv2010.1
+ Revision: 437830
- rebuild

* Fri Mar 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-3mdv2009.1
+ Revision: 349487
- fix netcat dependency

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.1-2mdv2009.1
+ Revision: 325637
- rebuild

* Thu Jul 17 2008 Funda Wang <fwang@mandriva.org> 0.1-1mdv2009.0
+ Revision: 237691
- import gtknetcat


