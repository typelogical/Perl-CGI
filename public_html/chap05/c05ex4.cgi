<!c05ex4.html>
<HTML>
<HEAD><TITLE>Juniper Printers</TITLE></HEAD>
<BODY>
<H1>Juniper Printers - Product Registration Form</H1>
<HR>

<FORM ACTION="../../cgi-bin/chap05/c05ex4a.cgi" METHOD=POST>
<P><B>Name:</B>       <INPUT TYPE=text NAME=Name   SIZE=40>
<B>Serial number:</B> <INPUT TYPE=text NAME=Serial SIZE=10></P>

<P><B>Printer model:</B><BR>
<INPUT TYPE=radio NAME=Model Value=0 CHECKED> Laser JX<BR>
<INPUT TYPE=radio NAME=Model Value=1>         Laser PL<BR>
<INPUT TYPE=radio NAME=Model Value=2>         ColorPrint XL</P>

<P><B>Operating system:</B><BR>
<INPUT TYPE=radio NAME=System Value=W CHECKED> Windows<BR>
<INPUT TYPE=radio NAME=System Value=M>         Macintosh<BR>
<INPUT TYPE=radio NAME=System Value=U>         UNIX</P>

<P><INPUT TYPE=submit VALUE="Submit Registration">
<INPUT TYPE=reset     VALUE="Reset the Form"></P>

<A HREF="../../cgi-bin/chap05/c05ex4b.cgi">View Registration File
</FORM></BODY></HTML>
