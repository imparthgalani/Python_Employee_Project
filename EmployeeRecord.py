import sqlite3
class Record:
 
      con = ""
      cur = ""
      
      def __init__(self):
            try:
                  self.con = sqlite3.connect("emp.db") 
            except:
                  pass
            self.cur = self.con.cursor()
 
            try:
                  self.cur.execute("create table employee(mid integer primary key autoincrement,id text,firstname text,lastname text,no text,department text,joinyear text,email text)")
                  self.con.commit()
            except:
                  pass
                 
      def add_record(self,eid,efname,elname,no,edepart,ejoinyear,eemail):
            self.cur.execute("insert into employee(id,firstname,lastname,no,department,joinyear,email) values(?,?,?,?,?,?,?)",(eid,efname,elname,no,edepart,ejoinyear,eemail))
            self.con.commit()
 
      def display_all(self):
            self.cur.execute("select * from employee")
            rec = self.cur.fetchall()
            for line in rec:
                  print(line)
 
      def get_employee_by_name(self,last):
            self.cur.execute("SELECT * FROM employee where lastname=?", (last,))
            rec = self.cur.fetchall()
            for line in rec:
                  print(line)
            
      def remove_by_id(self,id):
            self.cur.execute("DELETE from employee WHERE id=?", (id,))
            self.con.commit()
                  
      def update_by_id(self,eid,efname,elname,no,edepart,ejoinyear,eemail):
            self.cur.execute("update employee set firstname=?,lastname=?,no=?,department=?,joinyear=?,email = ? where id = ?",(efname,elname,no,edepart,ejoinyear,eemail,eid))   
            self.con.commit()
            