from trip_model import TripModel

trip_list = []

state = True

while state:

    input('Press ENTER to write new trip:\n')

    while True:
        a = str(input('Passengers First Name:\n'))
        b = str(input('Passengers Last Name:\n'))
        c = str(input('Passengers Phone Number (no spaces or "-":\n'))
        d = str(input('Passengers Address:\n'))
        e = str(input('Passengers Pick Up:\n'))
        f = str(input('Passengers Drop Off:\n'))
        g = str(input('Passengers Appointment Time:\n'))

        new_trip = TripModel(a, b, c, d, e, f, g)

        new_trip.return_trip_info()

        print('Your trip has been created!')

        trip_list.append(new_trip)

        break

    another = input('''
    Would you like to create another trip?
    Yes: Keep entering trips
    Write: Write all trips to CSV
    No: Discard all created trips
    ''').lower()

    if another == 'yes':
        continue
    elif another == 'write':
        [each.write_trip_to_csv() for each in trip_list]
        more = input('Your trips have been saved to CSV, would you like to write more (yes/no').lower()
        if more == 'yes':
            continue
        elif more == 'no':
            break
    elif another == 'no':
        trip_list.clear()
        input('Your trips have been discarded, press ENTER to exit')
        break







