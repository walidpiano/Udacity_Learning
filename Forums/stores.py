class MemberStore:

    members = []
    last_id = 1

    @staticmethod
    def get_all():
        return MemberStore.members

    @staticmethod
    def add(member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    @staticmethod
    def get_by_id(id):
        all_members = MemberStore.get_all()
        result = None
        for member in MemberStore.members:
            if member.id == id:
                result =  member
                break
        return result

    @staticmethod
    def update(member):
        member_to_update = MemberStore.get_by_id(member.id)
        member_to_update = member

    @staticmethod
    def delete(id):
        member_to_delete = MemberStore.get_by_id(id)
        MemberStore.members.remove(member_to_delete)

    @staticmethod
    def entity_exists(member):
        result = False
        if MemberStore.get_by_id(member.id) == member:
            result = True
        return result

    @staticmethod
    def get_by_name(name):
        result = []
        all_members = MemberStore.get_all()
        for member in all_members:
            print member
            if member.name == name:
                result.append(member)
                print 'match'
        return result



class PostStore:

    posts = []
    last_id = 1

    @staticmethod
    def get_all():
        return PostStore.posts

    @staticmethod
    def add(post):
        post.id = PostStore.last_id
        PostStore.posts.append(post)
        PostStore.last_id += 1

    @staticmethod
    def get_by_id(id):
        post = None
        for e in PostStore.posts:
            if e.id == id:
                post = e
                break
        return post

    @staticmethod
    def delete(id):
        post_to_delete = PostStore.get_by_id(id)
        PostStore.posts.remove(post_to_delete)

    @staticmethod
    def entity_exists(post):
        result = False
        if PostStore.get_by_id(post.id) == post:
            result = True
        return result