#!/usr/bin/perl
#c04ex3.cgi - creates a dynamic Web page that acknowledges
#the receipt of a registration form
print "Content-type: text/html\n\n";
use CGI qw(:standard -debug);
use strict;

#declare variables
my($name, $serial, $model, $sysletter, @uses, $key);
my %models = ("JX", "Laser JX", "PL", "Laser PL", "XL", "ColorPrint XL");
my %systems = ("M", "Macintosh",
	       "U", "UNIX",
	       "W", "Windows");
my @primary_uses = ("Home", "Business", "Educational", "Other");
#assign input items to variables
$name = param('Name');
$serial = param('Serial');
$model = param('Model'); 
$sysletter = param('System');
@uses=(param('Use'), param('Use'));

#create Web page
print "<HTML><HEAD><TITLE>Juniper Printers</TITLE></HEAD>\n";
print "<BODY><H2>\n";
print "Thank you, $name, for completeing \n";
print "the registration form.<br><br>\n";
print "We have registered your Juniper $models{$model} printer, \n";
print "serial number $serial. \n";
print "You indicated that the printer will be used on a \n";
print "$systems{$sysletter} system.<br>\n";
print "The primary use for this printer are:"; 
foreach $key (@uses) {
	print "$primary_uses[$uses]<br>\n";
}
print "</H2></BODY></HTML>\n";



