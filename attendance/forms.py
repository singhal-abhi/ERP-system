from django import forms
from .models import mark_attendance
from erp.models import course,subjects
from branch.models import branch_detail
from datetime import datetime


class mark_attendance_form(forms.ModelForm):
    course=forms.ModelChoiceField(queryset=course.course_obj.all())
    batch=forms.IntegerField(max_value=int(datetime.now().year),min_value=int(datetime.now().year-3))
    branch=forms.ModelChoiceField(queryset=branch_detail.branch_obj.all())
    CHOICES =(
    (None,'------'),
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    )
    section=forms.ChoiceField(choices=CHOICES)
    class Meta:
        model=mark_attendance
        fields=('course','batch','branch','section','subject')

        widgets={
            'course':forms.Select(attrs={'id':'course','class':'form-control'}),
            'batch':forms.TextInput(attrs={'id':'batch','class':'form-control'}),
            'branch':forms.Select(attrs={'id':'branch','class':'form-control'}),
        }
    def __init__(self,*args,**kwargs):

        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset=branch_detail.branch_obj.none()
        self.fields['subject'].queryset=subjects.sub_obj.none()
        

        