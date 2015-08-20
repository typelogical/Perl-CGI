#!/usr/bin/perl
#jackson.cgi - creates  a dynamic web page
print "Content-type: text/html\n\n";
use CGI qw(:standard);
#create web page
print "<html>\n";
print "<head><title>Jackson Elementary School</title><basefont size = 5></head>\n";
print "<bosdy>\n";
print "The capitol of ", param(state), " is ", param(cap), ".\n";
print "</body>\n";
print "</html>\n";
	
	