#!/usr/bin/perl
#c04ex2.cgi - creates a dynamic Web page that acknowledges
#the receipt of a registration form
print "Content-type: text/html\n\n";
use CGI qw(:standard -debug);
use strict;

#declare variables
my($name, $serial, $model, $sysnum);
my %models = ("JX", "Laser JX", "PL", "Laser PL", "XL", "ColorPrint XL");
my @systems = ("Windows", "Macintosh", "UNIX");
#assign input items to variables
$name = param('Name');
$serial = param('Serial');
$model = param('Model'); 
$sysnum = param('System');


#saves the form data and creates Web page
open(OUTFILE, ">>", "c05ex4.txt") or die "Unable to open c05ex4.txt for logging $!, stopped";
print OUTFILE "$name|$serial|$model|$sysnum\n";
print "<HTML><HEAD><TITLE>Juniper Printers</TITLE></HEAD>\n";
print "<BODY><H2>\n";
print "Thank you, $name, for completeing \n";
print "the registration form.<br><br>\n";
print "We have registered your Juniper $models{$model} printer, \n";
print "serial number $serial. \n";
print "You indicated that the printer will be used on a \n";
print "$systems[$sysnum] system.<br>\n";
print "</H2></BODY></HTML>\n";



