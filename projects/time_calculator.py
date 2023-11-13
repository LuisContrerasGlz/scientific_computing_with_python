"""

Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

"""

def add_time(start, duration, starting_day=""):
  pieces = start.split()
  time = pieces[0].split(":")
  end = pieces[1]

  if end == "PM":
      hour = int(time[0]) + 12
      time[0] = str(hour)

  dur_time = duration.split(":")
  new_hour = int(time[0]) + int(dur_time[0])
  new_minutes = int(time[1]) + int(dur_time[1])

  if new_minutes >= 60:
      hours_add = new_minutes // 60
      new_minutes -= hours_add * 60
      new_hour += hours_add

  days_add = 0
  if new_hour > 24:
      days_add = new_hour // 24
      new_hour -= days_add * 24

  if new_hour > 0 and new_hour < 12:
      end = "AM"
  elif new_hour == 12:
      end = "PM"
  elif new_hour > 12:
      end = "PM"
      new_hour -= 12
  else:
      end = "AM"
      new_hour += 12

  if days_add > 0:
      days_later = " (next day)" if days_add == 1 else " (" + str(days_add) + " days later)"
  else:
      days_later = ""

  week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

  if starting_day:
      weeks = days_add // 7
      i = week_days.index(starting_day.lower().capitalize()) + (days_add - 7 * weeks)
      if i > 6:
          i -= 7
      day = ", " + week_days[i]
  else:
      day = ""

  new_time = str(new_hour) + ":" + (str(new_minutes) if new_minutes > 9 else ("0" + str(new_minutes))) + " " + end + day + days_later

  return new_time
