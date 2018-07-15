from django import forms
from blog.models import Contact
from blog.models import Comment
from blog.models import SketchComment

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('author','email', 'message',)


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('author', 'message',)


class SketchCommentForm(forms.ModelForm):
	class Meta:
		model = SketchComment
		fields = ('author', 'message',)
