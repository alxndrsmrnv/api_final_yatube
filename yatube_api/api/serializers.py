from rest_framework import serializers, validators

from posts.models import Post, Group, Comment, Follow


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
    class Meta:
        model = Follow
        fields = '__all__'
