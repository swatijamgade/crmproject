from django.db import models

# Create your models here.
from django.db import models
from accounts.models import Account

class Lead(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('new', 'New'), ('contacted', 'Contacted'), ('converted', 'Converted')], default='new')
    assigned_to = models.CharField(max_length=100, null=True, blank=True)  # Can be a user or sales rep
    account = models.ForeignKey(Account, related_name='leads', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class LeadSource(models.Model):
    source_lead = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.source_lead

class LeadFollowUp(models.Model):
    lead = models.foreginkey('lead', on_delete=models.CASCADE, related_name="follow_ups")
    note = models.TextField()
    follow_up_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"follow-up for {self.lead} on {self.follow_up_date}"

class LeadAssign(models.Model):
    lead = models.ForeignKey('Lead', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return f"{self.lead} assign to {self.assigned_to}"

class LeadNote(models.Model):
    lead = models.ForeignKey('Lead', on_delete=models.CASCADE, related_name="notes")
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.lead}"

class LeadTag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    leads = models.ManyToManyField('Lead', related_name="tags")

    def __str__(self):
        return self.name


