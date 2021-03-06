import sys
from lcd import *
from tablebar_time import *
from tablebar_calender import *
from tablebar_weather import *
from tablebar_globals_modules import *
from tablebar_baseball import *
from tablebar_LCDlogging import *
#from gluon import current


def main():
    # Display wlan ip address
    lcd_string("Wlan IP Addr", LCD_LINE_1, 2)
    lcd_string(wip_chk()[:-1], LCD_LINE_2, 2)
    LCDlog2file("Wlan IP Addr", wip_chk()[:-1])
    time.sleep(3)
	
    # Display time information
    cycle = 10
    while getTask() == "0":
    	if cycle == 0:
    	    setTask("1")
    	    break
    	if getLock() == "False":
    	    setLock("True")
    	    # Display date & time
    	    lcd_string(getData(), LCD_LINE_1, 2)
    	    lcd_string(getTime(), LCD_LINE_2, 2)
    	    if cycle == 10:
    	    	LCDlog2file(getData(), getTime())
    	    cycle = cycle - 1
    	    time.sleep(1)
    	    setLock("False")
    
    # Display date information
    while getTask() == "1":
        # Display calender
        plines = getWeek()
        cycle = 5
        if getLock() == "False":
            setLock("True")
            while cycle > 0:
                time.sleep(1)
                lcd_string(plines[0], LCD_LINE_1, 1)
                lcd_string(plines[1], LCD_LINE_2, 1)
                if cycle == 5:
                	LCDlog2file(plines[0], plines[1])
                plines[0] = plines[0][:4]+plines[0][8:]
                plines[1] = plines[1][:4]+plines[1][8:]
                cycle = cycle - 1
                time.sleep(1)
            setLock("False")
        if cycle == 0:
            setTask("0")
            break
    """
    # Display Baseball information
    while getTask() == "2":
    	plines = getBaseballinfo()
    	cycle = 5
    	if getLock() == "False":
    	    setLock("True")
    	    while cycle > 0:
    	    	lcd_string(plines[0], LCD_LINE_1, 2)
    	    	lcd_string(plines[1], LCD_LINE_2, 2)
    	    	if cycle == 5:
    	    		LCDlog2file(plines[0], plines[1])
    	    	cycle = cycle - 1
    	    	time.sleep(1)
    	    setLock("False")
    	if cycle == 0:
    	    setTask("0")
    	    break
    """
    """
    while getTask() == "3":
    	cycle = 5
    	if getLock() == "False":
    	    setLock("True")
    	    while cycle > 0:
    	    	data = {}
    	    	data = getWeather()
    	    	lcd_string("Now : "+data['now_temp']+"'C, "+data['now_weather'], LCD_LINE_1, 2)
    	    	lcd_string("1h : "+data['one_later']+", 2h : "+data['two_later'], LCD_LINE_2, 2)
    	    	cycle = cycle - 1
    	    	time.sleep(5)
    	    setLock("False")
    	if cycle == 0:
    	    setTask("0")
    	    break
    """
    
def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

def wip_chk():
    cmd = "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1"
    wipAddr = run_cmd(cmd)
    return wipAddr

if __name__ == '__main__':
    try:
    	# Initialise display
        lcd_init()
        whiteLCDon()
        init_variables()
        while True:
            main()
    except KeyboardInterrupt:
        pass
    finally:
        lcd_byte(0x01, LCD_CMD)
        lcd_string("Goodbye!",LCD_LINE_1,2)
	#lcd_string("%d"%(session.which_task),LCD_LINE_2,2)
        GPIO.cleanup()
