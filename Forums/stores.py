class MemberStore:

    members = []
    last_id = 1

    def get_all(self):
        return self.members

    def add(self, member):
        member.id = self.last_id
        self.members.append(member)
        self.last_id += 1

    def get_by_id(self, id):
        all_members = self.get_all()
        result = None
        for member in self.members:
            if member.id == id:
                result =  member
                break
        return result

    def update(self, member):
        all_members = self.get_all()
        for index, current_member in enumerate(all_members):
            if current_member.id == member.id:
                all_members[index] = member
                break

    def delete(self, id):
        member_to_delete = self.get_by_id(id)
        self.members.remove(member_to_delete)

    def entity_exists(self, member):
        result = True
        if self.get_by_id(member.id) is None:
            result = False
        return result

    def get_by_name(self, name):
        all_members = self.get_all()
        for member in all_members:
            if member.name == name:
                yield member



class PostStore:

    posts = []
    last_id = 1

    def get_all(self):
        return self.posts

    def add(self, post):
        post.id = self.last_id
        self.posts.append(post)
        self.last_id += 1

    def get_by_id(self, id):
        post = None
        for e in self.posts:
            if e.id == id:
                post = e
                break
        return post

    def delete(self, id):
        post_to_delete = self.get_by_id(id)
        self.posts.remove(post_to_delete)

    def entity_exists(self, post):
        result = False
        if self.get_by_id(post.id) == post:
            result = True
        return result