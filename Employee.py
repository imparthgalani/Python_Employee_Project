import EmployeeVerification as sv                      
from EmployeeRecord import Record 
 
class Employee:

      _employeeid=""
      _employeeFirstName=""
      _employeeLastName=""
      _employee_No=""
      _employee_depart=""
      _employee_join_year=""
      _employeeEmail=""
 
      def __init__(self):
            e = sv.Verification()
            self._employeeid = e.verifyid()
            self._employeeFirstName = input("enter first name: ")
            self._employeeLastName = input("enter last name: ")
            self._employee_No = e.verifynumber()
            self._employee_depart = input("enter department: ")
            self._employee_join_year = int(input("enter year of joining: "))
            self._employeeEmail=e.verifyemail();      
            
      @staticmethod
      def is_holiday():
            with open("schedule.txt","a+") as f:
                  day = input("enter the day: ")
                  if day == 'saturday' or day == 'sunday':
                        note = 'It is holiday'
                  else:
                        note = 'It is Working day'
                  f.write(note) 
            print("Schedule Added=> "+ note)
                
while(1):
                      
    print("1. Add Employee")
    print("2. Display records of all the Employees")
    print("3. Add schedule")
    print("4. Get Employee by last name")
    print("5. Update Employee information..")
    print("6. Remove Employee by id")

    
    choice = int(input("Enter your Choice: "))
    if choice == 1:
        e = Employee()
        rec = Record()
        rec.add_record(e._employeeid,e._employeeFirstName,e._employeeLastName,e._employee_No,e._employee_depart,e._employee_join_year,e._employeeEmail)
        print("Employee record added")
    
    elif choice==2:
        rec = Record()
        rec.display_all()
    
    elif choice==3:
        Employee.is_holiday()
        
    elif choice==4:
        rec = Record()
        last = input("enter last name: ")
        rec.get_employee_by_name(last)
        
    elif choice==5:
        e =  Employee()
        rec = Record()
        rec.update_by_id(e._employeeid,e._employeeFirstName,e._employeeLastName,e._employee_No,e._employee_depart,e._employee_join_year,e._employeeEmail)
        print("Employee record Updated")
        
    elif choice==6:
        ID = input("Enter the ID of employee: ")
        rec = Record()
        rec.remove_by_id(ID)
        print("Employee record removed")    
          
    else:
        print("invalid choice")
        break