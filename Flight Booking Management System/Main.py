import random
import flights as fy
import difplane as pl

#The following are the lists representing different flights
#each flight with two different classes with 20 seats each

flight1=[20,20]
flight2=[20,20]
flight3=[20,20]
flight4=[20,20]
flight5=[20,20]

#flightlist is a list of above flight lists.

flightlist=[flight1,flight2,flight3,flight4,flight5]

#tic_list is a list of ticket numbers
tic_list=[]

#passen is a dictionary with key value pairs as ticketnumber and passenger class objects 
passen={}

#displays the type and availability of seats of a particular flight.

def display(a):
    print(" 1. Business Class ")
    print("    Available Seats:",flightlist[a][0])
    print("\n")
    print(" 2. Economic Class ")
    print("    Available seats:",flightlist[a][1])
    print("\n")
    seat_type=int(input("Enter Type of seat you want: "))
    if(seat_type==1):
        if(flightlist[a][0]!=0):
            seat_number=flightlist[a][0]
            flightlist[a][0]=flightlist[a][0]-1
            return seat_number
        else:
            alter()
            available_flights()
    else:
        if(flightlist[a][1]!=0):
            seat_number=flightlist[a][1]
            flightlist[a][1]=flightlist[a][1]-1
            return seat_number
        else:
            alter()
            available_flights()

            
class passenger:
    
    def info(self):
        Name=input(" Please Enter Your Name: ")
        self.name=Name
        passport_number=str(input(" Please Enter Your Passport Number: "))
        self.pass_number=passport_number
        gender=input(" Enter Your Gender(M/F/OTHER): ")
        self.sex=gender
        Age=int(input(" Enter Your Age: "))
        self.age=Age
        phone_number=int(input(" Enter Your Cell Number: "))
        self.cell_number=phone_number
        
    def print_details(self):
        print("\n********* PASSENGER DETAILS **************")
        print("Passenger Name = ",self.name)
        print("Passport Number = ",self.pass_number)
        print("Cell Number = ",self.cell_number)
        print("Age = ",self.age)


def reserve_seat():
    print("\n                             SEAT RESERVATION                                        ")
    seat_no=available_flights()
    ticket=random.randrange(100000,900000)
    passen[ticket]=passenger()
    passen[ticket].info()
    passen[ticket].print_details()
    print("Seat Number = ",seat_no)
    print("Ticket Number = ",ticket)
    print("\n****Ticket Booked Successfully***")
    tic_list.append(ticket)
    con=input("\nDo You Want To reserve seat Again(Y/N)? ")
    if(con=='Y' or con=='y'):
        reserve_seat()
def alter():
    print("\n")
    print("All seats are reserved in this class ")
def cancelled():
    print("\n")
    print("****Cancelled Successfully****")

def available_flights():
    fy.plane()
    s=int(input(" \nEnter the Serial number of flight in which you want to travel : "))
    print("\n")
    if(s==1):
          pl.f1()
          r=display(s-1)
    elif(s==2):
          pl.f2()
          r=display(s-1)
    elif(s==3):
          pl.f3()
          r=display(s-1)
    elif(s==4):
          pl.f4()
          r=display(s-1)
    elif(s==5):
          pl.f4()
          r=display(s-1)
    else:
        print("Enter correct option")
    return r
def Flights_Available():
    fy.plane()  
def cancel_seat():
    check_ticket=int(input("\nEnter your Ticket number: "))
    if check_ticket in tic_list:
        passen[check_ticket].print_details()
        flight_number=int(input("Enter Your Flight Number: "))
        clas_s=int(input("1. Business Class \n2. Economic Class\n"))
        if(flight_number==1):
            if clas_s==1:
                flightlist[0][0]+=1
                cancelled()
            elif clas_s==2:
                flightlist[0][1]+=1
                cancelled()
            else:
                print("Enter correct option")
        elif(flight_number==2):
            if clas_s==1:
                flightlist[1][0]+=1
                cancelled()
            elif clas_s==2:
                flightlist[1][1]+=1
                cancelled()
            else:
                print("Enter correct option")
        elif(flight_number==3):
            if clas_s==1:
                flightlist[2][0]+=1
                cancelled()
            elif clas_s==2:
                flightlist[2][1]+=1
                cancelled()
            else:
                print("Enter correct option")
        elif(flight_number==4):
            if clas_s==1:
                flightlist[3][0]+=1
                cancelled()
            elif clas_s==2:
                flightlist[3][1]+=1
                cancelled()
            else:
                print("Enter correct option")
        elif(flight_number==5):
            if clas_s==1:
                flightlist[4][0]+=1
                cancelled()
            elif clas_s==2:
                flightlist[4][1]+=1
                cancelled()
            else:
                print("Enter correct option")
        else:
            print("Enter correct option")   
    else:
        print("Invalid ticket number ")
        
#displayed when the user inputs 4 to exit the program
        
def quit_program():
    print("\n")
    print("                                                             Thank You")
    print("                                              Good Bye from Flight Ticket Management System")

print("\n\n")
#displayed when the program starts
print("                                                  WELCOME TO FLIGHT TICKET MANAGEMENT SYSTEM                 ")

req=True

while(req):
#driver menu displayed everytime the user wish to proceed with an operation
    print("\n")
    print("WHAT WOULD YOU LIKE TO DO? ")
    print(" 1) Reserve Seats ")
    print(" 2) Flights Available" )
    print(" 3) Cancel Seat ")
    print(" 4) Quit Program ")
    ch=int(input("Enter Your Choice: "))
    if(ch==1):
#calling the function reserve_seat()
        reserve_seat()
    elif(ch==2):
#calling the function Flights_Available()
        Flights_Available()
    elif(ch==3):
#calling the function cancel_seat()
        cancel_seat()
    elif(ch==4):
        req=False
        quit_program()





