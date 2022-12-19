from modul.person import Person



class Student(Person):
    # Manggil  constructur class Person
    def __init__(self, name, address, age, nim, jurusan):
        super().__init__(name, address, age)
        self.nim = nim
        self.jurusan = jurusan