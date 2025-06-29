# This is 71st code of this python course
# This code demonstrates the use of Notification from plyer module
# This is an mini experimental project...which reminds to drink water...according to custom time

import time
from plyer import notification

while(True):
    notification.notify(title =f'Please Drink Water',app_name="Drinking water" ,message="It's been a long time, please drink water",timeout=10 )
    time.sleep(20)
