class PassengerRegistration:
    def __init__(self):
        self.passengerName = None
        self.passengerCount = 0
        self.departure = None
        self.destination = None
        self.dateOfDeparture = None
        self.seatNo = None
        self.busType = None
        self.busFare = 0
    def startRegistration(self):
        self.passengerName = input("Enter the name of passenger : ")
        self.passengerCount = int(input("Enter the passenger count : "))
        while (self.departure == None):
            print("""
                1: Coimbatore
                2: Tirupur
                3: Erode
                4: Salem
            """)
            departure = int(input("Choose the departure Location: "))
            if (departure == 1):
                self.departure = "Coimbatore"
            elif (departure == 2):
                self.departure = "Tirupur"
            elif (departure == 3):
                self.departure = "Erode"
            elif (departure == 4):
                self.departure = "Salem"
            else:
                pass
        while (self.destination == None):
            print("""
                1: Cochin
                2: Palakkad
                3: Trivandrum
                4: Idukki
            """)
            destination = int(input("Choose the destination Location: "))
            if (departure == 1):
                self.destination = "Cochin"
            elif (destination == 2):
                self.destination = "Palakkad"
            elif (destination == 3):
                self.destination = "Trivandrum"
            elif (destination == 4):
                self.destination = "Idukki"
            else:
                pass
        self.dateOfDeparture = input(
            "Enter the date of departure (Format : 30-04-2004) : ")
        print("""
            [1] [2]  [3] [4] [5]
            [6] [7]  [8] [9] [10]
            [11][12] [13][14][15]
            [16][17] [18][19][20]
        """)
        self.seatNo = int(input("Choose the seat number : "))
        while (self.busType == None):
            print("""
                1. AC BUS : 500 Fare
                2. NON AC BUS : 300 Fare   
            """)
            busType = int(input("Choose the bus type : "))
            if (busType == 1):
                self.busType = "AC BUS"
                self.busFare = 500
            elif (busType == 2):
                self.busType = "NON AC BUS"
                self.busFare = 300
            else:
                pass
        print("""
                You have Successfully Registered for the bus !!!
                Happy Journey ⭐⭐⭐⭐⭐⭐⭐⭐⭐

                Your Bus ticket
                ----------------------------------------------------------------
                                    Legendmp Travels
                ----------------------------------------------------------------

                passenger name : {name}
                Date of Booking : {dateOfDeparture}

                ----------------------------------------------------------------
                            {departure} ---------> {destination}
                
                Bus Type : {busType}                    seat no : {seatNo}
                Bus Fare : {busFare}

                ________________________________________________________________
                                    ~Happy Journey ✅~
        """.format(name=self.passengerName, count=self.passengerCount,
                   departure=self.departure,
                   destination=self.destination,
                   dateOfDeparture=self.dateOfDeparture,
                   seatNo=self.seatNo,
                   busType=self.busType,
                   busFare=self.busFare))


passenger1 = PassengerRegistration()
passenger1.startRegistration()