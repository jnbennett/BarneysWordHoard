from rest_framework import serializers 
from wordhoard.models import Word, Group 

class WordSerializer(serializers.ModelSerializer):

	class Meta:
		model = Word 
		fields = ('pk', 'word', 'defintion_1', 'definition_2', 'definition_3', 'definition_4', 'definition_5'
				'alternate_spellings', 'case', 'gender')

class GroupSerializer(serializers.ModelSerializer):

	word = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='wordhoard:word-detail')

	class Meta:
		model = Group 
		fields = ('pk', 'group', 'word', 'history', 'frequency', 'compounds')