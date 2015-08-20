#!\usr\bin\perl
#file: c03ex6.cgi

use strict;
use CGI qw(:standard);
#associate file type
print "Content-type: text/html\n\n";
#delcare variables
my($item_name, $item_quantity, $shipping_box_capacity,
  $full_boxes, $items_remaining);

#initialize values
$item_name = param('Item_Name');
$item_quantity = param('Item_Quantity');
$shipping_box_capacity = param('Shipping_Box_Cap');

#do calculation
$full_boxes = $item_quantity/$shipping_box_capacity;
$items_remaining = $item_quantity % $shipping_box_capacity;

#create webpage
print "<html>\n";
print "<head><title>Colfax Industries</title></head>\n";
print "<body>\n";

print "Item Name : $item_name<br>\n";
print "Item Quantity: $item_quantity<br>\n";
print "Shipping Capacity: $shipping_box_capacity<br>\n";
print "<br>";
print "Items Remaining: $items_remaining\n";

print "</body>\n";

print "</html>";
