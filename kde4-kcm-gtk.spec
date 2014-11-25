Summary:	Configure the appearance of GTK apps in KDE
Name:		kde4-kcm-gtk
Version:	0.5.3
Release:	1
License:	GPL v2+
Group:		X11/Applications
URL:		https://launchpad.net/kcm-gtk
Source0:	http://launchpad.net/kcm-gtk/0.5.x/%{version}/+download/kcm-gtk_%{version}.orig.tar.gz
# Source0-md5:	b49e2df3cce3bcb8c6dc96e7af73716d
Patch1:		kcm-gtk-0.5.3-settings_category.patch
Patch2:		kcm-gtk-0.5.3-gtkrc_setenv.patch
Patch3:		kcm-gtk-0.5.3-fix-de.patch
Patch4:		kubuntu_01_xsettings_kipc.patch
BuildRequires:	gettext
BuildRequires:	kde4-kdelibs-devel >= 4.8
Requires:	kde4-kdebase-runtime

%description
This is a System Settings configuration module for configuring the
appearance of GTK apps in KDE.

%prep
%setup -q -n kcm-gtk-%{version}
%patch1 -p1 -b .settings_category
%patch2 -p1 -b .gtkrc_setenv
%patch3 -p1 -b .fix-de
%patch4 -p1 -b .xsettings_kipc

# fixup for kde-4.5+, see http://bugzilla.redhat.com/628381
sed -i.kde45 -e 's|^X-KDE-System-Settings-Parent-Category=appearance$|X-KDE-System-Settings-Parent-Category=application-appearance|' \
  kcmgtk.desktop

%build
install -d build
cd build
%{cmake} ..

%{__make}


%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang kcm_gtk

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kcm_gtk.lang
%defattr(644,root,root,755)
%doc Changelog
%attr(755,root,root) %{_libdir}/kde4/kcm_gtk.so
%{_iconsdir}/kcm_gtk.png
%{_datadir}/kde4/services/kcmgtk.desktop
