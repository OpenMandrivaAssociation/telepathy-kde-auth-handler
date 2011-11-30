%define rel 1

Summary:        UI/Kwallet Integration for telepathy-kde
Name:           telepathy-kde-auth-handler
Version:        0.2.0
Release:        %mkrel  %{rel}
Url:            https://projects.kde.org/projects/playground/network/telepathy/telepathy-auth-handler
Source0:        ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%name-%version.tar.bz2
License:        GPLv2+
Group:          Graphical desktop/KDE
BuildRequires:  kdelibs4-devel
BuildRequires:  telepathy-qt4-devel

%description
Provide UI/KWallet Integration For Passwords and SSL Errors on Account Connect

%files -f telepathy-auth-handler.lang
%{_kde_libdir}/kde4/libexec/telepathy-kde-auth-handler
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KDE.SASLHandler.service
%{_kde_datadir}/telepathy/clients/KDE.SASLHandler.client
#--------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang telepathy-auth-handler



