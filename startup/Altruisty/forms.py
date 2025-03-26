from django import forms
from .models import *


    # Adding choices for Year of Graduation
YEAR_OF_GRADUATION_CHOICES = [(str(year), str(year)) for year in range(2024, 2031)]  # Adjust according to your needs
YEAR_CHOICES = [
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
    ]
DOMAIN_CHOICES = [
    ('Web', 'Web'),
    ('App', 'App'),
    ('Digital', 'Digital'),
    ('Graphic', 'Graphic'),
    ('Training', 'Training'),
    ('Internship', 'Internship'),
]

# Choices for Duration
DURATION_CHOICES = [
    ('1 month', '1 month'),
    ('2 month', '2 month'),
    ('3 month', '3 months'),
    ('6 month', '6 months'),
]

# Define the choices directly in the form
COMPANY_STAGE_CHOICES = [
    ('Pre Seed', 'Pre Seed'),
    ('Seed', 'Seed'),
    ('Early Stage', 'Early Stage'),
    ('Growth Stage', 'Growth Stage'),
    ('Mature Stage', 'Mature Stage'),
    ('Other', 'Other'),
]

FOCUS_AREA_CHOICES = [
    ('Web', 'Web'),
    ('App', 'App'),
    ('Digital', 'Digital'),
    ('Graphic', 'Graphic'),
    ('Training', 'Training'),
    ('Internship', 'Internship'),
]

FUNDING_DURATION_CHOICES = [
    ('1 month', '1 month'),
    ('3 months', '3 months'),
    ('6 months', '6 months'),
]
FOCUS_AREA_MENTOR_CHOICES = [
    ('Career Guidance', 'Career Guidance'),
    ('Technical Skills Development', 'Technical Skills Development'),
    ('Project-Based Learning', 'Project-Based Learning'),
    ('Interview Preparation', 'Interview Preparation'),
    ('Resume Review', 'Resume Review'),
]

AVAILABLE_DAYS_CHOICES = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]
class CollegeRegistrationForm(forms.ModelForm):
    class Meta:
        model = collegeRegistartion
        fields = [
            'Name', 'contact_email', 'contact_phonenumber', 
            'College_name', 'Address_line_1', 'Area', 
            'city', 'state', 'zipcode'
        ]
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'contact_phonenumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'College_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter College name'}),
            'Address_line_1': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address Line 1'}),
            'Area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Area'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter State'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Zipcode'}),
        }

class StartupRegistrationForm(forms.ModelForm):
    class Meta:
        model = StartupRegistartion
        fields = [
            'startup_Name', 'founder_Name', 'founded_date', 'contact_email',
            'contact_phonenumber', 'sector', 'company_stage', 'employee_count',
            'Funding_Received', 'Key_technology', 'Address_line_1', 'Area',
            'city', 'state', 'zipcode', 'Focus_area', 'Funding_duration',
            'Linkedin_link', 'Github_link', 'Pitch_deck_link', 'reason'
        ]
        widgets = {
            'startup_Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter startup name'}),
            'founder_Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter founder name'}),
            'founded_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'contact_phonenumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'sector': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter sector'}),
            'company_stage': forms.Select(choices=COMPANY_STAGE_CHOICES, attrs={'class': 'form-control'}),
            'employee_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of employees'}),
            'Funding_Received': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter funding received'}),
            'Key_technology': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter key technology'}),
            'Address_line_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address line 1'}),
            'Area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter area'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter zipcode'}),
            'Focus_area': forms.Select(choices=FOCUS_AREA_CHOICES, attrs={'class': 'form-control'}),
            'Funding_duration': forms.Select(choices=FUNDING_DURATION_CHOICES, attrs={'class': 'form-control'}),
            'Linkedin_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter LinkedIn profile link'}),
            'Github_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter GitHub profile link'}),
            'Pitch_deck_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter pitch deck link'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter reason for funding'}),
        }
class MentorRegistrationForm(forms.ModelForm):
    # Adding custom choices for the fields
    

    class Meta:
        model = MentorRegistartion
        fields = [
            'Mentor_Name', 'contact_email', 'contact_phonenumber', 'Expertise', 
            'Job_title', 'Company_organisation', 'Year_of_experience', 
            'Address_line_1', 'Area', 'city', 'state', 'zipcode', 
            'Focus_area', 'Available_days', 'Linkedin_link', 'Github_link', 
            'resume_link', 'Short_bio'
        ]
        widgets = {
            'Mentor_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
            'Expertise': forms.TextInput(attrs={'class': 'form-control'}),
            'Job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'Company_organisation': forms.TextInput(attrs={'class': 'form-control'}),
            'Year_of_experience': forms.TextInput(attrs={'class': 'form-control'}),
            'Address_line_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Area': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'Focus_area': forms.Select(choices=FOCUS_AREA_MENTOR_CHOICES, attrs={'class': 'form-control'}),
            'Available_days': forms.Select(choices=AVAILABLE_DAYS_CHOICES, attrs={'class': 'form-control'}),
            'Linkedin_link': forms.URLInput(attrs={'class': 'form-control'}),
            'Github_link': forms.URLInput(attrs={'class': 'form-control'}),
            'resume_link': forms.URLInput(attrs={'class': 'form-control'}),
            'Short_bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ElearningRegistrationForm(forms.ModelForm):
    # Choices for Current Year field

    # Adding choices for Current Year in form
    Current_year = forms.ChoiceField(choices=YEAR_CHOICES)

    class Meta:
        model = ElearningRegistartion
        fields = [
            'student_Name',
            'age',
            'student_dob',
            'contact_email',
            'contact_phonenumber',
            'College_name_Company_name',
            'Department_designation',
            'Current_year',
            'Year_of_graduation',
            'student_skills',
            'Address_line_1',
            'Area',
            'city',
            'state',
            'zipcode',
            'Linkedin_link',
            'Github_link',
            'Resume_link'
        ]
        
        # Customizing the labels
        labels = {
            'student_Name': 'Name',
            'age': 'Age',
            'student_dob': 'Date of Birth',
            'contact_email': 'Email',
            'contact_phonenumber': 'Phone number',
            'College_name_Company_name': 'College Name',
            'Department_designation': 'Department',
            'Current_year': 'Current Year',
            'Year_of_graduation': 'Graduation Year',
            'student_skills': 'Skills',
            'Address_line_1': 'Building/Street No, Name',
            'Area': 'Area',
            'city': 'City',
            'state': 'State',
            'zipcode': 'Pin Code',
            'Linkedin_link': 'LinkedIn Profile',
            'Github_link': 'GitHub Profile',
            'Resume_link': 'Resume Link',
        }
        

class ElearningRegistrationForm(forms.ModelForm):
    # Adding choices for Current Year in form
    

    class Meta:
        model = ElearningRegistartion
        fields = [
            'student_Name',
            'age',
            'student_dob',
            'contact_email',
            'contact_phonenumber',
            'College_name_Company_name',
            'Department_designation',
            'Current_year',
            'Year_of_graduation',
            'student_skills',
            'Address_line_1',
            'Area',
            'city',
            'state',
            'zipcode',
            'Linkedin_link',
            'Github_link',
            'Resume_link',
        ]

        # Customizing the widgets to include Bootstrap classes for styling
        widgets = {
            'student_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'student_dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
            'College_name_Company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Department_designation': forms.TextInput(attrs={'class': 'form-control'}),
            'Current_year': forms.Select(choices=YEAR_CHOICES, attrs={'class': 'form-control'}),
            'Year_of_graduation': forms.Select(choices=YEAR_OF_GRADUATION_CHOICES, attrs={'class': 'form-control'}),
            'student_skills': forms.TextInput(attrs={'class': 'form-control'}),
            'Address_line_1': forms.TextInput(attrs={'class': 'form-control'}),
            'Area': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'Linkedin_link': forms.URLInput(attrs={'class': 'form-control'}),
            'Github_link': forms.URLInput(attrs={'class': 'form-control'}),
            'Resume_link': forms.URLInput(attrs={'class': 'form-control'}),
        }

        # Customizing the labels for better user experience
        labels = {
            'student_Name': 'Name',
            'age': 'Age',
            'student_dob': 'Date of Birth',
            'contact_email': 'Email',
            'contact_phonenumber': 'Phone number',
            'College_name_Company_name': 'College Name',
            'Department_designation': 'Department',
            'Current_year': 'Current Year',
            'Year_of_graduation': 'Graduation Year',
            'student_skills': 'Skills',
            'Address_line_1': 'Building/Street No, Name',
            'Area': 'Area',
            'city': 'City',
            'state': 'State',
            'zipcode': 'Pin Code',
            'Linkedin_link': 'LinkedIn Profile',
            'Github_link': 'GitHub Profile',
            'Resume_link': 'Resume Link',
        }

from django import forms
from .models import InternRegistartion

class PaymentForm(forms.ModelForm):
    
    

    class Meta:
        model = InternRegistartion
        fields = ['transaction_id']
        widgets ={
            'transaction_id': forms.TextInput(attrs={'class': 'form-control'}),
        }

    
# def getdomainchoices():
#     options = [(None,'Select')]
#     entry = intern_domain.objects.all()
#     for dta in entry :
#         options.append((dta.name,dta.name))
#     return options

# class InternRegistrationForm(forms.ModelForm):
#     # Fields with choices
#     domain_choices = intern_domain.objects.values_list('name', flat=True).distinct()
#     domain = forms.ChoiceField(
#         choices=[('choice','choice')],  # Convert to tuple format
#         widget=forms.Select(attrs={'class': 'form-control'}),
#     )

#     duration = forms.ChoiceField(
#         choices=[('1 month', '1 Month'), ('2 month', '2 Months'),
#                  ('3 month', '3 Months'), ('6 month', '6 Months')],
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )
   
#     class Meta:
#         model = InternRegistartion
#         fields = [
#             'student_Name', 'age', 'student_dob', 'contact_email', 'contact_phonenumber', 
#             'College_name', 'Department', 'Current_year', 'Year_of_graduation',
#             'student_skills', 'Address_line_1', 'Area', 'city', 'state', 'zipcode', 'domain', 
#             'duration', 'Linkedin_link', 'Github_link', 'Resume_link', 'reason'        ]
#         widgets = {
#             'student_Name': forms.TextInput(attrs={'class': 'form-control'}),
#             'age': forms.TextInput(attrs={'class': 'form-control'}),
#             'student_dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'contact_phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
#             'College_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'Department': forms.TextInput(attrs={'class': 'form-control'}),
#             'Current_year': forms.Select(choices=YEAR_CHOICES, attrs={'class': 'form-control'}),
#             'Year_of_graduation': forms.Select(choices=YEAR_OF_GRADUATION_CHOICES, attrs={'class': 'form-control'}),
#             'student_skills': forms.TextInput(attrs={'class': 'form-control'}),
#             'Address_line_1': forms.TextInput(attrs={'class': 'form-control'}),
#             'Area': forms.TextInput(attrs={'class': 'form-control'}),
#             'city': forms.TextInput(attrs={'class': 'form-control'}),
#             'state': forms.TextInput(attrs={'class': 'form-control'}),
#             'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
#             'domain': forms.Select(choices=getdomainchoices(), attrs={'class': 'form-control'}),
#             'duration': forms.Select(choices=DURATION_CHOICES, attrs={'class': 'form-control'}),
#             'Linkedin_link': forms.URLInput(attrs={'class': 'form-control'}),
#             'Github_link': forms.URLInput(attrs={'class': 'form-control'}),
#             'Resume_link': forms.URLInput(attrs={'class': 'form-control'}),
#             'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            
#         }
#         labels = {
#             'student_Name': 'Name',
#             'age': 'Age',
#             'student_dob': 'Date of Birth',
#             'contact_email': 'Email',
#             'contact_phonenumber': 'Phone number',
#             'College_name': 'College Name',
#             'Department': 'Department',
#             'Current_year': 'Current Year in College',
#             'Year_of_graduation': 'Graduation Year',
#             'student_skills': 'Skills',
#             'Address_line_1': 'Address',
#             'Area': 'Area',
#             'city': 'City',
#             'state': 'State',
#             'zipcode': 'Pin Code',
#             'domain': 'Domain',
#             'duration': 'Duration',
#             'Linkedin_link': 'LinkedIn Profile',
#             'Github_link': 'GitHub Profile',
#             'Resume_link': 'Resume Link',
#             'reason': 'Why we should hire you',
            
#         }