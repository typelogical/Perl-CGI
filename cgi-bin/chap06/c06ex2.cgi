#!/usr/bin/perl
#bonus.cgi - calculates a bonus amount and creates a dynamic Web page
#that contains form data and a bonus amount
print "Content-type: text/html\n\n";

#prevent Perl from creating undeclared variables
use strict;
use CGI qw(:standard); 
#declare variables
my($name, $sales, $rate, $bonus, $size, @errors);

#assign values to variables
$name = param('Salesperson');
$sales = param('Sales');
$rate = param('Rate');

#validate input data
if($name eq "" or $sales eq "" or $rate eq ""){
	push(@errors, "Input valid name, sales or rate");
}

if($rate < 0.05 and $rate > 0.10){
	push(@errors, "Enter a rate bewteen %5 and %10");
}

#calculate bonus amount
$bonus = $sales * $rate; 

#create Web page
if($size == 0){
	print "<HTML>\n";
	print "<HEAD><TITLE>Patton Industries</TITLE><BASEFONT SIZE=5></HEAD>\n";
	print "<H1>Bonus Calculation</H1>\n";
	print "<BODY>\n";
	print "Salesperson: $name<br>\n";
	printf "Your bonus is \$%.2f.<br><br>\n", $bonus;
	printf "You entered a sales amount of $%.2f and a\n", $sales;
	printf "bonus rate of %.2f.<br>\n", $rate;
	print "</BODY>\n";
	print "</HTML>\n";
}else{
	
	print "<HTML>\n";
	print "<HEAD><TITLE>Patton Industries</TITLE><BASEFONT SIZE=5></HEAD>\n";
	print "<H1>Bonus Calculation</H1>\n";
	print "<BODY>\n";
	for(my $x; $x < $size; $x = $x + 1){
		print "$errors[$x]<br>\n";
	}
	print "</BODY>\n";
	print "</HTML>\n";
	
}
	
