#!/usr/bin/perl
#c10ex3b.cgi - second script
print "Content-type: text/html\n\n";
use CGI qw(:standard -debug);

#prevent Perl from creating undeclared variables
use strict;

#declare and assign value to variable
my($bgcolor);
$bgcolor = param('Color');
#create Web page
print "<HTML>\n";
print "<HEAD><TITLE>Maribeth Designs</TITLE></HEAD>\n";
print "<BODY BGCOLOR = '$bgcolor'>\n";
print "<H1>Maribeth Designs</H1>\n";
print "<I>Thank you for visiting our Web site!</I>\n";
print "</BODY></HTML>\n";
