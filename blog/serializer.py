from rest_framework import serializers
from . import models



class BlogSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    blog_paragraphs = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()


    def get_blog_paragraphs(self,blog):
        return models.BlogParagraph.objects.filter(blogpost=blog).values('input_text','image')

    def get_comments(self,blog):
        return models.Comment.objects.filter(post=blog).values('comment_text','name','date_created')

    def get_category(self,blog):
        return blog.categories.names or ''
    class Meta:
        model =models.BlogPost
        fields = [ 
            'id',
            'comments','blog_paragraphs',
            'title','main_image','author','category','date_created','get_paragraph_intro'
        ]