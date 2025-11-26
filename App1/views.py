from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def SignUp(request):
    return render(request, "signup.html")

def Login(request):
    return render(request, "login.html")

def index(request):
    return render(request, 'index.html')

def features(request):
    return render(request, 'features.html')

def Contact(request):
    return render(request, "contact.html")

def About(request):
    return render(request, "about.html")

def pulse(request):
    return render(request, 'pulse.html')

def documentation(request):
    return render(request, 'main.html')

def schedule_therapy(request):
    if request.method == "POST":
        patient_name = request.POST.get('patientName')
        patient_email = request.POST.get('patientEmail')
        therapy_type = request.POST.get('therapyType')
        sessions = request.POST.get('sessions')
        preferred_time = request.POST.get('preferredTime')
        priority = request.POST.get('priority')

        subject = f"Therapy Scheduled: {therapy_type}"
        message = (
            f"Dear {patient_name},\n\n"
            f"Your {therapy_type} therapy has been scheduled.\n"
            f"Number of Sessions: {sessions}\n"
            f"Preferred Time: {preferred_time}\n"
            f"Priority Level: {priority}\n\n"
            f"Please reach on time for your session.\n\n"
            f"Best regards,\nAarogyaMitra Team"
        )
        send_mail(subject, message, 'tanisha.khakhrani2005@gmail.com', [patient_email])

        messages.success(request, f"Therapy scheduled and email sent to {patient_email}")
        return redirect('doctor')

    return render(request, 'main.html')

def send_notification(request):
    if request.method == "POST":
        patient_name = request.POST.get('patientName')
        patient_email = request.POST.get('patientEmail')
        notification_type = request.POST.get('notificationType')
        custom_message = request.POST.get('customMessage')

        subject = f"Notification: {notification_type.replace('-', ' ').title()}"
        message = f"Dear {patient_name},\n\n"
        if custom_message:
            message += f"{custom_message}\n\n"
        else:
            if notification_type == "pre-procedure":
                message += "Please follow the pre-procedure instructions carefully.\n\n"
            elif notification_type == "post-procedure":
                message += "Please follow the post-procedure care instructions carefully.\n\n"
            elif notification_type == "reminder":
                message += "This is a friendly reminder for your upcoming therapy session.\n\n"
            elif notification_type == "follow-up":
                message += "Please schedule your follow-up session at the earliest convenience.\n\n"
        message += "Best regards,\nAarogyaMitra Team"

        try:
            send_mail(
                subject,
                message,
                'tanisha.khakhrani2005@gmail.com',  # From email
                [patient_email],
                fail_silently=False  # This will raise exceptions if email fails
            )
            messages.success(request, f"Notification sent to {patient_name} ({patient_email}) successfully!")
        except BadHeaderError:
            messages.error(request, "Invalid header found.")
        except Exception as e:
            messages.error(request, f"Failed to send email: {str(e)}")

        return redirect('doctor')

    return render(request, 'main.html')

def education(request):
    return render(request, 'main1.html')

def prescription(request):
    return render(request, 'prescription.html')


