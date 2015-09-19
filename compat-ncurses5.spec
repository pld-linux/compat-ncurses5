#
# Conditional build:
%bcond_without	gpm		# build without (dynamically loadable) libgpm support

%define	basever	5.9
%define	patchlevel	20150117
Summary:	curses terminal control library - version 5.x for compatibility
Summary(pl.UTF-8):	Biblioteki curses do sterowania terminalem - wersja 5.x dla zgodności
Name:		compat-ncurses5
Version:	%{basever}.%{patchlevel}
Release:	1
License:	distributable
Group:		Libraries
Source0:	ftp://dickey.his.com/ncurses/ncurses-%{basever}.tar.gz
# Source0-md5:	8cb9c412e5f2d96bc6f459aa8c6282a1
# source: ftp://dickey.his.com/ncurses/5.9/
Patch0:		ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140308-patch.sh.bz2
# Patch0-md5:	8bd412a9c9ac97a2c504780ae87aa5d8
Patch1:		ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140315.patch.gz
# Patch1-md5:	1ddb1fbc5b301506e0522cc1364579b7
Patch2:		ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140322.patch.gz
# Patch2-md5:	e8af8722ca80e2c7693d07a1cb475235
Patch3:		ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140323.patch.gz
# Patch3-md5:	24fbdef991dd67b2557177e453efd572
Patch4:		ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140329.patch.gz
# Patch4-md5:	e7a772214088ca55185cd2230df2e9ee
Patch5:		ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140412.patch.gz
# Patch5-md5:	49762dfcdeb3f5da933319f58b9b4f18
Patch6:		ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140419.patch.gz
# Patch6-md5:	ec3760d2142cd0106a20db17a356a8cf
Patch7:		ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140426.patch.gz
# Patch7-md5:	b5df540a93b170ff946724b3a02125a2
Patch8:		ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140503.patch.gz
# Patch8-md5:	9885526f6f734e001ed6f55cd39a9feb
Patch9:		ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140510.patch.gz
# Patch9-md5:	bc591f4e1bf5dbf785b8c4c4eb5afce3
Patch10:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140524.patch.gz
# Patch10-md5:	b35022e923b354b95325e7f5f817c989
Patch11:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140607.patch.gz
# Patch11-md5:	ddfe11b9ed9477c785849c1b606d90dd
Patch12:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140609.patch.gz
# Patch12-md5:	769c45c1317021c471dd5036e7c172db
Patch13:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140614.patch.gz
# Patch13-md5:	13db4a8a7c62b4d825707c12e855dc57
Patch14:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140621.patch.gz
# Patch14-md5:	f6f582b7e76a9c1fedde3aafe6849f76
Patch15:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140629.patch.gz
# Patch15-md5:	65aa63ff4072642110f80542b3d9f885
Patch16:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140705.patch.gz
# Patch16-md5:	b5d3a9365a777e1ba0809edbca8fdebd
Patch17:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140712.patch.gz
# Patch17-md5:	9b97478790d5d6a539e6a4c0f9865ac6
Patch18:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140719.patch.gz
# Patch18-md5:	9bb67f50b2a08c8f2e1b909f68592ce8
Patch19:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140726.patch.gz
# Patch19-md5:	e45bdb82f2b3d03b5c42b85bf8f45365
Patch20:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140802.patch.gz
# Patch20-md5:	3afc2b4dd4afc2061705dd5ad3827e6b
Patch21:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140809.patch.gz
# Patch21-md5:	745c7b4660cc6a8b2982bfaefecb2184
Patch22:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140816.patch.gz
# Patch22-md5:	5aac11e74427728fa7a69d50fcdc6b6d
Patch23:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140823.patch.gz
# Patch23-md5:	a947c90441a6d1b2c8b3ce479938366c
Patch24:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140831.patch.gz
# Patch24-md5:	c44d667bacb27a46630e09ece9065468
Patch25:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140906.patch.gz
# Patch25-md5:	ff6b277fa958cccd9f74b403250bd0cf
Patch26:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140913.patch.gz
# Patch26-md5:	92433359cf3bf4d202212a2832b2521f
Patch27:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140920.patch.gz
# Patch27-md5:	70f40973fe4d96a58fb5b635be662bd5
Patch28:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20140927.patch.gz
# Patch28-md5:	649bd0ca7a2912b1b128b2073774f679
Patch29:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20141011.patch.gz
# Patch29-md5:	17e081953c7b54f12a53cd897a4edb60
Patch30:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20141018.patch.gz
# Patch30-md5:	eb676c1321f2964a9cb6d18dcfdc1a19
Patch31:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20141025.patch.gz
# Patch31-md5:	52c96fc7ec949b3c6e7fc765260eaaa4
Patch32:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20141101.patch.gz
# Patch32-md5:	e0644cdbb30184f3a424674d1480ce94
Patch33:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20141115.patch.gz
# Patch33-md5:	8fd3f6de88bec7a8afaa35d2e8c3ffb5
Patch34:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20141129.patch.gz
# Patch34-md5:	a3fd7e0cd2285dfcd47e43a6990b11d6
Patch35:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20141206.patch.gz
# Patch35-md5:	ba576465adfa4d9fadd2a1e4be5f0524
Patch36:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20141213.patch.gz
# Patch36-md5:	5b4cb12b7482133b2ce4d89ba8773200
Patch37:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20141220.patch.gz
# Patch37-md5:	793509c4f50168f6e152dca7fc9d91e5
Patch38:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20141221.patch.gz
# Patch38-md5:	0456dd738ecf3e58a0dc5d71efbd776f
Patch39:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20141227.patch.gz
# Patch39-md5:	8be86a8ff3da664b06a2b04ffc41318f
Patch40:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20150103.patch.gz
# Patch40-md5:	b5c653dbe82b7464a36ecc2e89b40da1
Patch41:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20150110.patch.gz
# Patch41-md5:	e662f8fd07bcb57fac68d9b05559929e
Patch42:	ftp://dickey.his.com/ncurses/5.9/ncurses-%{basever}-20150117.patch.gz
# Patch42-md5:	dcadc2d0b2bcc22f5546d5e02f51c26c

Patch100:	ncurses-screen_hpa_fix.patch
Patch101:	ncurses-xterm_hpa_fix.patch
Patch102:	ncurses-meta.patch
Patch103:	ncurses-xterm-home-end.patch
Patch104:	ncurses-mouse_trafo-warning.patch
Patch105:	ncurses-gnome-terminal.patch
# disable rain demo; triggers gcc bug: http://gcc.gnu.org/bugzilla/show_bug.cgi?id=14998
Patch107:	ncurses-no-rain-demo.patch
Patch108:	ncurses-fix-nonunicode-breakage.patch
URL:		http://dickey.his.com/ncurses/ncurses.html
BuildRequires:	automake
%{?with_gpm:BuildRequires:	gpm-devel}
BuildRequires:	pkgconfig
BuildRequires:	sharutils
# for (at least basic) terminfo database
Suggests:	ncurses >= %{version}
# for compatibility with old PLD packages
%ifarch %{x8664} ppc64 sparc64 s390x
Provides:	libtinfo.so.5()(64bit)
Provides:	libtinfow.so.5()(64bit)
%else
Provides:	libtinfo.so.5
Provides:	libtinfow.so.5
%endif
Obsoletes:	libncurses5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The curses library routines give the user a terminal-independent
method of updating character screens with reasonable optimization.
This implementation is ``new curses'' (ncurses) and is the approved
replacement for 4.4BSD classic curses, which is being discontinued.

%description -l de.UTF-8
Die curses-Library-Routinen geben dem Benutzer eine
Terminal-unabhängige Methode zur optimierten Aktualisierung von
zeichenbasierenden Bildschirminhalten an die Hand. Die vorliegende
Implementierung ist NEW CURSES (ncurses), die offizielle
Nachfolgerversion für 4.4BSC (die klassische curses-Version), welche
nicht weitergeführt wird.

%description -l es.UTF-8
Las rutinas de la biblioteca curses ofrecen al usuario un método
independiente de terminal para actualización de las pantallas de
caracteres con optimización razonable. Este soporte es "nuevo curses"
(ncurses) y es el substituto aprobado para los clásicos curses 4.4BSD,
que se quedaban desfasados.

%description -l fr.UTF-8
Les routines de la bibliothèque curses donnent à l'utilisateur une
méthode indépendante du terminal pour la mise à jour des écrans en
mode texte avec une optimisation correcte. Ceci est l'implantation du
« nouveau curses » (ncurses) et est le remplacement du curses 4.4BSD
classique qui est abandonné.

%description -l pl.UTF-8
Biblioteka curses udostępnia funkcje pozwalające użytkownikom na
odwoływanie się do zawartości terminala niezależnie od jego typu.
Pakiet ten zawiera implementację klasycznej biblioteki curses (z
systemu 4.4BSD) o nazwie ncurses (new curses) i jest zarazem jej
przyszłym zamiennikiem.

%description -l pt_BR.UTF-8
As rotinas da biblioteca curses fornecem ao usuário um método
independente de terminal para atualização das telas de caracteres com
otimização razoável. Essa implementação é "novo curses" (ncurses) e é
o substituto aprovado para os clássicos curses 4.4BSD, que estão se
tornando obsoletos.

%description -l ru.UTF-8
Программы библиотеки curses предоставляют пользователям возможность
терминально-независимого обновления символьных экранов с достаточной
оптимизацией. Эта реализация - "новые curses" (ncurses), которая
является одобренной заменой классической библиотеки curses из 4.4BSD,
в настоящее время "снятой с производства". В PLD Linux ncurses
является жизненно необходимой, без нее не будут функционировать многие
программы, составляющие базовую систему. Практически все программы,
которые выводят что-либо на терминал, используют ncurses. В PLD Linux
ни библиотека termcap, ни традиционный файл /etc/termcap, не
используются...

%description -l tr.UTF-8
curses kitaplığı ile kullanıcıya kullanılan terminal tipinden bağımsız
olarak karakter tabanlı ekranlara erişim olanağı sağlanabilmektedir.
Bu uyarlama 'new curses' (ncurses), BSD deki klasik curses'in gelişmiş
halidir.

%description -l uk.UTF-8
Програми бібліотеки curses дають користувачам можливість
термінально-незалежного поновлення символьних екранів з достатньою
оптимізацією. Ця реалізація - "нові curses" (ncurses), котра є
схваленою заміною класичної бібліотеки curses з 4.4BSD, яка наразі
"знята з виробництва". В PLD Linux ncurses є життєво необхідною, без
неї не буде працювати більшость програм, що складають базову систему.
Практично всі програми, котрі виводять щось на термінал,
використовують ncurses. В PLD Linux ані бібліотека termcap, ані
традиційний файл /etc/termcap не використовуються...

%package ext
Summary:	Additional ncurses libraries - version 5.x for compatibility
Summary(pl.UTF-8):	Dodatkowe biblioteki ncurses - wersja 5.x dla zgodności
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ext
This package contains addidion ncurses libraries like libforms,
libmenu and libpanel for easy making full screen curse application.

%description ext -l pl.UTF-8
Pakiet ten zawiera dodatkowe biblioteki libforms, libmenu i libpanel
służące do łatwego tworzenia aplikacji pełnoekranowych korzystających
z ncurses.

%prep
%setup -qc
mv ncurses-%{basever}/* .
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%{__rm} Ada95/src/library.gpr*
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1

%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch107 -p1
%patch108 -p1

%build
unset TERMINFO || :
gcc_target=$(gcc -dumpmachine)
gcc_version=%{cc_version}
CFLAGS="%{rpmcflags} -DPURE_TERMINFO -D_FILE_OFFSET_BITS=64"
cp -f /usr/share/automake/config.sub .

for t in narrowc wideclowcolor; do
install -d obj-$t
cd obj-$t
../%configure \
	--with-install-prefix=$RPM_BUILD_ROOT \
	--without-ada \
	--without-cxx \
	--without-cxx-binding \
	--with%{!?debug:out}-debug \
	--with%{!?with_gpm:out}-gpm \
	--with-largefile \
	--with-manpage-format=normal \
	--without-manpage-symlinks \
	--with-normal \
	--with-ospeed=unsigned \
	--with-pkg-config-libdir=%{_pkgconfigdir} \
	--without-profile \
	--with-shared \
	--without-static \
	--disable-lp64 \
	--enable-colorfgbg \
	--enable-hard-tabs \
	--enable-xmc-glitch \
	--with-chtype='long' \
	--with-mmask-t='long' \
	`[ "$t" = "narrowc" ] && echo --includedir=%{_includedir}/ncursesn` \
	`[ "$t" = "wideclowcolor" ] && echo --enable-widec --disable-ext-colors --includedir=%{_includedir}/ncurseswlc`

%{__make} -j1

cd ..
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

cp -a obj-narrowc/lib/lib{ncurses,form,menu,panel}.so.5* $RPM_BUILD_ROOT%{_libdir}
cp -a obj-wideclowcolor/lib/lib{ncurses,form,menu,panel}w.so.5* $RPM_BUILD_ROOT%{_libdir}
ln -sf $(basename $RPM_BUILD_ROOT%{_libdir}/libncurses.so.5.*) $RPM_BUILD_ROOT%{_libdir}/libtinfo.so.5
ln -sf $(basename $RPM_BUILD_ROOT%{_libdir}/libncursesw.so.5.*) $RPM_BUILD_ROOT%{_libdir}/libtinfow.so.5

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	ext -p /sbin/ldconfig
%postun	ext -p /sbin/ldconfig

%triggerpostun -- ncurses < 5.9-3
# rpm seems to remove them as those was %ghosts in ncurses < 5.9-3
# despite existing now as normal files/symlinks
ln -sf $(basename %{_libdir}/libncurses.so.5.*) %{_libdir}/libtinfo.so.5
ln -sf $(basename %{_libdir}/libncursesw.so.5.*) %{_libdir}/libtinfow.so.5
exit 0

%files
%defattr(644,root,root,755)
%doc ANNOUNCE README
%attr(755,root,root) %{_libdir}/libncurses.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libncurses.so.5
%attr(755,root,root) %{_libdir}/libncursesw.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libncursesw.so.5
# compatibility symlinks
%attr(755,root,root) %{_libdir}/libtinfo.so.5
%attr(755,root,root) %{_libdir}/libtinfow.so.5

%files ext
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libform.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libform.so.5
%attr(755,root,root) %{_libdir}/libmenu.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmenu.so.5
%attr(755,root,root) %{_libdir}/libpanel.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libpanel.so.5
%attr(755,root,root) %{_libdir}/libformw.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libformw.so.5
%attr(755,root,root) %{_libdir}/libmenuw.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmenuw.so.5
%attr(755,root,root) %{_libdir}/libpanelw.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libpanelw.so.5
