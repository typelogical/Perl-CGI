#!/usr/bin/perl
#c11ex5.cgi - displays a Web page containing the user's
#name and the book information
use CGI qw(:standard -debug);

#prevent Perl from creating undeclared variables
use strict;

#delcare and assign values to variables
my $times_visited;
$times_visited = cookie('Times Visited');

$times_visited += 1;

#create cookie
my $C_times_visited = cookie(-name => "Times Visited", -value => "$times_visited", 
		    -path => "/cgi-bin/chap11/", -exprires => "+6M");
#send cookie to browser
print header('Times Visited');

#create webpage

print >> endhtml;



