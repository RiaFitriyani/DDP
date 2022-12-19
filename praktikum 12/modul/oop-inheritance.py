
class Person():
    # Definisi awal variable
    name = ""
    address = ""
    age = 0

    # Constructor :=> Pembungkus
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age 
    
    # Methond / Function 
    def sayHello(self):
        print("Hello nama saya ", self.name, "usia saya", self.age, "alamat saya di", self.address)


class Student(Person):
    # Manggil  constructur class Person
    def __init__(self, name, address, age, nim, jurusan):
        super().__init__(self, name, address, age)
        self.nim = nim
        self.jurusan = jurusan

    # Instance object

yaya = Student("yaya", "Depok, Jabar", 19, "01102062", "Sistem Informasi")

yaya.sayHello()
print("Nim: ", yaya.nim)
print("jurusan: ", yaya.jurusan)
