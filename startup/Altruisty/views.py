from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.utils import timezone

from startup import settings
from .forms import *
from django.urls import reverse
from django.db.models import Count
from .models import (
    StartupRegistartion,
    MentorRegistartion,
    ElearningRegistartion,
    InternRegistartion,
    collegeRegistartion,
    Userauth,
    user_detail
)
import logging

logger = logging.getLogger(__name__)

# Global counter dictionary
counters = {
    'startup': 0,
    'elearn': 0,
    'student': 0,
    'mentor': 0,
    'intern': 0,
    'college': 0
}

# Last date for counter reset
last_date = None

# Maximum counter limit
MAX_COUNTER_LIMIT = 9999


def get_formatted_timestamp():
    """
    Get the current date formatted as DDMMYYYY.
    """
    now = timezone.now()
    return now.strftime('%d%m%Y')


def generate_unique_password(length):
    """
    Generate a unique password of a given length.
    """
    import random
    import string

    characters = string.ascii_letters + string.digits + '!@#$%^&*()_+[]{}|;:,.<>?'
    password = ''.join(random.choices(characters, k=length))

    # Append a unique identifier (timestamp)
    timestamp = hex(int(timezone.now().timestamp() * 1000))[2:]
    password += timestamp

    return password


def get_next_counter(category, model):
    """
    Dynamically fetch the next counter for a category based on database entries.
    :param category: The category for which to generate the counter (e.g., 'college', 'intern').
    :param model: The model class corresponding to the category.
    :return: The next counter value.
    """
    try:
        # Get today's date in DDMMYYYY format
        current_date = get_formatted_timestamp()

        # Count existing records for the current date
        existing_count = model.objects.filter(ep1=current_date).count()

        # The next counter is one more than the existing count
        next_counter = existing_count + 1

        logger.info(f"Category: {category}, Date: {current_date}, Next Counter: {next_counter}")
        return next_counter

    except Exception as e:
        logger.error(f"Error fetching next counter for {category}: {e}")
        raise e
# Example usage functions for each category
def add_entry_startup():
    get_next_counter('startup', StartupRegistartion)


def add_entry_intern():
    get_next_counter('intern', InternRegistartion)


def add_entry_college():
    get_next_counter('college', collegeRegistartion)


def add_entry_elearn():
    get_next_counter('elearn', ElearningRegistartion)


def add_entry_mentor():
    get_next_counter('mentor', MentorRegistartion)






# College Registration
def registerdatacollege(request):
    if request.method == "POST":
        form = CollegeRegistrationForm(request.POST)
        if form.is_valid():
            try:
                initialpart = "CL"
                secondpart = str(get_formatted_timestamp())
                ep1 = str(get_formatted_timestamp())
                next_counter = get_next_counter('college', collegeRegistartion)
                thirdpart = str(next_counter)
                user_id = initialpart + secondpart + thirdpart
                password = generate_unique_password(16)

                # Save the data
                form.instance.user_id = user_id
                form.instance.status = "accepted"
                form.instance.ep1 = ep1

                save = form.save()

                # Create additional records
                save2 = Userauth(user_id=user_id, username=form.cleaned_data['Name'], password=password)
                save3 = user_detail(user_id=user_id, name=form.cleaned_data['College_name'])
                save2.save()
                save3.save()

                # Send email
                subject = "College Registration Successful"
                message = f"""
                Dear {form.cleaned_data['Name']},

                Congratulations! Your registration at {form.cleaned_data['College_name']} has been successfully completed.

                Here are your credentials:
                Username: {user_id}
                Password: {request.POST.get('password')}

                Please log in and update your password at your earliest convenience.

                Best regards,
                Altruisty Team
                """
                sender_email = 'sarveshsr@altruisty.in'
                recipient_email = form.cleaned_data['contact_email']

                send_mail(subject, message, sender_email, [recipient_email], fail_silently=False)

                messages.success(request, "Successfully registered and credentials sent via email.")
                return render(request, 'collegeForm.html', {'form': form})

            except Exception as e:
                messages.error(request, f"data saved but failed to send mail: {str(e)}")
                return render(request, 'collegeForm.html', {'form': form})
        else:
            messages.error(request, "Form submission is invalid.")
            return render(request, 'collegeForm.html', {'form': form})

    else:
        form = CollegeRegistrationForm()

    return render(request, 'collegeForm.html', {'form': form})

# Startup Registration
def registerdatastartup(request):
    if request.method == 'POST':
        form = StartupRegistrationForm(request.POST)
        if form.is_valid():
            try:
                # Generating unique user_id
                initialpart = "SR"
                secondpart = str(get_formatted_timestamp())
                next_counter = get_next_counter('startup', StartupRegistartion)
                thirdpart = str(next_counter)
                user_id = initialpart + secondpart + thirdpart
                ep1 = str(get_formatted_timestamp())
                # Get cleaned data from form
                startup = form.save(commit=False)
                startup.user_id = user_id
                startup.status = "accepted"
                startup.ep1 = ep1
                # Saving the Startup Registration
                startup.save()
                password = generate_unique_password(16)
                # Create a user authentication and details
                user_auth = Userauth(user_id=user_id, username=startup.startup_Name, password=password)
                user_details = user_detail(user_id=user_id, name=startup.startup_Name)
                user_auth.save()
                user_details.save()

                # Sending registration email
                subject = "Startup Registration Details"
                message = f"Dear {startup.startup_Name},\n\nThank you for registering your startup.\n\nYour User ID: {user_id}\nYour Password: {request.POST.get('password')}\n\nPlease keep this information secure.\n\nBest regards,\nStartup Registration Team"
                from_email = "sarveshsr@altruisty.in"
                recipient_list = [startup.contact_email]

                send_mail(subject, message, from_email, recipient_list)

                # Success message
                messages.success(request, "Successfully registered and email sent.")
                return render(request, 'startupform.html', {'form': form})

            except Exception as e:
                logger.error(f"Error during startup registration: {e}")
                messages.error(request, f"Registration successful but failed to send email: {str(e)}")
                return render(request, 'startupform.html', {'form': form})
        else:
            messages.error(request, "There was an error with the form. Please check your entries.")
            return render(request, 'startupform.html', {'form': form})

    else:
        form = StartupRegistrationForm()
        return render(request, 'startupform.html', {'form': form})

# Mentor Registration

def registerdatamentor(request):
    if request.method == "POST":
        form = MentorRegistrationForm(request.POST)
        
        if form.is_valid():
            try:
                # Generate a unique user ID
                initialpart = "MR"
                secondpart = str(get_formatted_timestamp())
                ep1 = str(get_formatted_timestamp())
                next_counter = get_next_counter('mentor', MentorRegistartion)
                thirdpart = str(next_counter)
                user_id = initialpart + secondpart + thirdpart

                # Get form data
                mentor_registration = form.save(commit=False)
                mentor_registration.user_id = user_id
                mentor_registration.status = "accepted"
                mentor_registration.ep1 = ep1
                mentor_registration.save()

                # Saving user authentication details
                user_auth = Userauth(
                    user_id=user_id,
                    username=form.cleaned_data['Mentor_Name'],
                    password=generate_unique_password(16)
                )
                user_details = user_detail(
                    user_id=user_id,
                    name=form.cleaned_data['Mentor_Name']
                )
                user_auth.save()
                user_details.save()

                # Send confirmation email
                subject = "Mentor Registration Details"
                message = f"Dear {form.cleaned_data['Mentor_Name']},\n\nThank you for registering as a mentor.\n\nYour User ID: {user_id}\nYour Password: {request.POST.get('password')}\n\nPlease keep this information secure.\n\nBest regards,\nE-learning Team"
                from_email = "sarveshsr@altruisty.in"
                recipient_list = [form.cleaned_data['contact_email']]

                send_mail(subject, message, from_email, recipient_list)

                messages.success(request, "Successfully registered and email sent.")
                return render(request, 'mentorform.html', {'form': form})

            except Exception as e:
                logger.error(f"Error during mentor registration: {e}")
                messages.error(request, f"Registration successful but failed to send email: {str(e)}")
                return render(request, 'mentorform.html', {'form': form})
        else:
            messages.error(request, "Please correct the errors in the form.")
            return render(request, 'mentorform.html', {'form': form})

    else:
        form = MentorRegistrationForm()
        return render(request, 'mentorform.html', {'form': form})

# E-learning Registration

def registerdataelearning(request):
    if request.method == "POST":
        form = ElearningRegistrationForm(request.POST)
        
        if form.is_valid():
            try:
                # Generate user ID
                initialpart = "EL"
                secondpart = str(get_formatted_timestamp())
                ep1 = str(get_formatted_timestamp())
                next_counter = get_next_counter('elearn', ElearningRegistartion)
                thirdpart = str(next_counter)
                user_id = initialpart + secondpart + thirdpart

                # Save the form data
                instance = form.save(commit=False)
                instance.user_id = user_id
                instance.ep1 = ep1
                instance.status = "accepted"
                instance.save()

                # Create user and user_detail objects
                password = generate_unique_password(16)
                save2 = Userauth(user_id=user_id, username=instance.student_Name, password=password)
                save3 = user_detail(user_id=user_id, name=instance.student_Name)
                save2.save()
                save3.save()

                # Send confirmation email
                subject = "E-learning Registration Details"
                message = f"Dear {instance.student_Name},\n\nThank you for registering.\n\nYour User ID: {user_id}\nYour Password: {password}\n\nPlease keep this information secure.\n\nBest regards,\nE-learning Team"
                from_email = "sarveshsr@altruisty.in"
                recipient_list = [instance.contact_email]

                send_mail(subject, message, from_email, recipient_list)

                messages.success(request, "Successfully registered and email sent.")
                return render(request, 'studentform.html', {'form': form})
            
            except Exception as e:
                logger.error(f"Error during registration: {e}")
                messages.error(request, f"Registration successful but failed to send email: {str(e)}")
                return render(request, 'studentform.html', {'form': form})

        else:
            messages.error(request, "There was an error with your form submission. Please check the details.")
            return render(request, 'studentform.html', {'form': form})

    else:
        form = ElearningRegistrationForm()
        return render(request, 'studentform.html', {'form': form})
    

def registerdataintern(request):
    if request.method == "POST":
        form = InternRegistrationForm(request.POST)
        initialpart = "IN"
        secondpart = str(get_formatted_timestamp())
        ep1 = str(get_formatted_timestamp())
        next_counter = get_next_counter('intern', InternRegistartion)
        thirdpart = str(next_counter)
        user_id = initialpart+secondpart+thirdpart
        password =  generate_unique_password(10)
        form.instance.user_id= user_id
        form.instance.status = "registered"
        form.instance.ep1 = ep1
        
        save=form.save()
        save2 = Userauth(user_id=user_id, username=form.cleaned_data['student_Name'], password=password)
        save3 = user_detail(user_id=user_id, name=form.cleaned_data['student_Name'])
        save2.save()
        save3.save()
        messages.success(request, "Successfully regis     tered and email sent.")
        return redirect(reverse('altruisty:payment', kwargs={'id': user_id}))
    else:
        # form = InternRegistrationForm()
        return render(request, 'internship.html')

import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render

# Function to generate QR code
def generate_qr(upi_id='sarveshgod2003@okhdfcbank',amount=400):
    
    upi_uri = f"upi://pay?pa={upi_id}&pn=Sarvesh&am={amount}&cu=INR"
    qr = qrcode.make(upi_uri)
    
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer

# Serve the QR Code as an image
def upi_qr_view(request, price):
    discount_percentage = request.session.get('discount_percentage',0)
    print(discount_percentage)
    print(price)
    amount = float(price) * (100-discount_percentage)/100# Default amount, you can fetch this from a database using 'id'
    buffer = generate_qr(amount=amount)
    return HttpResponse(buffer.getvalue(), content_type="image/png")

# Main page to display the QR code
def qr_page(request, id):
    discount_percentage = request.session.get('discount_percentage',0)
    user = get_object_or_404(InternRegistartion,user_id=id)
    domain = get_object_or_404(intern_domain,name=user.domain)
    form = PaymentForm()
    amount = float(domain.price) * (100-discount_percentage)/100
    return render(request, "payment.html", {"id": id,'price':str(domain.price),'form':form,'amount':amount})

from .forms import PaymentForm

def submit_payment(request, id):
    intern = get_object_or_404(InternRegistartion, user_id=id)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            intern.transaction_id = form.cleaned_data['transaction_id']

            # Convert the uploaded file to binary
            screenshot_file = request.FILES['transaction_screenshot']
            intern.transaction_screenshot = screenshot_file.read()
            intern.status = 'requested' 
            intern.save()
            entry = payment_history(user_id=id,domain_name=intern.domain,domain_duration=intern.duration,transaction_id=form.cleaned_data['transaction_id'],transaction_ss=screenshot_file.read())
            entry.save()
            return redirect('altruisty:intern')  # Redirect after successful submission
    else:
        return HttpResponse('Error in form submission')

    
def coupon_check(request, id):
    user = get_object_or_404(InternRegistartion, user_id=id)  # Ensure correct user retrieval
    
    if request.method == "POST":
        coupon_code = request.POST.get("coupon_code", "").strip()

        try:
            # Make sure field names match correctly
            coupon = Coupon.objects.get(
                unique_id=coupon_code, 
                status="Active",
                name=user.student_Name, 
                college_name=user.College_name, 
                phone_number=user.contact_phonenumber, 
                email=user.contact_email
            )
            messages.success(request, "Coupon applied successfully!")

            # Redirect with correct variable name
            request.session['discount_percentage'] = coupon.discount_percentage
            coupon.status = 'Expired'
            coupon.save()
            
            return redirect(reverse('altruisty:payment', kwargs={'id': user.user_id}))

        except Coupon.DoesNotExist:
            messages.error(request, "Invalid Coupon Code!")
            request.session['discount_percentage'] = 0
            return redirect(reverse('altruisty:payment', kwargs={'id': user.user_id}))
        
def home(request):
    return render(request,"templates/index.html")

def interns(request):
    return render(request,"internship.html")

def collegeForm(request):
    return render(request,"collegeForm.html")

def studentform(request):
    return render(request,"studentform.html")

def mentorform(request):
    return render(request,"mentorform.html")

def startupform(request):
    return render(request,"startupform.html")

def aboutus(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def verify(request):
    return render(request,"verifyintern.html")
def services(request):
    return render(request,"service.html")
def DetailsPage(request,heading):
    data = {
        'Idea To Product Development':{
            'title':['Idea Validation Analyst',
                     'Concept to Prototype Development',
                     'MVP Development','Product Development',
                     'Idea Implementation Consultant',
                     'Product Roadmap Consultant'
                     ],
             'images': [
                'id1.png',
                'id2.png',
                'ss.jpg',
                'invest4.png',
                'black.jpg',
                'Student.png'
            ],
            'description': [
                'Assess the potential of your innovative ideas through comprehensive market research. We evaluate market demand, competition, and challenges to help you make informed decisions about your concept.',
                'Bring your idea to life with our expert team. We work with you to refine your concept and create a detailed prototype that captures the essence of your products key features and functionality.',
                'Quickly develop and launch a Minimum Viable Product (MVP) to test your concept in the market. Gather valuable user feedback and iterate on your product to meet real-world needs.',
                'Transform your MVP into a full-scale product. We guide you through every stage, from design and development to testing and deployment, ensuring your product is ready for the market.',
                'Turn your vision into reality with our strategic support. We help you navigate the complexities of implementation, optimize workflows, and achieve your goals efficiently.',
                'Create a comprehensive product roadmap that aligns with your business goals. We help you prioritize features, allocate resources effectively, and adapt to changing market dynamics.'
            ]
        },
        'Patent And Copy Rights':{
            'title':['Patent Research Assistant',
                     'Patent Filing Assistant & Consultant',
                     'Trademark Registration',
                     'Patent Litigation Support & Consultant',
                     'Patent & Copyright Registration',
                     'Copyright Renewal Assistant & Consultant'
                     ],
            'images': [
                'ptnt.png',
                'ptnt2.png',
                'ptnt3.png',
                'reg2.png',
                'fund4.png',
                'b.jpg'
            ],
            'description':[
                "Unlock your innovation's potential with our Patent Research Assistant service. We conduct thorough patent searches and provide in-depth analysis to ensure your ideas are unique and protectable.",
                "Navigate the patent filing process with confidence. Our experts offer personalized support, from drafting applications to meeting regulatory requirements, ensuring your intellectual property is well-protected.",
                "Secure your brand identity with ease through our Trademark Registration service. We guide you through the trademark process, helping you protect your brand and stand out in the market.",
                "When disputes arise, our Patent Litigation Support & Consultant service provides strategic guidance and expert assistance. We help you navigate the complexities of patent litigation, ensuring your intellectual property rights are effectively protected.",
                "Protect your creative works. We offer comprehensive services for patent and copyright registration, safeguarding your intellectual property assets and maximizing their value.",
                "Stay ahead with copyright renewals. We manage the entire process, ensuring your works remain protected and compliant with all deadlines.",                
            ]
        },
        'Company Registration And Other Registration':{
            'title':['Startup Registration Coordinator',
                     'Company Incorporation Advisor',
                     'Professional Corporation Formation Consultant',
                     'Company & Business Registration Consultant',
                     'Legal Entity Formation Consultant',
                     'Import-Export License Assistant'
                     ],
            'images': [
                'reg1.png',
                'reg2.png',
                'reg3.png',
                'reg4.png',
                'invest4.png',
                'invest3.png'
            ],
            'description':[
                "Starting your entrepreneurial journey? Our Startup Registration Coordinator service simplifies the process, handling paperwork and legalities so you can focus on realizing your vision.",
                "Establishing your business? Our Company Incorporation Advisor service offers expert guidance on choosing the right structure and navigating legal requirements to set your company up for success.",
                "Enhance your professional practice with tailored corporate structures. Our Professional Corporation Formation Consultant service is designed for doctors, lawyers, and accountants, ensuring compliance with industry standards.",
                "Starting or expanding your business? Our Company & Business Registration Consultant service provides comprehensive support for all registration and licensing needs, streamlining the process for a smooth start.",
                "Forming a corporation, LLC, or partnership? Our Legal Entity Formation Consultant service guides you through every step, ensuring compliance with regulatory requirements.",
                "Entering international trade? Our Import-Export License Assistant service simplifies obtaining licenses and permits, handling customs documentation, and ensuring trade compliance.",
            ]
        },
        'Funding Preparation':{
            'title':['Funding Proposal Writer',
                     'Grant Application Consultant',
                     'Investor Pitch Deck Designer',
                     'Business Valuation Analyst',
                     'Fundraising Consultant',
                     'Funding Strategy Advisor',
                     'Investor Matchmaker',
                     'Pitch Competition Coordinator',
                     'Investor Engagement Specialist',
                     'Investor Presentation Coach',
                     'Angel Investor Outreach Coordinator',
                     'Investor Outreach Strategist'
                     ],
            'images': [
                'fund2.png',
                'fund3.png',
                'fund1.png',
                'fund4.png',
                'fund5.png',
                'fund6.png',
                'invest1.png',
                'invest2.png',
                'invest3.png',
                'invest4.png',
                'invest5.png',
                'invest6.png'
            ],
            'description':[
                "Are you seeking financial support for your project or organization? Let our experienced funding proposal writers craft compelling proposals that resonate with donors, investors, and grant-making bodies.",
                "Navigating the intricacies of grant applications can be daunting. Our seasoned consultants specialize in guiding you through the process, from identifying relevant funding opportunities to developing winning proposals.",
                "Captivate investors and stakeholders with visually stunning pitch decks that tell your story with clarity and impact. Our design team combines creativity and strategic thinking to craft compelling presentations.",
                "Understanding the true value of your business is crucial for making informed decisions and attracting investors. Our team of skilled analysts employs rigorous methodologies to conduct comprehensive business valuations.",
                "Unlock the full potential of your fundraising efforts with expert guidance from our consultants. From donor engagement strategies to campaign planning and execution, we offer personalized solutions.",
                "Developing a robust funding strategy is essential for sustaining and growing your organization. Our advisors work closely with you to assess your financial needs, identify opportunities for diversification.",  
                "Welcome to Investor Matchmaker, where we connect entrepreneurs with the perfect investors to fuel their dreams. Whether you're a startup seeking funding or an investor looking for promising opportunities, our platform brings together the ideal matches to foster growth and innovation. Let us be your bridge to success.",
                "Are you ready to showcase your startup's potential on a grand stage? As Pitch Competition Coordinators, we curate electrifying events where entrepreneurs pitch their ideas to a panel of esteemed judges. Join us in this exhilarating journey of innovation, where the boldest ideas transform into reality.",
                "Unlock the power of meaningful connections with our Investor Engagement Specialists. We understand that building relationships with investors is paramount to your business's success. Let us craft personalized strategies to captivate investors, turning interest into investment.",
                "Crafting the perfect investor pitch is an art form, and our Investor Presentation Coaches are here to guide you every step of the way. From refining your message to perfecting your delivery, we'll ensure your presentation leaves a lasting impression, setting the stage for investment success.",
                "Calling all entrepreneurs seeking the backing of angel investors! Our Angel Investor Outreach Coordinators specialize in connecting innovative startups with high-net-worth individuals eager to support promising ventures. Let us navigate the intricacies of angel investing to help turn your vision into reality.",
                "In today's competitive landscape, strategic investor outreach is essential for securing funding and driving growth. Our Investor Outreach Strategists are experts in crafting tailored approaches to engage investors effectively. Partner with us to unlock new opportunities and propel your business forward."
            ]
            
        },
        'Investor Connect': {
    'title': [
        'Investor Matchmaker',
        'Pitch Competition Coordinator',
        'Investor Engagement Specialist',
        'Investor Presentation Coach',
        'Angel Investor Outreach Coordinator',
        'Investor Outreach Strategist'
    ],
    'images': [
        'invest1.png',
        'invest2.png',
        'invest3.png',
        'invest4.png',
        'invest5.png',
        'invest6.png'
    ],
    'description': [
        "Welcome to Investor Matchmaker, where we connect entrepreneurs with the perfect investors to fuel their dreams. Whether you're a startup seeking funding or an investor looking for promising opportunities, our platform brings together the ideal matches to foster growth and innovation. Let us be your bridge to success.",
        "Are you ready to showcase your startup's potential on a grand stage? As Pitch Competition Coordinators, we curate electrifying events where entrepreneurs pitch their ideas to a panel of esteemed judges. Join us in this exhilarating journey of innovation, where the boldest ideas transform into reality.",
        "Unlock the power of meaningful connections with our Investor Engagement Specialists. We understand that building relationships with investors is paramount to your business's success. Let us craft personalized strategies to captivate investors, turning interest into investment.",
        "Crafting the perfect investor pitch is an art form, and our Investor Presentation Coaches are here to guide you every step of the way. From refining your message to perfecting your delivery, we'll ensure your presentation leaves a lasting impression, setting the stage for investment success.",
        "Calling all entrepreneurs seeking the backing of angel investors! Our Angel Investor Outreach Coordinators specialize in connecting innovative startups with high-net-worth individuals eager to support promising ventures. Let us navigate the intricacies of angel investing to help turn your vision into reality.",
        "In today's competitive landscape, strategic investor outreach is essential for securing funding and driving growth. Our Investor Outreach Strategists are experts in crafting tailored approaches to engage investors effectively. Partner with us to unlock new opportunities and propel your business forward."
        ]
        },
    }
    selectedheading = data.get(heading, {})
    if 'title' in selectedheading and 'images' in selectedheading and 'description' in selectedheading:
        service_details = zip(selectedheading['title'], selectedheading['images'], selectedheading['description'])
    else:
        service_details = []

    return render(request, 'details.html', {'service_details': service_details, 'heading': heading})
