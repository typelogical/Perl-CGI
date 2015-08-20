#!/usr/bin/perl
#c01ex3.cgi - displays a message 
print "Content-type: text/html\n\n";
use CGI qw(:standard -debug);
#generate html
print "<html>\n";
print "<head><title>Message</title></head>\n";
print "<body>\n";
print "Perl is powerful.<br>\n";
print "Perl is easy to learn.<br>\n";
print "Perl is free.\n";
print "</body>\n";
print "</html>\n";
