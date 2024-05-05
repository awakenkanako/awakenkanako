#!/usr/bin/perl

print "Content-Type: text/html\n\n";
@music = ('chocobo','deepblue','fatehaze','ff','ff5a01','ff5battle','ff5drgn','ff5gilg',
	'ff5home','ff5intro','ff5mbox','ff5seal','ff5townx','ff5unlan','ff5worus',
	'lenna','mog');
srand(time^$$);
$n = int(rand(@music));
print "<html><body><bgsound src=music/$music[$n].mid loop=infinite></body></html>";
exit;