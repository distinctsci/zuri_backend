class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        if (isinstance(name, str) and isinstance(age, int) and isinstance(tracks, list) and isinstance(score, (int, float))):
            self.name = name
            self.age = age
            self.tracks = tracks
            self.score = score
        else:
            raise ValueError("Wrong values initialized!")
        
        pass
    
    def change_name(self, new_name):
        self.name = new_name
    
    def change_age(self, new_age):
        self.age = new_age

    def add_track(self, new_track):
        self.tracks.append(new_track)
    
    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
score = Bob.get_score()

print(Bob.name, Bob.age, Bob.tracks, score, sep = "\n")