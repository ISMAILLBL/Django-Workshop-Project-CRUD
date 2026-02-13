
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def validate_titre(self, value):
        if len(value) > 100:
            raise serializers.ValidationError("Le titre ne peut pas dépasser 100 caractères.")
        return value

    def validate_contenu(self, value):
        if not value.strip():
            raise serializers.ValidationError("Le contenu ne peut pas être vide.")
        return value
