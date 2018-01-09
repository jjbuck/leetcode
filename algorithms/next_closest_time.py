class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        
        hour = time[0:2]
        minute = time[3:5]
        digits = ''.join(time.split(":"))
        digits = [c for c in digits]
        if len(set(digits)) <= 1:
            return time
        options = [a + b + ":" + c + d for a in digits for b in digits for c in digits for d in digits]
        # check for valid options
        options = [check for check in options if self.isValidTime(check)]
        options = [check for check in options if check != time]
        closest_time = options[0]
        closest_diff = self.timeDifference(time,closest_time)
        if closest_diff < 0: # this occurs if the next time is before the current time, i.e., the next day
                closest_diff += (24*60)
        for i in range(1, len(options)):
            diff = self.timeDifference(time,options[i])
            if diff < 0: # this occurs if the next time is before the current time, i.e., the next day
                diff += (24*60)
            if  diff < abs(closest_diff):
                closest_diff = diff
                closest_time = options[i]
        return closest_time
            
        
    def isValidTime(self,time):
        '''
        Checks to see if the input time is a valid time value
        '''
        hour = int(time[0:2])
        minute = int(time[3:5])
        if 0 <= hour < 24 and 0 <= minute < 60:
            return True
        else:
            return False
        
    def timeDifference(self,time1,time2):
        '''
        Calculates the elapsed time from time1 to time2
        '''
        hour1 = int(time1[0:2])
        hour2 = int(time2[0:2])
        minute1 = int(time1[3:5])
        minute2 = int(time2[3:5])
        diff = 60 * (hour2 - hour1) + (minute2 - minute1)
        return diff
        
            
        
        

assert Solution().nextClosestTime("19:34") == "19:39"
assert Solution().nextClosestTime("23:59") == "22:22"
Solution().nextClosestTime("00:00")