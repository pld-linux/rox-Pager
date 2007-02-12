%define _name Pager
%define	_platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	Show a miniature view of your desktop
Summary(pl.UTF-8):   Wyświetlanie miniatur pulpitów
Name:		rox-%{_name}
Version:	1.0.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/pager-%{version}.tgz
# Source0-md5:	78e00f3d0d827edfe182bf4db906272a
Source1:	%{name}.desktop
URL:		http://rox.sourceforge.net/phpwiki/index.php/Pager
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libwnck-devel >= 0.14
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	pkgconfig
Requires:	rox >= 2.2.0-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir %{_libdir}/ROX-apps

%description
ROX-Pager is an applet for the ROX panel that shows you a miniature
view of your desktop.

%description -l pl.UTF-8
ROX-Pager jest apletem, który pokazuje miniatury pulpitów.

%prep
%setup -q -n pager-%{version}

%build
cd %{_name}
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,%{_platform},Messages}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

cd %{_name}
install .DirIcon *Run *.xml $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install %{_platform}/Pager $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}
install Messages/*.gmo $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Messages
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install .DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Pager/Help/Changes
%attr(755,root,root) %{_appsdir}/%{_name}/*Run
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}
%dir %{_appsdir}/%{_name}
%{_appsdir}/%{_name}/.DirIcon
%{_appsdir}/%{_name}/*.xml
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}/Messages
%lang(it) %{_appsdir}/%{_name}/Messages/it.gmo
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
