class MemberStore:

    members = []
    last_id = 1

    @staticmethod
    def get_all():
        # get all members
        return MemberStore.members

    @staticmethod
    def add(member):
        # append member
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    @staticmethod
    def get_by_id(id):
        # search for member by id
        result = None
        for e in MemberStore.members:
            if e.id == id:
                result =  e
                break
        return result

    @staticmethod
    def update(member):
        # update member data
        pass

    @staticmethod
    def delete(id):
        # delete member by id
        member_to_delete = MemberStore.get_by_id(id)
        if member_to_delete is not None:
            x = 0
            while x < len(MemberStore.members):
                print str(x)
                if MemberStore.members[x].id == member_to_delete.id:
                    del MemberStore.members[x]
                    break
                x += 1

    @staticmethod
    def entity_exists(member):
        # checks if an intity exists in a store
        result = False
        if MemberStore.get_by_id(member.id) is not None:
            result = True
        return result


class PostStore:

    posts = []

    def get_all(self):
        # get all posts
        return self.posts

    def add(self, post):
        # append post
        self.posts.append(post)

    def get_by_id(self, id):
        # search for a post by id
        pass

    def delete(self, id):
        # delete a post
        pass
