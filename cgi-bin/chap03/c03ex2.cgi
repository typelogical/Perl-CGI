#!/usr/bin/perl
#c03ex2.cgi - calculates gross pay and creates a dynamic Web page
#that contains form data and the gross pay
print "Content-type: text/html\n\n";

#prevent Perl from creating undeclared variables
use strict; 
use CGI qw(:standard);
#declare variables
my($employee, $hours, $rate, $gross_pay); 

#assign values to variables
$employee = param('Employee'); 
$hours = param('Hours');
$rate = param('Rate');

#calculate gross pay amount
$gross_pay = $hours * $rate;


#create Web page
print "<HTML>\n";
print "<HEAD><TITLE>AeroDynamics</TITLE><BASEFONT SIZE=5></HEAD>\n";
print "<H1>Gross Pay Calculation</H1>\n";
print "<BODY>\n";

print "Employee: $employee <br>\n";
print "Hours: $hours <br>\n";
print "Rate: $rate <br>\n";
printf "Gross Pay: %.2f <br>", $gross_pay;  


print "</BODY>\n";
print "</HTML>\n";
