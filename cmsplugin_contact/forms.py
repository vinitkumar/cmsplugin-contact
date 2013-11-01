from django import forms
from django.utils.translation import ugettext_lazy as _
#import settings
from cmsplugin_contact.nospam.forms import HoneyPotForm, RecaptchaForm, AkismetForm
  
class ContactForm(forms.Form):
    first_possibility = forms.DateField(label=_("First"), widget=forms.TextInput(attrs={'placeholder': 'first_possibility*'}))
    second_possibility = forms.DateField(label=_("Second"), widget=forms.TextInput(attrs={'placeholder': 'Second possiblity*'}), required=False)
    name = forms.CharField(label=_("Name"), widget=forms.TextInput(attrs={'placeholder': 'Your name*'}))
    email = forms.EmailField(label=_("Email"), widget=forms.TextInput(attrs={'placeholder': 'Your email address*'}))
    phone = forms.CharField(label=_("Phone"), widget=forms.TextInput(attrs={'placeholder': 'Phone number'})) 
    remarks = forms.CharField(label=_("Remarks"), widget=forms.Textarea(attrs={'placeholder': 'Remarks*'}))

    template = "cmsplugin_contact/contact.html"
  
class HoneyPotContactForm(HoneyPotForm):
    pass

class AkismetContactForm(AkismetForm):
    akismet_fields = {
        'comment_author_email': 'email',
        'comment_content': 'content'
    }
    akismet_api_key = None
    

class RecaptchaContactForm(RecaptchaForm):
    recaptcha_public_key = None
    recaptcha_private_key = None
    recaptcha_theme = None
