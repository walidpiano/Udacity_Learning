class MemberStore:

    members = []

    def get_all(self):
        # get all members
        return self.members


    def add(self, member):
        # append member
        self.members.append(member)

    def get_by_id(self, id):
        # search for member by id
        print ''

    def update(self, member):
        # update member data
        print ''

    def delete(self, id):
        # delete member by id
        print ''

    def entity_exists(self, member):
        # checks if an intity exists in a store
        print ''

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
        print ''

    def delete(self, id):
        # delete a post
        print ''
