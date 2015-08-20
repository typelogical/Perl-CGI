#!/usr/bin/perl
#c05ex5.cgi - displats the registration statistics for a Seminar
print "Content-type: text/html\n\n";
use CGI qw(:standard);
use strict; 
# print "This is a test";
# delcare variables
my ($name, $seminar, @records, $total_registered); 
my @seminars = ("Computer Maintenance", 
		"Microsoft Office", 
		"Unix Essentials", 
		"CGI/Perl");
my @seminar_count = (0, 0, 0, 0);


open(INFILE, "<", "c05ex5.txt") or die "Opening of c05ex5.txt failed, $!, stopped.";
@records = <INFILE>;
print "<HTML>";
print "<HEAD><TITLE>Seminar Workshop</TITLE></HEAD>";
print "<BODY>\n<H1>Seminar Workshop Registrations</H1><HR>\n";

print "<br>\n";
print "<table>\n";
print "<tr>\n";
print "<td><h4>Seminar</h4></td>\n";
print "<td><h4>Registered</h4></td></tr>\n";
$total_registered = 0;
foreach my $recs (@records){
	chomp($recs);
	($name, $seminar) = split(/,/, $recs);
	$seminar_count[$seminar - 1] += 1;
	$total_registered += 1;
}
my ($i);
for( $i = 1; $i <= 4; $i = $i + 1){
	print "\n<tr>\n<td>$seminars[$i-1]</td><td>     $seminar_count[$i-1]</td>\n</tr>";
}
print "\n<tr><td><br><br>Total Registered: $total_registered</td></tr>";
print "</table>\n</BODY>\n</HTML>\n";