from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from accounts import models

class PatientSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    #class_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = models.User1
    
    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_patient = True
        user.save()
        patient = patient.objects.create(user=user)
        #patient.class_name = self.cleaned_data.get('class_name')
        patient.phone_number = self.cleaned_data.get('phone_number')
        patient.save()
        return user


class DoctorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    #department = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = models.User1
    
    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_doctor = True
        user.save()
        doctor = doctor.objects.create(user=user)
        doctor.phone_number = self.cleaned_data.get('phone_number')
        #teacher.department = self.cleaned_data.get('department')
        doctor.save()
        return user





class StaffSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    #department = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = models.User1
    
    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_staff = True
        user.save()
        staff = staff.objects.create(user=user)
        staff.phone_number = self.cleaned_data.get('phone_number')
        staff.save()
        return user