from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """
    Stores a single blog post entry related to :model: `auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Model representing a comment on a blog post.

    Attributes:
        post (ForeignKey): The blog post that this comment is associated with.
        author (ForeignKey): The user who made the comment.
        body (TextField): The content of the comment.
        approved (BooleanField): Indicates if the comment is approved for display.
        created_on (DateTimeField): The timestamp when the comment was created.

    Meta:
        ordering: Comments are ordered by the creation date.

    Methods:
        __str__(): Returns a string representation of the comment, showing 
        the author's username and the first 20 characters of the comment body. 
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments_author"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.author.username} by {self.body[:20]}"
