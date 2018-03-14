from rest_framework import serializers

from gallery.models import Submission, Picture, Comment

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        read_only_fields = ('downscaled', 'fullsize', 'filesize')
        fields = read_only_fields


class SubmissionSerializer(serializers.ModelSerializer):
    favorites = serializers.IntegerField(read_only=True)

    class Meta:
        model = Submission
        read_only_fields = ('id', 'uploaded_by', 'created', 'submission_type', 'thumbnail', 'favorites')
        fields = read_only_fields + ('title', 'description', 'is_visible', 'is_nsfw')


class SubmissionDetailSerializer(serializers.ModelSerializer):
    favorites = serializers.IntegerField(read_only=True)
    picture = PictureSerializer(read_only=True)

    class Meta:
        model = Submission
        read_only_fields = ('id', 'uploaded_by', 'created', 'submission_type', 'thumbnail', 'favorites', 'picture')
        fields = read_only_fields + ('title', 'description', 'is_visible', 'is_nsfw', 'is_commenting_enabled')
    

class SubmissionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        read_only_fields = ('id', 'created', 'user', 'deleted')
        fields = read_only_fields + ('text',)

    def create(self, validated_data):
        return Comment.objects.create(
            user=self.context['request'].user,
            submission_id=self.context['submission_id'],
            text=validated_data['text'],
        )
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if ret['deleted']:
            del ret['text']
        
        return ret
