# Problem
# =====================================================================================================================
# Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.


# Solution
# =====================================================================================================================
def clock_angle(time):
    """
    clock_angle: Finds the angle between the two clock hands
    :param time: (string) The time in hh:mm format
    :return: (int) Angle between the hour and minute hand to the nearest degree
    """
    hour, minute = time.split(":")
    # The extra degrees the hour hand moves due to what minute it is in the hour
    minute_offset = (int(minute) / 60) * 30
    hour_angle = ((360/12) * int(hour)) + minute_offset
    minute_angle = (360/60) * int(minute)
    return round(abs(hour_angle - minute_angle))


# Input
# =====================================================================================================================
print(clock_angle('01:30'))
print(clock_angle('08:30'))
