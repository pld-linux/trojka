Summary:	A non-X game of falling blocks
Summary(pl):	Nie-Xowa gra w spadaj±ce klocki
Name:		trojka
Version:	1.1
Release:	20
License:	distributable
Group:		Applications/Games
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/arcade/tetris/%{name}.tgz
# Source0-md5:	e5d09a395df937b4e09a089013648a77
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-Makefile.patch
Patch2:		%{name}-glibc.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The game of Trojka involves a set of falling blocks. The point is to
move the blocks around as they fall, so that three of the same blocks
end up next to each other, either horizontally or diagonally. Once the
blocks fill up the entire game area, the game is over.

%description -l pl
Gra w Trojkê polega na manipulowaniu spadaj±cymi zestawami klocków.
Celem jest ustawianie ich w miarê ich spadania, tak ¿eby trzy klocki
tego samego rodzaju u³o¿y³y siê obok siebie, poziomo lub po
przek±tnej. Gra koñczy siê, gdy klocki wype³ni± ca³± planszê.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} CFLAGS="-DLINUX %{rpmcflags}" LDFLAGS="%{rpmldflags}" trojka

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/games,%{_mandir}/man6,/var/games}

install trojka $RPM_BUILD_ROOT%{_prefix}/games
install trojka.6 $RPM_BUILD_ROOT%{_mandir}/man6
touch $RPM_BUILD_ROOT/var/games/trojka.scores

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(2755,root,games) %{_prefix}/games/trojka
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/trojka.scores
%{_mandir}/man6/*
%doc COPYRIGHT
