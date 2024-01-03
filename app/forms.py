from django import forms
G=[['male','Male'],['female','Female']]
C=[['python','Python'],['DJANGO','DJANGO'],('SQL','SQL')]
class NameForm(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':10,'rows':10}))
    gender=forms.ChoiceField(choices=G,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=C,widget=forms.CheckboxSelectMultiple)