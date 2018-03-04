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

print (store.MemberStore.get_all())
print (store.MemberStore.get_by_id(7))
print (store.MemberStore.entity_exists(member1))

store.MemberStore.delete(1)
