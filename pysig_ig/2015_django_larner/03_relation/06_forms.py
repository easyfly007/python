from django import forms
from myapp.models import Publisher, Book, Author

class PublisherForm(forms.ModelForm):
	class Meta:
		model = Publisher
		fields = '__all__'

class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = '__all__'
		
class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = '__all__'