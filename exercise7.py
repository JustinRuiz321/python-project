class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_name(self):
        print(f"{self.first_name} {self.last_name}")


class Student(Person):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.lectures = []

    def list_lectures(self):
        if self.lectures:
            print("Lectures attended:", ", ".join(self.lectures))
        else:
            print("No lectures attended.")

    def add_lecture(self, lecture_name):
        self.lectures.append(lecture_name)
        print(f"Lecture '{lecture_name}' added.")

    def remove_lecture(self, lecture_name):
        if lecture_name in self.lectures:
            self.lectures.remove(lecture_name)
            print(f"Lecture '{lecture_name}' removed.")
        else:
            print(f"Lecture '{lecture_name}' not found.")


class Professor(Person):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.subjects = []

    def list_subjects(self):
        if self.subjects:
            print("Subjects taught:", ", ".join(self.subjects))
        else:
            print("No subjects taught.")

    def add_subject(self, subject_name):
        self.subjects.append(subject_name)
        print(f"Subject '{subject_name}' added.")

    def remove_subject(self, subject_name):
        if subject_name in self.subjects:
            self.subjects.remove(subject_name)
            print(f"Subject '{subject_name}' removed.")
        else:
            print(f"Subject '{subject_name}' not found.")


class Lecture:
    def __init__(self, name, max_students, duration):
        self.name = name
        self.max_students = max_students
        self.duration = duration
        self.professors = []

    def print_details(self):
        print(f"Lecture: {self.name}, Duration: {self.duration} hours, Max Students: {self.max_students}")

    def add_professor(self, professor_name):
        self.professors.append(professor_name)
        print(f"Professor '{professor_name}' added to lecture '{self.name}'.")

    def list_professors(self):
        if self.professors:
            print(f"Professors for '{self.name}':", ", ".join(self.professors))
        else:
            print(f"No professors assigned to '{self.name}'.")