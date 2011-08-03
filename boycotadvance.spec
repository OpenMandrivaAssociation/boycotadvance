%define name	boycotadvance
%define version	0.2.8
%define release	%mkrel 0.r1.4

Summary:	Gameboy Advance emulator
Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		1
Group:		Emulators
License:	Freeware
URL:		http://boycottadvance.emuunlim.com/
Source0:	http://sdlemu.ngemu.com/releases/BoyCottAdvance-SDL-0.2.8R1.i386.linux.tar.gz
BuildRequires:	chrpath
BuildRoot:	%{_tmppath}/%{name}-root
ExclusiveArch:	%ix86

%description
Boycot Advance is a portable program for emulating the Nintendo 
Gameboy Advance software platform.

%prep
%setup -q -n boyca-sdl
%__perl -p -i -e 's|\r\n|\n|g' docs/*.TXT

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_bindir}
chrpath -d boyca
%__install -m 755 boyca %{buildroot}%{_bindir}/boyca
%__mkdir_p %{buildroot}%{_sysconfdir}
%__install -m 755 boyca.cfg %{buildroot}%{_sysconfdir}/boyca.cfg
(cd %{buildroot}%{_bindir} && %__ln_s %{_sysconfdir}/boyca.cfg boyca.cfg)

%files
%defattr(0644,root,root,0755)
%doc boyca.cfg docs/*.TXT PongFighter/*.zip
%attr(0755,root,root) %{_bindir}/boyca
%config(noreplace) %{_sysconfdir}/boyca.cfg
%{_bindir}/boyca.cfg

%clean
%__rm -rf %{buildroot}

