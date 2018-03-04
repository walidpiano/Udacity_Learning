class MemberStore:

    members = []
    last_id = 1

    def get_all(self):
        # get all members
        return self.members

    def add(self, member):
        # append member
        member.id = self.last_id
        self.members.append(member)
        self.last_id += 1

    def get_by_id(self, id):
        # search for member by id
        result = None
        for e in self.members:
            if e.id == id:
                result =  e
                break
        return result

    def update(self, member):
        # update member data
        pass

    def delete(self, id):
        # delete member by id
        member_to_delete = self.get_by_id(id)
        if member_to_delete is not None:
            x = 0
            while x < len(self.members):
                if self.members[x].id == member_to_delete.id:
                    del self.members[x]
                    break
                x += 1

    def entity_exists(self, member):
        # checks if an intity exists in a store
        result = False
        if self.get_by_id(member.id) is not None:
            result = True
        return result


class PostStore:

    posts = []
    last_id = 1

    def get_all(self):
        # get all posts
        return self.posts

    def add(self, post):
        # append post
        post.id = self.last_id
        self.posts.append(post)
        self.last_id += 1

    def get_by_id(self, id):
        # search for a post by id
        post = None
        for e in self.posts:
            if e.id == id:
                post = e
                break
        return post


    def delete(self, id):
        # delete a post
        post_to_delete = self.get_by_id(id)
        if post_to_delete is not None:
            x = 0
            while x < len(self.posts):
                if self.posts[x].id == post_to_delete.id:
                    del self.posts[x]
                    break
                x += 1

    def entity_exists(self, post):
        # checks if an intity exists in a store
        result = False
        if self.get_by_id(post.id) is not None:
            result = True
        return result