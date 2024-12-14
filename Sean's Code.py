#imports the os to check if a file exists or not
import os
#imports the Appointment class from appointment file
from appointment import Appointment
#reference list of the days of the week
day_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#creates an empty weekly calander list. Iterates each day in day_of_the_week list. Loops the hours between 9-4pm to create a (day,hour)
#(day, hour) gets appended to the calender list
def create_weekly_calendar():
    calendar = []
    for day in day_of_the_week:
        for hour in range(9, 17):  # Appointments from 9 AM to 4 PM (last slot ends at 5 PM)
            calendar.append(Appointment(day, hour))
    return calendar

#loads appointments from an inputted file and checks if the file exists or not
#if file exists it will read and print the contents(clientname, phone#, ext)
#returns the number of appointments on the file 
def load_scheduled_appointments(appointments):
    filename = input("Enter the filename to load appointments from: ")

    if not os.path.exists(filename):
        filename = input("File not found. Re-enter appointment name: ")

    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
                client_name, client_phone, appt_type, day, start_time_hour = line.strip().split(',')
                appointment = find_appointment_by_time(appointments, day, int(start_time_hour))
                if appointment:
                    appointment.schedule(client_name, client_phone, int(appt_type))
    print(f"{len(lines)} previously scheduled appointments have been loaded")
    return len(lines)

#searches for appointments that match a given day and start hour by looping through the file contents
#if a match is found, it returns the appointment object, or returns none
def find_appointment_by_time(appointments, day, start_hour):
    for appointment in appointments:
        if appointment.get_day_of_week() == day and appointment.get_start_time_hour() == start_hour:
            return appointment
    return

#searches and prints all appointments for a client by name
#loops through appointments to see if client_name contains the name
#prints appointment if found, otherwise "No appointments found"
def show_appointments_by_name(appointments, name):
    matches_by_name = []
    for appt in appointments:
        if name.lower() in appt.get_client_name().lower():
            matches_by_name.append(appt)
    
    if matches_by_name:
        for appt in matches_by_name:
            print(appt)

    else:
        print(f"\nNo appointments found.\n")

#searches and prints all appointments for a specific day
#loops through appointments to see if there is a matching day
#prints the matching appointment if found
def show_appointments_by_day(appointments, day):
    matches_by_day = []
    for appt in appointments:
        if appt.get_day_of_week() == day:
            matches_by_day.append(appt)
    
    if matches_by_day:
        for appt in matches_by_day:
            print(appt)

#allows to changes to exisiting appointment timeslots
#finds the appointment to be changed using find_appointment_by_time function
#if the appointment is found, it asks for the user to input a new day and time.
#checks if the new time slot is available. if available, reschedules to the new time. If not avail, says the slot is already booked
def change_appointment_by_day_time(appointments):

    day = input("Whatday: ").title()
    start_hour = int(input("Enter start hour (24 hour clock): "))
    appointment = find_appointment_by_time(appointments, day, start_hour)

    if not appointment:
        print("No appointment found at the given time.")
        return

    new_day = input("Enter a new day: ").title()
    new_start_hour = int(input("Enter start hour (24 hour clock): "))
    new_appointment = find_appointment_by_time(appointments, new_day, new_start_hour)

    if new_appointment and new_appointment.get_appt_type() == 0:
        new_appointment.schedule(appointment.get_client_name(), appointment.get_client_phone(), appointment.get_appt_type())
        appointment.cancel()
        print(f"Appointment rescheduled {appointment.get_client_name()} has been changed to \nDay = {new_day}\nTime = {new_start_hour}:00")
    else:
        print("The new time slot is already booked\n")
