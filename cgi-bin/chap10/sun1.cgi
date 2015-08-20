#!/usr/bin/perl
#sun1.cgi - displays a dynamic Web page listing available brochures
print "Content-type: text/html\n\n";
use CGI qw(:standard -debug);

#prevent Perl from creating undeclared variables
use strict;

#declare and assign values to variables
my($name, $email);
$name = param('Name');
$email = param('Email');

#create Brochure Listing form
print "<HTML>\n";
print "<HEAD><TITLE>Sun Travel</TITLE></HEAD>\n";
print "<BODY>\n";
print "<FORM 
        ACTION='http://endor.vvc.edu/~williamng/cgi-bin/chap10/sun2.cgi' 
        METHOD=POST>\n";
print "<!hidden fields>\n";
print "<input type=hidden name=H_name value='$name'>\n";
print "<input type=hidden name=H_email value=$email>\n";

print "<H1>Sun Travel Brochure Listing</H1><HR>\n";
print "<H3>Thank you, $name.<BR>\n";
print "Please select from our list of brochures:</H3>\n";
print "<SELECT NAME=Brochure SIZE=4>\n";
print "<OPTION VALUE=Aruba SELECTED>Aruba\n";
print "<OPTION VALUE=California>California\n";
print "<OPTION VALUE=Florida>Florida\n";
print "<OPTION VALUE=Jamaica>Jamaica\n";
print "</SELECT><BR><BR>\n";

print "<INPUT TYPE=submit VALUE=Submit>\n";
print "</FORM></BODY></HTML>\n";

