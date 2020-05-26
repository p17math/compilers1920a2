import re   


def replacement(m):	#"Callback" συνάρτηση για την μετατροπή HTML entities με την χρήση της μεθόδου sub() (ζητούμενο 6).
	if (m.group(1) == 'amp'):
		return '&'
	elif (m.group(1) == 'gt'):
		return '>'
	elif (m.group(1) == 'lt'):
		return '<'
	else:
		return ' '


text = open('testpage.txt','r').read()	    #"Διάβασμα" αρχείου κειμένου (testpage.txt) σε μια μεταβλητή text.


one = re.compile(r'<title>(.+?)</title>')     #1. Εξαγωγή και εκτύπωση του τίτλου (οτιδήποτε βρίσκεται μεταξύ <title> και </title>).
m = one.search(text)
print(m.group(1))


two = re.compile(r'<!--.*?-->',re.DOTALL)     #2. Απαλοιφή των σχολίων (οτιδήποτε βρίσκεται μεταξύ <!-- και -->).
text = two.sub('',text)



three = re.compile(r'<(script|style).*?>.*?</(script|style)>',re.DOTALL)    #3. Απαλοιφή των <script> και <style> tags με όλο τους το περιεχόμενο.
text = three.sub('',text)


four = re.compile(r'<a.*?href="(.+?)">(.*?)</a>',re.DOTALL)     #4. Εξαγωγή και εκτύπωση του συνδέσμου (ιδιότητα href) από <a> tags και του κειμένου τους.
for m in four.finditer(text):
	print (m.group(1),m.group(2))


five = re.compile(r'<[^>]+>',re.DOTALL)		#5. Απαλοιφή όλων των tags από το κείμενο.
text = five.sub('',text)


six = re.compile(r'&(amp|gt|lt|nbsp);')		#6. Μετατροπή των ειδικών HTML entities που υπάρχουν στο κείμενο σύμφωνα με τον πίνακα που δώθηκε.
text = six.sub(replacement,text)


seven = re.compile(r'\s+')		#7. Μετατροπή ακολουθιών συνεχόμενων χαρακτήρων whitespace σε ένα ακριβώς κενό.
text = seven.sub(' ',text)


print(text)		#8. Στο τέλος τυπώστε και το κείμενο, όπως έχει διαμορφωθεί μετά τις προηγούμενες μετατροπές.
