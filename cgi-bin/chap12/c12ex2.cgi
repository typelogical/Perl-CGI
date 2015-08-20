#!/usr/bin/perl
#jackson.cgi - creates  a dynamic web page
print "Refresh: 5; url=http://endor.vvc.edu/~williamng/public_html/chap12/c12ex2.html\n";
print "Content-type: text/html\n\n";
use CGI qw(:standard);
#create web page
print "<html>\n";
print "<head><title>Jackson Elementary School</title><basefont size = 5></head>\n";
print "<bosdy>\n";
print "The capitol of ", param(state), " is ", param(cap), ".\n";
print "</body>\n";
print "</html>\n";
	
	