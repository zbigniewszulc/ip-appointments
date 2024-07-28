from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date, datetime, timedelta
from .models import Appointment
import logging
logger = logging.getLogger('django')

def get_previous_Sunday_date (start_date):
    """
    Calculate date of the previous Sunday from given date.

    Adjusts the given date to the most recent previous Sunday. 
    If the given date is already a Sunday, it will return the same date.

    Args:
        start_date (datetime.date): Date from which to calculate previous Sunday

    Returns:
        datetime.date: The date of the previous Sunday.

    Notes:
        - `timedelta` to calculate the difference 
            between given date and the previous Sunday.
        - `start_date.weekday()` returns an integer representing 
            day of the week (Monday is 0 and Sunday is 6).
        - `(start_date.weekday() + 1) % 7` calculates the number of days 
            to subtract, to get to the previous Sunday.
    """
    previous_sunday = start_date = start_date - timedelta(
        days=(start_date.weekday() + 1) % 7
    )
    return previous_sunday  

def generate_week_calendar(start_date):
    """ 
    Returns list of dates representing a week starting from Sunday.

    Args:
        start_date (datetime.date): Starting date for the week. 
            Function will adjust this date to the previous Sunday.

    Returns:
        list of datetime.date: A list of 7 datetime.date objects representing 
            the week from Sunday to Satrday.
    """
    start_date = get_previous_Sunday_date(start_date)
    # List comprehension - to generate a list of dates representing a week
    week = [start_date + timedelta(days=i) for i in range(7)]
    return week

def get_time_slots(date):
    """ 
    Generate a list of hourly time slots for a given date.

    Args:
        date (datetime.date): The date for which to generate time slots. 

    Returns:
        list of str: A list of time slots in the format 'HH:MM' 
            from 10:00 to 17:00.

    Notes:
        - `strptime` string parse time 
        - `%H:%M` represents hours and minutes
        - `start_time` sample is an object (e.g. 2024-07-27 10:00:00)
        - `delta` object representing duration of 1 hour
        - `strftime` represents string format time (HH:MM)
    """
    start_time = datetime.strptime('10:00', '%H:%M')
    end_time = datetime.strptime('18:00', '%H:%M')
    delta = timedelta(hours=1)
    time_slots = []
    while start_time < end_time:
        time_slots.append(start_time.strftime('%H:%M'))
        start_time += delta
    return time_slots

def get_booked_slots(date):
    """ 
    Returns list of booked time slots for a given date.

    Args:
        date (datetime.date): The date for which to retrieve booked time slots.

    Returns:
        list of str: A list of booked time slots in the format 'HH:MM'.
    """
    # Fetch appointments for given date
    queryset = Appointment.objects.filter(date=date)
    booked_slots = queryset.values_list('time_slot', flat=True)
    logger.info(f"Booked slots: {booked_slots}")
    return booked_slots
    
def is_slot_booked(slot, booked_slots):
    """
    Check if the given time slot is booked.

    Args:
        slot (str): The time slot to check, in 'HH:MM' format.
        booked_slots (list of datetime.time): The list of booked time slots.

    Returns:
        bool: `True` if the slot is in booked_slots, otherwise `False`.
    """
    booked_slots_str = {
        booked_slot.strftime('%H:%M') for booked_slot in booked_slots
    }

    return slot in booked_slots_str

def get_week_calendar_with_slots(start_date):
    """ 
    Generate a weekly calendar with time slots and booking information.

    Args:
        start_date (datetime.date): The starting date of the week. 
           Week will be calculated starting from the nearest previous Sunday.

    Returns:
        list of dict: A list of dictionaries, each representing a day 
            in the week, including the following keys:
                - 'date' (datetime.date): The date for the day.
                - 'slots' (list of dict): Time slots for the day, 
                    where each dictionary contain:
                    - 'time' (str): The time slot in 'HH:MM' format.
                    - 'booked' (bool): Whether the time slot is booked.
                - 'is_weekend' (bool): `True` if the day is Saturday or Sunday, 
                    `False` otherwise.
    """
    week_days = generate_week_calendar(start_date)
    week_with_slots = []
    for day in week_days:
        date = day
        time_slots = get_time_slots(date)
        booked_slots = get_booked_slots(date)
        slots_with_booking_info = []
        # Create dictionary representing a time slot with its booking status
        for slot in time_slots:
            slot_info = {
                'time': slot,
                'booked': is_slot_booked(slot, booked_slots)
            }
            slots_with_booking_info.append(slot_info)
        # Encapsulate all relevant information
        day_info = {
            'date': date,
            'slots': slots_with_booking_info,
            # Check if the date is Sat (5) or Sun (6)
            'is_weekend': date.weekday() in [5, 6]
        }
        week_with_slots.append(day_info)
        
    return week_with_slots

def calendar_view(request, year=None, month=None, day=None):
    """ 
    Render a calendar view for provided week starting on Sunday.

    Calculates the start date of the week based on the provided 
    year, month, and day, or defaults to today's date. Then, it generates a 
    weekly calendar with time slots and booking information, and renders a 
    template with this data.

    Args:
        request (HttpRequest): The HTTP request object.
        year (int, optional): Year to display. Defaults to the current year 
            if not provided.
        month (int, optional): Month to display. Defaults to the 
            current month if not provided.
        day (int, optional): The day to display. Defaults to the current day if 
            not provided.

    Returns:
        HttpResponse: Rendered HTML page for the calendar view.

    Context:
        - week_data (list of dict): A list of dictionaries representing each day 
            in the week. Each dictionary contains:
            - 'date' (datetime.date): The date for the day.
            - 'slots' (list of dict): Time slots for the day, where 
                each dictionary contains:
                - 'time' (str): The time slot in 'HH:MM' format.
                - 'booked' (bool): Whether the time slot is booked.
            - 'is_weekend' (bool): `True` if the day is Saturday or Sunday, 
                `False` otherwise.
        - current_week (str): String representing the current week.
        - today (datetime.date): The current date.
        - next_year (int): The year for the next week.
        - next_month (int): The month for the next week.
        - next_day (int): The day for the next week.
        - prev_year (int): The year for the previous week.
        - prev_month (int): The month for the previous week.
        - prev_day (int): The day for the previous week.
        - show_current_week_button (bool): `True` if the button to show the 
        current week should be displayed.
    """
    # sample of what method today() of datetime class returns.. 
    # ..(e.g. (2024, 7, 27, 12, 0, 0))
    # method date() of the datetime object extracts the date part.. 
    # ..(e.g. (2024, 7, 27))
    today = datetime.today().date()

    # Validate input date, in case if user typed in URL manually
    if year and month and day:
        try:
            start_date = datetime(year, month, day).date()
        except ValueError:
            messages.error(
                request, 
                "Invalid date provided. Redirecting to current week.."
            )
            return redirect('calendar_view')
    else:
        start_date = today

    # Make sure the calendar view starts on (previous) Sunday, ..
    # .. Sat/Sun are closing days, calendar looks better if on oposite poles
    start_date = get_previous_Sunday_date(start_date)

    # List of dictionaries, where each dictionary represents a day in the week..
    # ..inluding date, timelots with booking status and if it is weekend
    week_data = get_week_calendar_with_slots(start_date)

    # Determine the date for begining of the next week (for Next button)
    next_week_start = start_date + timedelta(days=7)
    # Determine the date for begining of the previous week (for Previous button)
    prev_week_start = start_date - timedelta(days=7)

    # Check if the current date (today) falls within the week.. 
    # ..starting from start_date
    is_current_week = (start_date <= today <= start_date + timedelta(days=6))

    context = {
        'week_data': week_data,
        'current_week': f"Week of {start_date.strftime('%B %d, %Y')}",
        'today': today,
        'next_year': next_week_start.year,
        'next_month': next_week_start.month,
        'next_day': next_week_start.day,
        'prev_year': prev_week_start.year,
        'prev_month': prev_week_start.month,
        'prev_day': prev_week_start.day,
        'show_current_week_button': not is_current_week,  
    }

    return render(request, 'appointment/calendar.html', context)
