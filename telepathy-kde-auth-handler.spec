%define srcname ktp-auth-handler

Summary:	UI/Kwallet Integration for telepathy-kde
Name:		telepathy-kde-auth-handler
Version:	0.5.1
Release:	2
Url:		https://projects.kde.org/projects/playground/network/telepathy/telepathy-auth-handler
Source0:	ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%srcname-%version.tar.bz2
License:	GPLv2+
Group:		Networking/Instant messaging 
BuildRequires:	telepathy-kde-common-internals-devel
BuildRequires:	pkgconfig(QJson)
Requires:	telepathy-kde-common-internals-core

%description
Provide UI/KWallet Integration For Passwords and SSL Errors on Account Connect.

%files -f ktp-auth-handler.lang
%{_kde_libdir}/kde4/libexec/ktp-auth-handler
%{_datadir}/telepathy/clients/KTp.SASLHandler.client
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.SASLHandler.service

#------------------------------------------------------------------------------

%prep
%setup -q -n %srcname-%version

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang ktp-auth-handler
