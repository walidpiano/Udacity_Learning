class Member:

    def __init__(self, name, age):
        self.id = 0
        self.name = name
        self.age = age

    def __str__(self):
        return  'name: {}\t\tAge: {}'.format(self.name, self.age)

    def __repr__(self):
        return self.name

class Post(Member):

    def __init__(self, subject, content, member):
        self.subject = subject
        self.content = content
        self.member = member

    def __str__(self):
        return 'member: {}\tage: {}\nsubject: {}\ncontent: {}' .format(self.member.name, self.member.age, self.subject, self.content)

    def __repr__(self):
        return self.subject
