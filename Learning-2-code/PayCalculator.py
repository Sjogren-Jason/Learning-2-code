i = False
while True:
    hours_week_1 = input("How many hours did you work during the first week of the pay period? ")
    hours_week_2 = input("How many hours did you work during the second week of the pay period? ")
    pay = 17
    tax = 0.3
    overtime_pay = int(pay) * 1.5

    if hours_week_1 > str(40):
        overtime_hours_week_1 = int(hours_week_1) - 40
        regular_hours_week_1 = 40
    else:
        overtime_hours_week_1 = 0
        regular_hours_week_1 = hours_week_1

    if hours_week_2 > str(40):
        overtime_hours_week_2 = int(hours_week_2) - 40
        regular_hours_week_2 = 40
    else:
        overtime_hours_week_2 = 0
        regular_hours_week_2 = hours_week_2

    total_regular_hours = int(regular_hours_week_1) + int(regular_hours_week_2)
    total_overtime_hours = int(overtime_hours_week_1) + int(overtime_hours_week_2)

    overtime = overtime_pay * int(total_overtime_hours)
    regular_pay = int(total_regular_hours) * int(pay)

    gross_pay = int(regular_pay) + int(overtime)
    taxable_pay = int(gross_pay) * tax
    net_pay = int(gross_pay) - int(taxable_pay)

    print("Gross Pay $" + str(gross_pay))
    print("Net Pay $" + str(net_pay))
    print("Total Regular Hours " + str(total_regular_hours))
    print("Total OT Hours " + str(total_overtime_hours))

    again = input("Again? ")

    if again == "yes":
        i = False
    else:
        print("That is too bad, have a nice day!")
        break
print("See you again soon")