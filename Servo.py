from machine import Pin, PWM
import utime

class Servo:
    def __init__(self, pin, pwm_freq = 50, min_duty = 1700, max_duty = 7700, time180_ms = 360):
        self.MIN_DUTY = min_duty
        self.MAX_DUTY = max_duty
        self.TIME_180 = int(time180_ms)
        self.DEG_DUTY = (self.MAX_DUTY - self.MIN_DUTY) / 180
        self.DEG_TIME = self.TIME_180 / 180
        self.NOW_DEG = 90
        self.servoPWM = PWM(Pin(pin))
        self.servoPWM.freq(pwm_freq)
        
        # Full Sweep
        self.Min()
        self.Sleep(self.TIME_180 * 1.0)
        self.Max()
        self.Sleep(self.TIME_180 * 0.5)
        self.Min()
        self.Sleep(self.TIME_180 * 0.5)
    
    def Min(self):
        self.GoToDegree(0)
    
    def Max(self):
        self.GoToDegree(180)
    
    def GoToDegree(self, degree, time_ms = 0):
        if(self.NOW_DEG == degree): return
        if(degree < 0): return
        if(degree > 180): return
        if(time_ms < 0):
            time_ms = 0
        
        degree = int(degree)
        
        if (time_ms == 0):
            deg_distance = abs(degree - self.NOW_DEG)
            duty = int((degree * self.DEG_DUTY) + self.MIN_DUTY)
            self.servoPWM.duty_u16(duty)
            self.NOW_DEG = degree
            self.Sleep(deg_distance * self.DEG_TIME)
        else:
            direction = 1
            if(self.NOW_DEG > degree):
                direction = -1
            deg_distance = abs(degree - self.NOW_DEG)
            req_time = (deg_distance * self.DEG_TIME)
            if(req_time > time_ms):
                time_ms = req_time
            deg_time = (time_ms / deg_distance)
            for _ in range(deg_distance):
                destination = self.NOW_DEG + direction
                duty = int((destination * self.DEG_DUTY) + self.MIN_DUTY)
                self.NOW_DEG = destination
                self.servoPWM.duty_u16(duty)
                self.Sleep(deg_time)
            
    
    def Sleep(self, time_ms):
        utime.sleep_ms(int(time_ms))