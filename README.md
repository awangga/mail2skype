# mail2skype
Add skype contact(by send chat message) from email inbox body.

How It Works :
 1. Send email to your gmail account with any subject with body only skype id wnd with #, example : awangga.net#
 2. Apps will read unread email and parsing body with # end act as Skype ID and send chat message to it

Instalation :
 1. Please run and Login into your Skype Client
 2. enter terminal and run python runmefist.py
 3. if you in 64 bit version of mac osx please run : arch -i386 python2.6 runmefirst.py
 4. Open dialog on Skype Client, PLease Allow and alwasy remember Skype4Py to connect to your Skype Apps
 5. Open main.py edit #change to your gmail account and password

Run :
 1. python2.6 main.py if you run in 64 bit use : arch -i386 python2.6 main.py
 2. add it to your crontab for running per minutes
 3. please keep Skype Client running and login in.

Library :
 * https://github.com/awahlig/skype4py
 * https://pypi.python.org/pypi/Skype4Py/
 * https://github.com/charlierguo/gmail

Thanks to :
 * http://stackoverflow.com/questions/2088569/how-do-i-force-python-to-be-32-bit-on-snow-leopard-and-other-32-bit-64-bit-quest
 * http://stackoverflow.com/questions/4536146/need-an-python-script-that-uses-skype4py-to-send-an-instant-message

