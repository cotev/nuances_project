from django import forms
from blog.models import Contact
from blog.models import Comment

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('author','email', 'message',)


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('author', 'message',)
