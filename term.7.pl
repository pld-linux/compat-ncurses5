.\"***************************************************************************
.\" Copyright (c) 1998 Free Software Foundation, Inc.                        *
.\"                                                                          *
.\" Permission is hereby granted, free of charge, to any person obtaining a  *
.\" copy of this software and associated documentation files (the            *
.\" "Software"), to deal in the Software without restriction, including      *
.\" without limitation the rights to use, copy, modify, merge, publish,      *
.\" distribute, distribute with modifications, sublicense, and/or sell       *
.\" copies of the Software, and to permit persons to whom the Software is    *
.\" furnished to do so, subject to the following conditions:                 *
.\"                                                                          *
.\" The above copyright notice and this permission notice shall be included  *
.\" in all copies or substantial portions of the Software.                   *
.\"                                                                          *
.\" THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS  *
.\" OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF               *
.\" MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.   *
.\" IN NO EVENT SHALL THE ABOVE COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,   *
.\" DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR    *
.\" OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR    *
.\" THE USE OR OTHER DEALINGS IN THE SOFTWARE.                               *
.\"                                                                          *
.\" Except as contained in this notice, the name(s) of the above copyright   *
.\" holders shall not be used in advertising or otherwise to promote the     *
.\" sale, use or other dealings in this Software without prior written       *
.\" authorization.                                                           *
.\"***************************************************************************
.\"
.\" $Id$
.\" Translation (c) 1998 Marcin Mazurek <mazek@capella.ae.poznan.pl>
.\" {PTM/MM/0.1/08-10-1998/"term.7 - zasady nazywania typ�w terminali"}
.TH TERM 7
.ds n 5
.ds d /usr/share/terminfo
.SH NAZWA
term \- zasady nazywania typ�w terminali
.SH OPIS
.PP
Zmienna �rodowiskowa \fBTERM\fR powinna standardowo zawiera� nazw� typu  
terminala, konsoli lub urz�dzenia wy�wietlaj�cego, kt�rego u�ywasz. 
Informacja ta jest niezb�dna dla wszystkich program�w wy�wietlaj�cych wyniki
na ekranie, w��czaj�c w to Tw�j edytor czy program pocztowy.
.PP
Standardowa warto�� zmiennej \fBTERM\fR b�dzie ustawiona poprzez
inicjalizacj� lini poprzez plik \fB/etc/inittab\fR (Linux i
System-V-podobne UNIXy)
lub plik \fB/etc/ttys\fR (BSD UNIXy). To prawie zawsze wystarczy dla stacji
roboczych czy konsoli mikrokomputer�w.
.PP
Je�li u�ywasz lini telefonicznej, typ urz�dzenia do��czonego do niej mo�e by�
r�ny. Starsze systemy UNIXowe ustawiaj� pocz�tkowo bardzo prosty typ
terminala np. `dumb' lub `dialup'.  Nowsze mog� u�ywa�
terminala `vt100', odzwierciedlaj�c rozpowszechnienie terminali DECa
VT100-kompatybilnych i emulator�w z komputer�w osobistych.
.PP
Nowoczesne telnet'y przekazuj� Twoj� zmienn� �rodowiskow� \fBTERM\fR z
lokalnego systemu do odleg�ego. Mog� wyst�pi� problemy je�eli terminfo lub  
termcap na odleg�ym systemie nie zawiera definicji terminala kompatybilnej z
Twoj�, ale ta sytuacja jest rzadka i mo�e by� prawie zawsze unikni�ta przez
ustawienie typu terminala na `vt100' (zak�adaj�c, �e rzeczywi�cie u�ywasz 
VT100-podobnej konsoli, terminala, lub emulatora terminala.)
.PP
W ka�dym razie, mo�esz dowolnie zmienia� zmienn� \fBTERM\fR ustawion� przez
Tw�j system na dowoln� warto�� w profilu Twojej pow�oki. Program \fBtset\fR(1) 
mo�e by� w tym pomocny; mo�esz mu poda� zbi�r regu� aby wydedukowa� lub
za��da� podania typu terminala bazuj�c na urz�dzeniu tty i pr�dko�ci
przesy�u danych (baud rate).
.PP
Ustawienie zmiennej \fBTERM\fR w�asn� warto�ci� mo�e by� tak�e u�yteczne
je�li stworzy�e� w�asn� definicj� terminala w��czaj�c opcje (takie jak 
widzialny dzwonek (czyli b�y�ni�cie ekranu) lub pod�wietlenie) kt�re maj�
zamieni� standardowe ustawienia systemu.
.PP
Opisy typ�w terminali s� przechowywane jako pliki zawieraj�ce dane opisuj�ce
ich mo�liwo�ci w katalogu \*d. Aby przejrze� list� wszystkich nazw terminali 
rozpoznawanych przez system, wykonaj 

	toe | more

z promptu pow�oki. Pliki te, opisuj�ce mo�liwo�ci terminali s� przechowywane
w formacie binarnym aby zapewni� optymaln� pr�dko�� dost�pu do nich
(odwrotnie ni� w przypadku starego bazuj�cego na tek�cie pliku \fBtermcap\fR, 
kt�ry zast�puj�); aby sprawdzi� jedn� z pozycji musisz u�y� komendy \fBinfocmp\fR(1).
Wywo�aj j� nast�puj�co:

	infocmp \fInazwa\fR

gdzie \fInazwa\fR jest nazw� typu terminala, kt�ry chcesz sprawdzi�
(i zarazem nazw� pliku w podkatalogu \*d nazwanym od pierwszej litery typu
terminala). Komenda ta wy�wietla plik z opisem terminala w formacie tekstowym
opisanym przez \fBterminfo\fR(\*n).  
.PP
Pierwsza linia \fBterminfo\fR(\*n) opisuje nazwy, pod kt�rymi terminfo
rozpoznaje terminal, nazwy przedzielone s� znakami `|', a ostatnia 
zako�czona jest przecinkiem.  Pierwsza nazwa jest podstawow� nazw�
terminala \fI(primary name)\fR, i powinna by� u�ywana przy ustawianiu
zmiennej \fBTERM\fR.  Ostatnia nazwa jest w
rzeczywisto�ci opisem typu terminala (mo�e zawiera� spacje; inne musz� by�
pojedynczymi s�owami). Nazwy pomi�dzy pierwsz�, a ostatni� (o ile istniej�)
s� aliasami nazwy terminala i zazwyczaj przechowywane s� tam dawne nazwy
terminala dla kompatybilno�ci.
.PP
Istniej� pewne konwencje jak dobiera� podstawowe nazwy terminala, kt�re
pozwalaj� aby by�y unikalne, a zarazem nios�y w sobie pewn� informacj�.
Poni�ej zamieszczony jest przewodnik, kt�ry krok po kroku wyja�nia jak
nazywa� a tak�e jak je rozumie�:
.PP
Najpierw wybierz g��wn� nazw�.  Powinna si� ona sk�ada� z ma�ej litery
i nast�puj�cych po niej do siedmiu ma�ych liter b�d� cyfr. Powiniene�
unika� u�ywania znak�w przestankowych w g��wnych nazwach, poniewa� s� one
u�ywane i interpretowane jako nazwy plik�w i meta-znak�w pow�oki
(np. takie jak !, $, *, ? etc.), umieszczone w nich mog� spowodowa� dziwne
i k�opotliwe zachowanie.
Uko�nik (/), czy jakikolwiek inny znak, kt�ry mo�e zosta� zinterpretowany
przez czyj� system plik�w (\e, $, [, ]), jest szczeg�lnie niebezpieczne 
(terminfo jest niezale�ne od platformy, wi�c wyb�r nazwy zawieraj�cej znaki
specjalne mo�e kt�rego� dnia spowodowa� pewne problemy dla przysz�ych
u�ytkownik�w). Znak kropki (.) jest wzgl�dnie bezpieczny o ile wyst�puje co
najwy�ej jedna w nazwie g��wnej; niekt�re starsze nazwy terminfo
wykorzystuj� j�.
.PP
Nazwa g��wna terminala lub typu konsoli stacji roboczej powinna prawie zawsze
zaczyna� si� od przedrostka sprzedawcy (np. \fBhp\fR dla Hewlett-Packard, \fBwy\fR
dla Wyse, czy \fBatt\fR dla terminali AT&T), lub popularn� nazw� lini
terminala (\fBvt\fR dla terminali typu  VT od DECa, czy \fBsun\fR dla
konsoli stacji roboczych Suna czy \fBregent\fR dla modeli ADDS Regent).
Mo�esz wylistowa� drzewo terminfo aby zobaczy� jakie przedrostki s� ju� w
powszechnym u�yciu.
Po nazwie g��wnej powinien znajdowa� si�, je�li to potrzebne, numer modelu;
a wi�c \fBvt100\fR, \fBhp2621\fR, \fBwy50\fR.
.PP
Nazw� g��wn� dla konsoli typu PC-Unix powinna by� nazwa systemu
operacyjnego np. \fBlinux\fR, \fBbsdos\fR, \fBfreebsd\fB, \fBnetbsd\fR.
\fINie\fR powinna to by� nazwa typu \fBconsole\fR czy jakakolwiek inna
og�lna nazwa kt�ra mo�e spowodowa� zamieszanie w �rodowisku o wielu
platformach. Je�li p�niej nast�puje numer modelu, powinien wskazywa� albo
numer wersji systemu operacyjnego lub numer wersji sterownika konsoli.
.PP
Nazw� g��wna dla emulatora terminala (zak�adaj�c �e nie pasuje do kt�rego�
ze standardu ANSI lub typu vt100) powinna by� nazwa programu lub z �atwo�ci�
rozpoznawalny skr�t (np. \fBversaterm\fR, \fBctrm\fR).
.PP
Po nazwie g��wnej, mo�esz doda� dowoln� lecz rozs�dn� ilo�� rozdzielonych
��cznikiem przyrostk�w okre�laj�cych specjalne w�a�ciwo�ci.
.TP 5
2p
Ma dwie strony pami�ci.  Podobnie 4p, 8p, itd.
.TP 5
mc
Magic-cookie.  Niekt�re terminale (szczeg�lnie starsze Wyse) mog� wspiera�
jedynie jeden atrybut bez utraty magic-cookie. Ich definicja w terminfo
zazwyczaj jest sparowana z inn� (kt�ra posiada ten przyrostek) aby wspiera�
du�� ilo�� atrybut�w.
.TP 5
-am
W��cza auto-margines (prawostronne zawijanie)
.TP 5
-m
Tryb mono - wy��czenie wsparcia dla kolor�w
.TP 5
-na
Bez strza�ek - termcap ignoruje strza�ki kt�re w rzeczywisto�ci s� na
terminalu, wi�c u�ytkownik mo�e u�ywa� ich lokalnie.
.TP 5
-nam
Bez auto-marginesu - Wy��cz opcj� am
.TP 5
-nl
Bez etykiet - wy��cz mi�kkie etykiety
.TP 5
-nsl
Bez lini statusu - zlikwiduj lini� statusu
.TP 5
-pp
Ma port drukarki kt�ry jest u�ywany
.TP 5
-rv
Terminal w odwr�conym trybie video (czarny na bia�ym)
.TP 5
-s
U�yj lini statusu.
.TP 5
-vb
U�yj widzialnego dzwonka (b�ysk) a nie kr�tkiego dzwi�ku.
.TP 5
-w
Szeroki; terminal jest w 132 kolumnowym trybie.
.PP
Standardowo, je�li typ Twojego terminala jest jednym z wariant�w, kt�ry ma za zadanie
okre�li� liczb� lini, przyrostek powinien znale�� si� tam pierwszy. Dla
hipotetycznego terminala FuBarCo model 2317 w 30-liniowym trybie z odwrotnym
wy�wietlaniem (reverse video), lepsz� nazw� by�aby \fBfubar-30-rv\fR
(ni� np. `fubar-rv-30').
.PP
Typy terminali, kt�re nie s� opisane jako samodzielne sekcje, a raczej jako
sk�adniki do do��czenia do innych sekcji poprzez \fBuse\fR,
s� rozr�niane poprzez u�ycie znak�w plus (+) a nie minus (-).
.PP
Komendy, kt�re u�ywaj� typu terminala aby kontrolowa� wy�wietlanie cz�sto
akceptuj� opcj� -T, kt�ra pozwala poda� typ terminala jako argument.
Takie programy powinny skorzysta� ze zmiennej �rodowiskowej \fBTERM\fR
kiedy opcja -T jest nie podana.
.SH PRZENO�NO��
Dla maksymalnej kompatybilno�ci ze starymi systemami UNIXowymi V, nazwy i
aliasy powinny by� unikalne w pierwszych 14 znakach.
.SH PLIKI
.TP 5
\*d/?/*
sk�pilowane pliki zawieraj�ce opisy terminali
.TP 5
/etc/inittab
inicjalizacja lini tyy (AT&T-podobne UNIXy).
.TP 5
/etc/ttys
inicjalizacja lini tty (BSD-podobne UNIXy).
.SH "ZOBACZ TAK�E"
\fBcurses\fR(3X), \fBterminfo\fR(\*n), \fBterm\fR(\*d).
.\"#
.\"# The following sets edit modes for GNU EMACS
.\"# Local Variables:
.\"# mode:nroff
.\"# fill-column:79
.\"# End:
