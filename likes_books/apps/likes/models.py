from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
      return self.first_name


    def __unicode__(self):
        return "id: " + str(self.id) + ", first_name : " + self.first_name + ", last_name : " + self.last_name + ", email : " + self.email + ", created_at : " + str(self.created_at) + ", updated_at : " + str(self.updated_at)

class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)
    uploader = models.ForeignKey(User, related_name = "uploaded_books")
    liked_users = models.ManyToManyField(User, related_name = "liked_books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self):
      return self.name


# Likes/Books
# NOT NULL contraint error for ForeignKey??
# 	b1=Book.objects.create(name=“book1”,desc=“desc1”,uploader=u1)
# 			-worked
# Have the 2nd user create/upload 2 other books
# 	Book.objects.create(name=“book3”,desc=“book3”,uploader=u2)
# Have the first user like the last book and the first book
# 	u1.liked_books.add(Book.objects.last( ) )
# 	u1.liked_books.add(Book.objects.first( ) )
# Have the 2nd user like the first and 3rd book
# 	u2.liked_books.add(Book.objects.get(id=3))
# Have the 3rd user like all books
# 	u3.liked_books.add(Book.objects.get(id=1))
# Display all users who like the first book
# 	Book.objects.get(id=1).liked_users.all()
# Display the user who uploaded the first book
# 	Book.objects.get(id=1).uploader
# Display all the users who like the second book
# 	Book.objects.get(id=2).liked_users.all( )
# Display all the user who uploaded the second book
# 	Book.objects.get(id=2).uploader


# DONE