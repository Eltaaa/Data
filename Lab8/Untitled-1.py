class ProbHash:
    def __init__(self, cap):
        self.hashtable = cap * [None]
        self.n = cap

    def hashFunction(self, mykey):
        # return Address
        return mykey % self.n

    def rehashFunction(self, hashkey):
        return (hashkey + 1) % self.n

    def insertData(self, student_obj):

        # index
        address = self.hashFunction(student_obj.getId())

        while True:
            if self.hashtable[address] is None:
                self.hashtable[address] = student_obj

                print(f"Insert {student_obj.getId()} at index {address}")
                break

            else:
                address = self.rehashFunction(address)

    def searchData(self, std_id):

        x = self.hashFunction(std_id)

        while True:

            if self.hashtable[x] is None:
                print(f"{std_id} does not exist.")
                return None
            
            elif self.hashtable[x].getId() != std_id:
                x = self.rehashFunction(x)

            else:
                print(f"Found {std_id} at index {x}")
                return self.hashtable[x]

    def insertList(self, lst):

        for std in lst:
            self.insertData(std)


class Student:

    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getGpa(self):
        return self.gpa

    def printDetails(self):
        print(f"ID: {self.getId()}")
        print(f"Name: {self.getName()}")
        print(f"GPA: {self.getGpa()}")


s1 = Student(65070001, "Sandee Boonmak", 3.05)
s2 = Student(65070077, "SomSak Jaidee", 2.78)
s3 = Student(65070021, "Somsri Jaiyai", 3.44)
s4 = Student(65070042, "Sommai Meeboon", 2.89)


hash = ProbHash(20)

hash.insertList([s1, s2, s3, s4])

std = hash.searchData(65070077)
std.printDetails()
print("-----------------")

std = hash.searchData(65070021)
std.printDetails()
print("-----------------")

std = hash.searchData(65070042)
std.printDetails()
print("-----------------")

std = hash.searchData(65070032)
