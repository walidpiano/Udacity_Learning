class Member:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Post(Member):

    def __init__(self, subject, content, member):
        self.subject = subject
        self.content = content
        self.member = member


