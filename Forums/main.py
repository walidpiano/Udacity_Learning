import models
import store

member1 = models.Member("Walid", 32)
member2 = models.Member("Omar", 23)

post1 = models.Post("Lets learn",
                    "Learning is not easy at the beginning, but when you proceed with learnin, you find that it is so much fun at the end",
                    member1)

post2 = models.Post("Programming",
                    "When you decide to learn a programming, you need to be patient at the beginning in order to be able to get through it",
                    member2)

post3 = models.Post("Python Language",
                    "Python language is a very strong language that supports object oriented programming",
                    member1)

#print member1
#print member2

#print post1
#print post2
#print post3

member_store = store.MemberStore()
member_store.add(member1)
member_store.add(member2)

post_store = store.PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)

# for testing members

print (member_store.get_all())
print (member_store.get_by_id(1))
member_store.delete(1)
print (member_store.entity_exists(member1))

print (post_store.get_all())
print (post_store.get_by_id(2))
print (post_store.entity_exists(post2))
post_store.delete(2)
print (post_store.entity_exists(post2))
