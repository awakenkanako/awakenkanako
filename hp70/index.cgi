#!/usr/bin/perl

print "Content-Type: text/html\n\n";
require('doorserif.pl');
print "<html><head><link rel=shortcut icon href=gmtgame.ico><title>GMT Game's</title></head><body><center><font size=2>GMT Game's</font></center><p><a href=main.html><center><img src=";
( $sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst ) =
localtime(time);
if(($mon==2 && $mday==1) || ($mon==7 && $mday==15) || ($mon==5 && $mday==6) ||
($mon==6 && $mday==17) || ($mon==9 && $mday==3)) 
{ print "images/Taeguk.gif border=0 width=300 height=200";}
else {print "images/door.jpg border=0 width=162 height=213";}
print "></a></p>
<font size=2 face=HY엽서L>";
srand(time^$$);
$n = int(rand(28));
print "$ment[$n]</font><br></center> <p align=right><font size=2 color=purple>$from[$n]</p></font><center><font size=2>당신은<img src=http://home.bawi.org/~potator/tiny/tiny.cgi>번째 손님입니다.</center></font></body> </html>";
exit;
