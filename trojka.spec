Summary:	A non-X game of falling blocks.
Summary(pl):	Nie-Xowa gra w spadaj±ce klocki
Name:		trojka
Version:	1.1
Release:	1
Copyright:	distributable
Group:		Games
Group(pl):	Gry
Source0:	ftp://sunsite.unc.edu:/pub/Linux/games/arcade/tetris/%{name}.tgz
Patch0:		trojka-FHS.patch
Patch1:		trojka-Makefile.patch
Patch2:		trojka-glibc.patch
BuildRequires:	ncurses-devel >= 5.0
Requires:	ncurses >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The game of Trojka involves a set of falling blocks. The point is to move
the blocks around as they fall, so that three of the same blocks end up
next to each other, either horizontally or diagonally. Once the blocks fill
up the entire game area, the game is over.

%description -l pl
Gra w Trojkê polega na manipulowaniu spadaj±cymi zestawami klocków. Celem
jest ustawianie ich w miarê ich spadania, tak ¿eby trzy klocki tego samego
rodzaju u³o¿y³y siê obok siebie, poziomo lub po przek±tnej. Gra koñczy siê,
gdy klocki wype³ni± ca³± planszê.

%prep
%setup -q -n trojka
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} CFLAGS="-DLINUX $RPM_OPT_FLAGS" LDFLAGS="-s" trojka

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/games
install -d $RPM_BUILD_ROOT%{_mandir}/man6
install -d $RPM_BUILD_ROOT/var/lib/games

gzip -9nf trojka.6 COPYRIGHT

install trojka $RPM_BUILD_ROOT%{_prefix}/games
install trojka.6.gz $RPM_BUILD_ROOT%{_mandir}/man6
touch $RPM_BUILD_ROOT/var/lib/games/trojka.scores

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(2755,root,games) %{_prefix}/games/trojka
%attr(664,root,games) /var/lib/games/trojka.scores
%{_mandir}/man6/*
%doc COPYRIGHT.gz
