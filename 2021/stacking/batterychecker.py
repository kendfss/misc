'''
https://stackoverflow.com/questions/66198494/how-can-i-get-this-recurring-script-to-only-run-if-the-response-box-isnt-presen
'''
import os
import time
import threading
import pickle

limit = 35
save_p = 'save.p'

#Load in pickle
boxStatus = pickle.load(open(save_p, "rb" ))

def getStats():
    #There is a function here that reads the battery percentages
    mouse = 30 #for testing, I set mouse to 30
    keyboard = 70 #for testing, I set keyboard to 70
    return mouse, keyboard

def box(body):
    global r
    r = os.system("osascript -e 'Tell application \"System Events\" to display dialog \"" + body + "\"'")

def wait(body):
    boxStatus = False
    pickle.dump(boxStatus, open(save_p, "wb"))
    done = False
    while not done:
        thread = threading.Thread(target=box(body))
        thread.start()
        thread.join()
        if r == 0:
            #OK             
            boxStatus = True
            pickle.dump(boxStatus, open(save_p, "wb"))
            done = True
        if r == 256:
            #Cancel
            time.sleep(600) #Remind me again in 10 minutes


if not boxStatus: #assuming you only want to run this if 
    r = None
    mouse, keyboard = getStats()
    #If batteries are low:
    if mouse < limit or keyboard < limit:
        wait("Batteries Low: Mouse has %s%% charge.\nKeyboard has %s%% charge." % (str(mouse),str(keyboard)))
    time.sleep(20)


class BatteryChecker:
    def __init__(self, log='save.pkl', limit=35, message="Batteries Low: Mouse has %s%% charge.\nKeyboard has %s%% charge."):
        self.response = None
        self.limit = minimum
        self.message = message
        self.log = log
        if not os.path.exists(log):
            with open(log, 'x') as fob:
                pickle.save(True, fob)
    def dump(self):
        with open(self.log, 'wb') as fob:
            fob.write(pickle.dumps(self.alerted, pickle.HIGHEST_PROTOCOL))
    def load(self):
        with open(self.log, 'rb') as fob:
            pickle.load(self.alerted)
    @property # this enables you to invoke a method as if it were a constant attribute
    def mouse(self):
        return 30
    @property # this enables you to invoke a method as if it were a constant attribute
    def keybd(self):
        return 70
    def state(self):
        return self.mouse, self.keybd
    def is_critical(self):
        return any(i <= self.limit for i in (self.state()))
    def response(self):
        command = "osascript -e 'Tell application \"System Events\" to display dialog \" %s'"
        return os.system(command % (self.message % (self.mouse, self.keybd)))
    def main(self):
        if not self.alerted:
            if self.critical
        
    