from django.core.exceptions import ValidationError
#This is all currently unused but really useful to know. 
def validate_email(value):
        email = value
        if ".edu" in email:
            raise ValidationError("We do not accept edu emails")



CATEGORIES = ['Mexican', 'Asian', 'American', 'Whatever']

def validate_category(value):
    cat = value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f"{value} not a valid category")
