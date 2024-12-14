def print_menu():
    print("="*38)
    print(f'{"Hair Salon Appointment Manager":^38}')
    print("="*38)
    print("1. Schedule an appointment\n"
          "2. Find appointment by name\n"
          "3. Print calendar for a specific day\n"
          "4. Cancel an appointment\n"
          "5. Change an appointment\n"
          "6. Calculate total fees for a day\n"
          "7. Calculate total weekly fees\n"
          "9. Exit the system")

def main():
    appointments = create_weekly_calendar()
    print("Starting the Appointment Manager System\nWeekly calendar created")

    load_choice = input("Would you like to load previously scheduled appointments from a file (Y/N)? ").lower()
    if load_choice == 'y':
        load_scheduled_appointments(appointments)
    
    print_menu()
    user_choice = int(input("Enter your selection: "))

    while user_choice != 10:

        if user_choice == 1:
            schedule_appt(appointments)

        elif user_choice == 2:
            print("** Find an appointment by name **")
            name = input("Enter client name: ")
            print(f"Appointments for {name}")
            calendar_header()
            print("\n")
            show_appointments_by_name(appointments, name)

        elif user_choice == 3:
            print("\n** Print calendar for a specific day **")
            day = input("Enter day of week: ").title()
            if day not in day_of_the_week:
                print(f"Appointments for {day}")
                calendar_header()
            show_appointments_by_day(appointments, day)
            print("\n")

        elif user_choice == 4:
            day = input("What day: ").title()
            start_hour = input("Enter start hour (24-hour clock): ")
            
            if not start_hour.isdigit():
                print("Invalid hour.")
            else:
                start_hour = int(start_hour)
            appointment = find_appointment_by_time(appointments, day, start_hour)
            if appointment and appointment.get_appt_type() != 0:
                cancelled_name = appointment.get_client_name()
                appointment.cancel()
                print(f"Appointment: {day} {start_hour}:00 - {start_hour + 1}:00 for {cancelled_name} has been cancelled!\n")
            else:
                print("That time slot isn't booked and doesn't need to be cancelled\n")

        elif user_choice == 5:
            print("\n")
            print("Change an appointment for:")
            change_appointment_by_day_time(appointments)

        elif user_choice == 6:
            print("Fees calculation per day....")
            calculate_fees_per_day(appointments)

        elif user_choice == 7:
            calculate_weekly_fees(appointments)
        
        elif user_choice == 8:
            print("\nInvalid option\n")

        elif user_choice == 9:
            print("** Exit the system **")
            save_choice = input("Would you like to save all scheduled appointments to a file (Y/N)? ").lower()
            if save_choice == 'y':
                save_scheduled_appointments(appointments)
            print("Good Bye!")
            break

        elif user_choice > 9:
                print("Invalid option\n")
                print_menu()
                user_choice = int(input("Enter your selection: "))

        print_menu()
        user_choice = int(input("Enter your selection: "))


if __name__ == "__main__":
    main()
