from lcd import *

def main():
    lcd_string("Hello", LCD_LINE_1, 2)
    lcd_string("ChanMin", LCD_LINE_2, 2)
    time.sleep(3)

if __name__ == '__main__':
    try:
    	# Initialise display
        lcd_init()
        whiteLCDon()
        main()
    except KeyboardInterrupt:
        pass
    finally:
        lcd_byte(0x01, LCD_CMD)
        lcd_string("Goodbye!",LCD_LINE_1,2)
        GPIO.cleanup()
