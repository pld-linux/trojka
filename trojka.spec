Summary: A non-X game of falling blocks.
Name: trojka
Version: 1.1
Release: 13
Copyright: distributable
Group: Amusements/Games
Source: sunsite.unc.edu:/pub/Linux/games/arcade/tetris/trojka.tgz
Patch0: trojka-fsstnd.patch
Patch1: trojka-misc.patch
Patch2: trojka-glibc.patch
BuildRoot: /var/tmp/trojka-root

%description
The game of Trojka involves a set of falling blocks.  The point is
to move the blocks around as they fall, so that three of the same blocks
end up next to each other, either horizontally or diagonally.  Once the
blocks fill up the entire game area, the game is over.

Install the trojka package if you want to play a non-X game of falling
blocks.

%prep
%setup -q -n trojka
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS" linux

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{games,man/man6}
mkdir -p $RPM_BUILD_ROOT/var/lib/games

install -m755 -s trojka $RPM_BUILD_ROOT/usr/games
install -m644 trojka.6 $RPM_BUILD_ROOT/usr/man/man6/trojka.6
cp /dev/null $RPM_BUILD_ROOT/var/lib/games/trojka.scores
chmod 666 $RPM_BUILD_ROOT/var/lib/games/trojka.scores

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/games/trojka
/usr/man/man6/trojka.6
/var/lib/games/trojka.scores
