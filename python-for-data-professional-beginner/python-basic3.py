class Employee:
    company = 'ABC'

aksara = Employee()
aksara.company = 'DEF'
senja = Employee()

print("aksara.company:",aksara.company)
print("aksara.__class__.company:",aksara.__class__.company)
print("senja.company:",senja.company)
print("senja.__class__.company:",senja.__class__.company)

print('#######################################################')

class Employee2:
    company = 'ABC'

aksara = Employee2()
senja = Employee2()

print("aksara.__class__.company:",aksara.__class__.company)
aksara.__class__.company = 'DEF'
print("aksara.company:",aksara.company)
print("aksara.__class__.company:",aksara.__class__.company)
print("senja.company:",senja.company)
print("senja.__class__.company:",senja.__class__.company)

print('#######################################################')

class Employee3:
    company = 'ABC'
    def __init__(self, name, age, salary):
         self.name = name
         self.age = age
         self.salary = salary

aksara = Employee3('Aksara', 25, 8500000)
senja = Employee3('Senja', 28, 12500000)
print(aksara.name + ', Age: ' + str(aksara.age) + ', Salary: ' + str(aksara.salary))
print(senja.name + ', Age: ' + str(senja.age) + ', Salary: ' + str(senja.salary))

print('#######################################################')

class Employee4:
    def __init__(self, name, age, salary, overtime_pay):
        self.name = name
        self.age = age
        self.salary = salary
        self.overtime_pay = overtime_pay
        self.bonus = 0
    
    def overtime(self):
        self.bonus += self.overtime_pay

    def project_bonus(self, pj_bonus):
        self.bonus += pj_bonus
    
    def total_salary(self):
        return self.salary + self.bonus

class Company:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.employee_list = []
    
    def activate(self, employee):
        self.employee_list.append(employee)
    
    def deactivate(self, employee_name):
        deactivate_employee = None
        for emp in self.employee_list:
            if emp.name == employee_name:
                deactivate_employee = emp
                break
        
        if deactivate_employee is not None:
            self.employee_list.remove(deactivate_employee)

company = Company('ABC', 'Jl. Jendral Sudirman, Blok 11', '(021) 95205XX')

employee_1 = Employee4('Ani', 25, 8500000, 100000)
employee_2 = Employee4('Budi', 28, 12000000, 150000)
employee_3 = Employee4('Cici', 30, 15000000, 200000)

company.activate(employee_1)
company.activate(employee_2)
company.activate(employee_3)
company.deactivate("Cici")

employee_1.overtime()
employee_2.overtime()
employee_3.overtime()

print("Employee List:")
for data in company.employee_list:
    print(data.name+', Age: '+str(data.age)+', Salary: '+str(data.salary)+', Overtime pay: '+str(data.overtime_pay)+', Total salary: '+str(data.total_salary()))

print('#######################################################')
print('ENCAPSULATION')

class Employee5:
    company = 'ABC'
    __overtime_pay = 250000

    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = 0
    
    def overtime(self):
        self.__bonus += self.__overtime_pay

    def project_bonus(self, pj_bonus):
        self.__bonus += pj_bonus
    
    def total_salary(self):
        return self.__salary + self.__bonus

aksara = Employee5('Aksara', 25, 8500000)
print("This object work at: " + aksara.__class__.company)
#print("This object's name is: " + aksara.__name)

print('#######################################################')
print('INHERITANCE')

class Employee6: 
    company = 'ABC' 
    overtime_pay = 250000
    def __init__(self, name, age, salary): 
        self.name = name
        self.age = age 
        self.salary = salary 
        self.bonus = 0
    
    def overtime(self):
        self.bonus += self.overtime_pay 
    
    def project_bonus(self, pr_bonus):
        self.bonus += pr_bonus 
    
    def total_salary(self):
        return self.salary + self.bonus

class DataAnalyst(Employee6):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

class DataScientist(Employee6):
    overtime_pay = 500000
    def __init__(self, name, age, salary): 
        super().__init__(name, age, salary)

aksara = DataAnalyst('Aksara', 25, 8500000)
aksara.overtime()
print("Total salary " + aksara.name + ": " + str(aksara.total_salary()))

senja = DataScientist('Senja', 28, 13000000)
senja.overtime()
print("Total salary " + senja.name + ": " + str(senja.total_salary()))

# using pass
class Mamalia:
    def interaksi(self):
        print('Bersuara')

class Anjing(Mamalia):
    def interaksi(self):
        print('Guk')

class Manusia(Mamalia):
    pass

blacky = Anjing()
toni = Manusia()
toni.interaksi()
blacky.interaksi()

print('#######################################################')
print('POLYMORPHISM')

class Employee7:
    company = 'ABC'
    overtime_pay = 250000

    def __init__(self, name, age, salary): 
        self.name = name
        self.age = age 
        self.salary = salary 
        self.bonus = 0
    
    def overtime(self):
        self.bonus += self.overtime_pay 
    
    def project_bonus(self, pr_bonus):
        self.bonus += pr_bonus 
    
    def total_salary(self):
        return self.salary + self.bonus

class DataAnalyst2(Employee7):
    def __init__(self, name, age, salary): 
        super().__init__ (name, age, salary)

    def overtime(self):
        super().overtime()
        self.bonus += int(self.salary * 0.05)

aksara = DataAnalyst2('Aksara', 25, 8500000)
aksara.overtime()
print("Total salary:",aksara.total_salary())

print('#######################################################')
print('DEFAULT PARAMETER')

class Employee8:
    company = 'ABC'
    overtime_pay = 250000

    def __init__(self, name, age = 21, salary = 5000000):
        self.name = name
        self.age = age
        self.salary = salary
        self.bonus = 0

    def overtime(self):
        self.bonus += self.overtime_pay
    
    def project_bonus(self, pj_bonus):
        self.bonus += pj_bonus
    
    def total_salary(self):
        return self.salary + self.bonus

new_emp1 = Employee8("Budi")
new_emp2 = Employee8("Didi", 25)
new_emp3 = Employee8("Hadi", salary = 8000000)

emp_list = [new_emp1, new_emp2, new_emp3]

i = 1
for data in emp_list:
    print("Data #" + str(i))
    print("Name: " + data.name)
    print("Age: " + str(data.age))
    print("Total salary: " + str(data.total_salary()))
    print("--------------------")
    i += 1

print('#######################################################')
print('KUIS')

class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur
    
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    
    def tambahan_proyek(self,jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan
    
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan 

class TenagaLepas(Karyawan):
    def __init__(self, nama, usia, pendapatan): 
        super().__init__(nama, usia, pendapatan, 0)
    
    def tambahan_proyek(self, nilai_proyek): 
        self.pendapatan_tambahan += nilai_proyek * 0.01

class AnalisData(Karyawan):
    def __init__(self, nama, usia = 21, pendapatan = 6500000, 
                 insentif_lembur = 100000):
        super().__init__(nama, usia, pendapatan, insentif_lembur) 

class IlmuwanData(Karyawan):
    def __init__(self, nama, usia = 25, pendapatan = 12000000, 
                 insentif_lembur = 150000):
        super().__init__(nama, usia, pendapatan, insentif_lembur) 
    
    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan += 0.1 * nilai_proyek 

class PembersihData(TenagaLepas):
    def __init__(self, nama, usia, pendapatan = 4000000): 
        super().__init__(nama, usia, pendapatan)

class DokumenterTeknis(TenagaLepas):
    def __init__(self, nama, usia, pendapatan = 2500000): 
        super().__init__(nama, usia, pendapatan)
    
    def tambahan_proyek(self, jumlah_tambahan): 
        return

class Perusahaan:
    def __init__(self, nama, alamat, nomor_telepon): 
        self.nama = nama
        self.alamat = alamat 
        self.nomor_telepon = nomor_telepon 
        self.list_karyawan = []
    
    def aktifkan_karyawan(self, karyawan): 
        self.list_karyawan.append(karyawan)
    
    def nonaktifkan_karyawan(self, nama_karyawan): 
        karyawan_nonaktif = None
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan: 
                karyawan_nonaktif = karyawan 
                break
        if karyawan_nonaktif is not None: 
            self.list_karyawan.remove(karyawan_nonaktif)
    
    def total_pengeluaran(self): 
        pengeluaran = 0
        for karyawan in self.list_karyawan:
            pengeluaran += karyawan.total_pendapatan() 
        return pengeluaran
    
    def cari_karyawan(self, nama_karyawan): 
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan: 
                return karyawan
        return None

ani = PembersihData('Ani',25)
budi = DokumenterTeknis('Budi',18)
cici = IlmuwanData('Cici')
didi = IlmuwanData('Didi',32,20000000)
efi = AnalisData('Efi')
febi = AnalisData('Febi',28,12000000)

perusahaan = Perusahaan('ABC','Jl. Jendral Sudirman, Blok 11','(021) 95812XX')

perusahaan.aktifkan_karyawan(ani)
perusahaan.aktifkan_karyawan(budi)
perusahaan.aktifkan_karyawan(cici)
perusahaan.aktifkan_karyawan(didi)
perusahaan.aktifkan_karyawan(efi)
perusahaan.aktifkan_karyawan(febi)

print("Daftar karyawan:")
for data in perusahaan.list_karyawan:
    print(data.nama)

print("Total pengeluaran ABC:",perusahaan.total_pengeluaran())