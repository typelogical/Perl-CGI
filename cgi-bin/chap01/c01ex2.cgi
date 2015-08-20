#!/usr/bin/perl
#c01ex2.cgi - displays a message 
print "Content-type: text/html\n\n";
use CGI qw(:standard -debug);
#generate html
print "<html>\n";
print "<head><title>Message</title></head>\n";
print "<body>\n";
print "Perl statements \n";
print "end with a semicolon.\n";
print "</body>\n";
print "</html>\n";
