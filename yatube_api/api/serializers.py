from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers, validators


class PostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Group
        fields = ('title', 'slug', 'description', 'author',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Comment.objects.all(),
                fields=('author', 'text')
            )
        ]


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault())
    author = serializers.SlugRelatedField(slug_field='username',
                                          queryset=User.objects.all())

    class Meta:
        fields = '__all__'
        model = Follow
