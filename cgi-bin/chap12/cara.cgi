#!/usr/bin/perl
#cara.cgi - Location header example
print "Content-type: text/html\n\n";
use CGI qw(:standard -debug);
use strict;

#declare and assign value to variable
my $name;
$name = param('Name');

#create Hello page
if ($name ne "") {
		
	print "<HTML>\n";
	print "<HEAD><TITLE>Cara Antiques</TITLE></HEAD>\n";
	print "<BODY>\n";
	print "<H1 ALIGN=center>Cara Antiques<HR>\n";
	print "Hello, $name!</H1></BODY></HTML>";
} 
else {
	
	print "Location: http://endor.vvc.edu/~williamng/public_html/chap12/cara2.html\n\n";
}






