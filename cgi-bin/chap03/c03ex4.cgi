#!/usr/bin/perl
#c03ex4.cgi - calculates the discount price of product
use CGI qw(:standard -debug);
use strict;
print "Content-type: text/html\n\n";

#declare varaiables
my ($original_price, $discount_rate, $discount_price);

#give values to variables
$original_price = param('Original_Price');
$discount_rate = param('Discount_Price');
#calculate discount price
$discount_price = $original_price * (1 - $discount_rate);

#create webpage
print "<html>\n";
print "<head><title>Discount Price</title></head>\n";
print "<body>\n";
print "<h1>Discount Price</h1><br>\n";
print "<table>\n";
print "<tr>\n";
print "<td>Original Price: </td>"; printf "<td\$>%.2f</td>\n", $original_price;
print "</tr>\n";
print "<tr>\n";
print "<td>Discount rate: </td>"; printf "<td>%.2f</td>\n", $discount_rate;
print "</tr>\n";
print "<tr>\n";
print "<td>Discount: </td>"; printf "<td>\$%.2f</td>\n", $discount_price;
print "</tr>\n";
print "</table>\n";
print "</body>\n";
print "</html>\n";