#!/usr/bin/perl
#c02ex4.cgi - creates a dynamic Web page
print "Content-type: text/html\n\n";

use CGI qw(:standard -debug);

#create Web page
print "<HTML>\n";
print "<HEAD><TITLE>Jackson Elementary School</TITLE><BASEFONT SIZE=5></HEAD>\n";
print "The spanish word for ", param(eng_word), " is ", param(span_word) ".\n";
print "<BODY>\n";

print "</BODY>\n";
print "</HTML>\n";
