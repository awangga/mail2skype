# mail2skype
Add skype contact(by send chat message) from email inbox body. Tested on Mac OSX Lion.

How It Works :
 1. Send email to your email account with any subject with body information word "Skype ID".
 2. Apps will read unread email for today and parsing email body then send chat message to it
 3. Reply email to sender for confirmation.

Instalation :
 1. Please run and Login into your Skype Client
 2. open end edit config.py with your email username and password
 3. enter terminal and run python runmefist.py
 4. if you in 64 bit version of mac osx please run : arch -i386 python2.6 runmefirst.py
 5. A dialog open from Skype Client, PLease Allow and always remember Skype4Py to connect to your Skype
 6. For gmail account please run : arch -i386 python2.6 main.py
 7. For live,hotmail,outlook, any microsoft email account please run : arch -i386 python2.6 outlook.py

Run :
 1. Open and Login to your skype client apps
 2. Open terminal and navigate to mail2skype directory
 3.	For gmail account, run command : python2.6 main.py ,if you run in 64 bit use : arch -i386 python2.6 main.py
 4. For outlook account, run command : python2.6 outlook.py ,if you run in 64 bit use : arch -i386 python2.6 outlook.py

Library :
 * https://github.com/awahlig/skype4py
 * https://pypi.python.org/pypi/Skype4Py/
 * https://github.com/charlierguo/gmail

Skype Name/ID Rule:
 * Contain number or letter or . , - _ with 6-32 char

Thanks to :
 * http://stackoverflow.com/questions/2088569/how-do-i-force-python-to-be-32-bit-on-snow-leopard-and-other-32-bit-64-bit-quest
 * http://stackoverflow.com/questions/4536146/need-an-python-script-that-uses-skype4py-to-send-an-instant-message

