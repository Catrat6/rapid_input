import random
import pandas as pd

class TripModel:

    def __init__(self, pas_fn, pas_ln, pas_num, pas_add, pas_pu, pas_do, pas_app):
        self.tripID = self.unique_id()
        self.firstName = pas_fn
        self.lastName = pas_ln
        self.phoneNumber = pas_num
        self.address = pas_add
        self.pickUp = pas_pu
        self.dropOff = pas_do
        self.appointment = pas_app

    def unique_id(self):
        while True:
            new_trip_id = random.randint(1000, 9999)
            x = pd.read_csv('trip_id_check.csv')
            x_list = x['Trip ID'].to_list()
            if new_trip_id not in x_list:
                x.loc[len(x), 'Trip ID'] = new_trip_id
                x.to_csv('trip_id_check.csv', index=False)
                return new_trip_id


    def return_trip_info(self):
        print(f"{self.tripID}, {self.firstName}, {self.lastName}, {self.phoneNumber}, {self.address}, {self.pickUp}, "
              f"{self.dropOff}, {self.appointment}\n")

    def write_trip_to_csv(self):
        a = pd.read_csv('trip_id.csv')
        row = len(a)
        a.loc[row, 'Trip ID'] = self.tripID
        a.loc[row, 'First Name'] = self.firstName
        a.loc[row, 'Last Name'] = self.lastName
        a.loc[row, 'Phone Number'] = self.phoneNumber
        a.loc[row, 'Address'] = self.address
        a.loc[row, 'Pick Up'] = self.pickUp
        a.loc[row, 'Drop Off'] = self.dropOff
        a.loc[row, 'Appointment'] = self.appointment

        a.to_csv('trip_id.csv', index=False)







