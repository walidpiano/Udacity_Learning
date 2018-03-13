import stores
import models


def create_dummy_data():
    post_store = stores.PostStore()
    post_store.add(models.Post("Life", "Life is always great"))
    post_store.add(models.Post("Sunshine", "Sunshine is amazing"))
    return post_store