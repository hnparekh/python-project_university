from django.forms.models import ModelForm

from results.models import Student, Marks


class StudentForm(ModelForm):
    #name = forms.CharField(widget=forms.TextInput(attrs={'style' : 'border: 1px dotted #000000;'}))
    #address = forms.CharField(widget=forms.TextInput(attrs={'style' : 'border: 3px inset #FFA5A5;'}))
    class Meta:
        model = Student 
        #fields = ('name', 'address', 'gender')
        fields = '__all__'
        
class MarksForm(ModelForm):
    class Meta:
        model = Marks
        fields = '__all__'

