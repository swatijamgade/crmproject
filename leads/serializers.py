from rest_framework import serializers
from .models import Lead, LeadSource, LeadFollowUp, LeadAssign, LeadNote, LeadTag

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        models = Lead
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'company_name', 'lead_source', 'status', 'created_by', 'updated_at']


class LeadSourceSerializer(serializers.ModelSerializer):

    class Meta:
        models = LeadSource
        fields = '__all__'

class LeadFolloUpSerializer(serializers.ModelSerializer):

    class Meta:
        models = LeadFollowUp
        fields = '__all__'

class LeadAssignSerilaizer(serializers.ModelSerializer):

    class Meta:
        models = LeadAssign
        fields = '__all__'
class LeadNoteSerializer(serializers.ModelSerializer):

    class Meta:
        models = LeadNote
        fields = '__all__'

class LeadTagSerializer(serializers.ModelSerializer):

    class Meta:
        models = LeadTag
        fields = '__all__'

