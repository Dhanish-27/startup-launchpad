from django.db import models

# Create your models here.
class intern_domain(models.Model):
    
    name = models.CharField(max_length=250)
    image = models.BinaryField(null=True, blank=True)  # Store image as binary
    duration = models.CharField(max_length=20, choices=[
        ('1_month', '1 Month'),
        ('3_months', '3 Months'),
        ('6_months', '6 Months')
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    attribute1 = models.CharField(max_length=100, blank=True, null=True)
    attribute2 = models.CharField(max_length=100, blank=True, null=True)
    attribute3 = models.CharField(max_length=100, blank=True, null=True)
    attribute4 = models.CharField(max_length=100, blank=True, null=True)
    attribute5 = models.CharField(max_length=100, blank=True, null=True)
    attribute6 = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'InternDomain'

class StartupRegistartion(models.Model):
    
    user_id=models.CharField(max_length=30,null=True,blank=True)
    startup_Name = models.CharField(max_length=30)
    founder_Name = models.CharField(max_length=50)
    founded_date = models.CharField(max_length=20)
    contact_email = models.CharField(max_length=50)
    contact_phonenumber = models.CharField(max_length=15)
    sector = models.CharField(max_length=30)
    company_stage = models.CharField(max_length=30)
    employee_count = models.CharField(max_length=10)
    Funding_Received = models.CharField(max_length=30)
    Key_technology = models.CharField(max_length=50)
    Address_line_1 = models.CharField(max_length=30)
    Area = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=6)
    Focus_area = models.CharField(max_length=25)
    Funding_duration = models.CharField(max_length=15)
    Linkedin_link = models.CharField(max_length=100)
    Github_link = models.CharField(max_length=100)
    Pitch_deck_link = models.CharField(max_length=100)
    reason = models.CharField(max_length=300)
    status = models.CharField(max_length=300,null=True,blank=True)
    ep1 = models.CharField(max_length=300,null=True,blank=True)
    ep2 = models.CharField(max_length=300,null=True,blank=True)
    ep3 = models.CharField(max_length=300,null=True,blank=True)
    ep4 = models.CharField(max_length=300,null=True,blank=True)
    ep5 = models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.startup_Name

    class Meta:
        db_table = 'Startup_Registartion'  # Specify custom table name here

class MentorRegistartion(models.Model):
    user_id=models.CharField(max_length=30,null=True,blank=True)
    Mentor_Name = models.CharField(max_length=50)
    contact_email = models.CharField(max_length=100)
    contact_phonenumber = models.CharField(max_length=15)
    Expertise = models.CharField(max_length=30)
    Job_title = models.CharField(max_length=30)
    Company_organisation = models.CharField(max_length=50)
    Year_of_experience = models.CharField(max_length=5)
    Address_line_1 = models.CharField(max_length=30)
    Area = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=6)
    Focus_area = models.CharField(max_length=25)
    Available_days = models.CharField(max_length=15)
    Linkedin_link = models.CharField(max_length=100)
    Github_link = models.CharField(max_length=100)
    resume_link = models.CharField(max_length=100)
    Short_bio = models.CharField(max_length=300)
    status = models.CharField(max_length=300,null=True,blank=True)
    ep1 = models.CharField(max_length=300,null=True,blank=True)
    ep2 = models.CharField(max_length=300,null=True,blank=True)
    ep3 = models.CharField(max_length=300,null=True,blank=True)
    ep4 = models.CharField(max_length=300,null=True,blank=True)
    ep5 = models.CharField(max_length=300,null=True,blank=True)


    def __str__(self):
        return self.Mentor_Name

    class Meta:
        db_table = 'Mentor_Registartion'  # Specify custom table name here


class ElearningRegistartion(models.Model):
    user_id=models.CharField(max_length=30,null=True,blank=True)
    student_Name = models.CharField(max_length=50)
    age = models.CharField(max_length=20)
    student_dob = models.CharField(max_length=30)
    contact_email = models.CharField(max_length=50)
    contact_phonenumber = models.CharField(max_length=15)
    College_name_Company_name = models.CharField(max_length=50)
    Department_designation = models.CharField(max_length=30)
    Current_year = models.CharField(max_length=25,null=True,blank=True)
    Year_of_graduation = models.CharField(max_length=5,null=True,blank=True)
    student_skills = models.CharField(max_length=50)
    Address_line_1 = models.CharField(max_length=30)
    Area = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=6)
    Linkedin_link = models.CharField(max_length=100)
    Github_link = models.CharField(max_length=100)
    Resume_link = models.CharField(max_length=100)
    status = models.CharField(max_length=300,null=True,blank=True)
    ep1 = models.CharField(max_length=300,null=True,blank=True)
    ep2 = models.CharField(max_length=300,null=True,blank=True)
    ep3 = models.CharField(max_length=300,null=True,blank=True)
    ep4 = models.CharField(max_length=300,null=True,blank=True)
    ep5 = models.CharField(max_length=300,null=True,blank=True)
    
    

    def __str__(self):
        return self.student_Name

    class Meta:
        db_table = 'student_Registartion'  # Specify custom table name here

class user_detail(models.Model):
    profile_photo = models.FileField(upload_to='userprofile/', null=True, blank=True)
    user_id = models.CharField(max_length=20,null=True,blank=True)
    name = models.CharField(max_length=90,null=True,blank=True)
    bio = models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'User_profile'

import uuid

class Coupon(models.Model):
    unique_id = models.CharField(max_length=50, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    discount_percentage = models.IntegerField()
    status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Expired', 'Expired')], default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = str(uuid.uuid4())[:10]  # Generate a unique 10-character ID
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.discount_percentage}%"

    class Meta:
        db_table = "coupons"


class intern_domain(models.Model):
    
    name = models.CharField(max_length=250)
    image = models.BinaryField(null=True, blank=True)  # Store image as binary
    duration = models.CharField(max_length=20, choices=[
        ('15 day', '15 days'),
        ('1 month', '1 Month'),
        ('2 month', '2 Months'),
        ('3 month', '3 Months'),
        ('6 month', '6 Months')
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    attribute1 = models.CharField(max_length=100, blank=True, null=True)
    attribute2 = models.CharField(max_length=100, blank=True, null=True)
    attribute3 = models.CharField(max_length=100, blank=True, null=True)
    attribute4 = models.CharField(max_length=100, blank=True, null=True)
    attribute5 = models.CharField(max_length=100, blank=True, null=True)
    attribute6 = models.CharField(max_length=100, blank=True, null=True)
    
    def _str_(self):
        return self.name

    class Meta:
        db_table = 'InternDomain'


class payment_history(models.Model):
    user_id = models.CharField(max_length=45,null=True,blank=True)
    domain_name = models.CharField(max_length=45,null=True,blank=True)
    domain_duration = models.CharField(max_length=45,null=True,blank=True)
    transaction_id = models.CharField(max_length=45,null=True,blank=True)
    transaction_ss = models.BinaryField()
    created_at = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.domain_name

    class Meta:
        db_table='transaction_history'

class Userauth(models.Model):
    user_id = models.CharField(max_length=13)
    username = models.CharField(max_length=85)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'user_authenthication'

class InternRegistartion(models.Model):
    user_id = models.CharField(max_length=30, null=True, blank=True)
    student_Name = models.CharField(max_length=50)
    age = models.CharField(max_length=20)
    student_dob = models.CharField(max_length=30)
    contact_email = models.CharField(max_length=50)
    contact_phonenumber = models.CharField(max_length=15)
    College_name = models.CharField(max_length=50)
    Department = models.CharField(max_length=30)
    Current_year = models.CharField(max_length=25, null=True, blank=True)
    Year_of_graduation = models.CharField(max_length=5, null=True, blank=True)
    student_skills = models.CharField(max_length=50)
    Address_line_1 = models.CharField(max_length=30)
    Area = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=6)
    domain = models.CharField(max_length=25)
    duration = models.CharField(max_length=25)
    Linkedin_link = models.CharField(max_length=100)
    Github_link = models.CharField(max_length=100)
    Resume_link = models.CharField(max_length=100)
    reason = models.CharField(max_length=300)
    status = models.CharField(max_length=300, null=True, blank=True)

    # Extra parameters (ep1 to ep10)
    ep1 = models.CharField(max_length=300, null=True, blank=True)
    ep2 = models.CharField(max_length=300, null=True, blank=True)
    ep3 = models.CharField(max_length=300, null=True, blank=True)
    ep4 = models.CharField(max_length=300, null=True, blank=True)
    ep5 = models.CharField(max_length=300, null=True, blank=True)
    ep6 = models.CharField(max_length=300, null=True, blank=True)
    ep7 = models.CharField(max_length=300, null=True, blank=True)
    ep8 = models.CharField(max_length=300, null=True, blank=True)
    ep9 = models.CharField(max_length=300, null=True, blank=True)
    ep10 = models.CharField(max_length=300, null=True, blank=True)

    # Transaction details
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    transaction_screenshot = models.BinaryField(null=True, blank=True)  # Stores image as binary

    def __str__(self):
        return self.student_Name

    class Meta:
        db_table = 'intern_Registartion'  # Custom table name



class collegeRegistartion(models.Model):
    user_id=models.CharField(max_length=30,null=True,blank=True)
    Name = models.CharField(max_length=50)
    
    contact_email = models.CharField(max_length=50)
    contact_phonenumber = models.CharField(max_length=15)
    College_name = models.CharField(max_length=50)
    
    Address_line_1 = models.CharField(max_length=30)
    Area = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=6)
    status = models.CharField(max_length=300,null=True,blank=True)
    ep1 = models.CharField(max_length=300,null=True,blank=True)
    ep2 = models.CharField(max_length=300,null=True,blank=True)
    ep3 = models.CharField(max_length=300,null=True,blank=True)
    ep4 = models.CharField(max_length=300,null=True,blank=True)
    ep5 = models.CharField(max_length=300,null=True,blank=True)
    
    

    def str(self):
        return self.Name

    class Meta:
        db_table = 'College_Registartion'  # Specify custom table name here
