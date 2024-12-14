# This is a function that will set an appointment
def schedule_appt(appointments):
    print("** Schedule an appointment **")
    day = input("What day: ").title()


    start_hour = input("Enter start hour (24-hour clock): ")
    # This will return back into the menu when the user accidentally enters a letter instead of a number
    if not start_hour.isdigit():
        print("Invalid hour.")
        return

    start_hour = int(start_hour)
    
    # Ensure time is within the working hours (9 to 17)
    if start_hour < 9 or start_hour >= 17:
        print("Sorry that time slot is not in the weekly calendar!\n")
        return
    # This is to set the clients name, the day they want and the time they want the appointment
    appointment = find_appointment_by_time(appointments, day, start_hour)
    if appointment:
        # This is to get the appoinment type from the appointment calss
        if appointment and appointment.get_appt_type() == 0:
            client_name = input("Client Name: ")
            client_phone = input("Client Phone: ")
            print("Appointment types:\n1: Mens Cut $40, 2: Ladies Cut $60, 3: Mens Colouring $40, 4: Ladies Colouring $80")
            
            # This is to ensure the input is a number instead of a letter or a character
            appt_type = input("Type of Appointment: ")
            if not appt_type.isdigit():
                print("Invalid type.")
                return

            # This is tp create a schedule for the client using the schedule setter from appointment class then displays it is scheduled
            # This will also display if the time slot is  taken or is not available
            appt_type = int(appt_type)
            if appt_type in Appointment.appt_type_dict:
                appointment.schedule(client_name, client_phone, appt_type)
                print(f"OK, {client_name}'s appointment is scheduled!\n")
            else:
                print("Invalid appointment type.")
        else: print("Sorry that time slot is booked already!\n")
    else:
        print("Sorry that time slot is not in the weekly calendar!\n")

    # This is called when entering 9 or exiting the system
    # This saves the current configuration to a file 
    # This will receive a list of appointments
def save_scheduled_appointments(appointments):
    filename = input("Enter appointment filename: ")
    # Inputs appointment filename from user, checks if the file already exists and if so,
    #  allows user to proceed and repeat the filename input
    if os.path.exists(filename):
        overwrite = input("File already exists. Do you want to overwrite it (Y/N)? ").lower()
        if overwrite != 'y':
            filename = input("Enter appointment filename: ")
    
    # writes the appointment to the file in the proper CSV format
    with open(filename, 'w') as file:
        # Iterates over each appointment in the list
        for appt in appointments:
            if appt.get_appt_type() != 0:
                file.write(appt.format_record() + '\n')
    print(f"3 scheduled appointments have been successfully saved")

# This calculates the  fees for the day th user wants to open
def calculate_fees_per_day(appointments):
    # The user inputs the day they want
    day = input("Enter the day to calculate fees: ").title()
    # This will check if the day inputed is within the days of the week the store is open.
    if day not in day_of_the_week:
        print(f"{day} is invalid or the salon is closed\n")
        return
    # This is to initialize the fees to be calculated
    total_fees = 0
    # This adds all the fees aassociated to the day entered and print the total fees
    for appt in appointments:
        if appt.get_day_of_week() == day and appt.get_appt_type() != 0:
            total_fees += Appointment.appt_fee_dict[appt.get_appt_type()]
    
    print(f"Total fees for {day}: ${total_fees}\n")

# This calculates the weekly fees for the whole week
def calculate_weekly_fees(appointments):
    total_fees = 0
    # This adds all the fees aassociated to the day entered and print the total fees
    for appt in appointments:
        if appt.get_appt_type() != 0:
            total_fees += Appointment.appt_fee_dict[appt.get_appt_type()]
    
    print(f"Total weekly fees: ${total_fees}\n")


