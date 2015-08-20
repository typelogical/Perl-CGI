#!/usr/bin/perl
 #c12ex4a.cgi - calculates a bonus amount and creates a dynamic Web page
 #that contains form data and a bonus amount
print "Content-type: text/html\n\n";
 use CGI qw(:standard);

 #prevent Perl from creating undeclared variables
 use strict;

 #declare variables
 my ($name, $sales, $rate, $bonus, @empty, $size, $url);

 #assign values to variables
 $name = param('Salesperson');
 $sales = param('Sales');
 $rate = param('Rate');
 
 
 if($name eq "") {
     push(@empty, "NameEmpty=y");
 }
 if($sales eq "") {
     push(@empty, "SalesEmpty=y");
    }
 if($rate eq "") {
     push(@empty, "RateEmpty=y");
}

 $size = @empty;
 #remove leading and trailing spaces
 $name =~ s/^ +//;
 $name =~ s/ +$//;
 $sales =~ s/^ +//;
 $sales =~ s/ +$//;
 $rate =~ s/^ +//;
 $rate =~ s/ +$//;     

 
 if($size != 0) {
     $url = "http://endor.vvc.edu/~williamng/public_html/chap12/c12ex4b.cgi";
     $url .= "?";
     my  $i = 0;
     for ($i; $i < $size -1; ++$i) {
          $url .= "$empty[$i]+";
     }
     $url .= "$empty[$i]";
      
 
 print "Location: $url\n\n";
 }
 else {
 print "Content-type: text/html\n\n";
 #calculate bonus amount
 $bonus = $sales * $rate;

 #create Web page
 print "<HTML>\n";
 print "<HEAD><TITLE>Patton Industries</TITLE><BASEFONT SIZE=5></HEAD>\n";
 print "<H1>Bonus Calculation</H1>\n";
 print "<BODY>\n";
 print "Salesperson: $name<BR>\n";
 printf "Your bonus is \$%.2f.<BR><BR>\n", $bonus;
 printf "You entered a sales amount of \$%.2f and a \n", $sales;
 printf "bonus rate of %.1f%%.<BR>\n", $rate * 100;
 print "</BODY>\n";
 print "</HTML>\n";
 }