#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_registration_api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# def Check_email_validation(request):
    
    # gtoken = request.data["gtoken"]
    
    # print(gtoken)
    
    # valid_user = User_Registration_with_email.objects.filter(gtoken=gtoken)
    # x = User_RegistrationSerializer_with_Email_id(valid_user, many=True)
    # print("this is x",x.data)
    
    # # print("here ",valid_user)
    
    # if x.data == [] :
    #     raise AuthenticationFailed({
    #     "message" : "User not exist !", 
    #     "value ": "google"
    # })

    # print(valid_user)

    
    #     # x = User_Registration_with_facebook.objects.filter(ftoken__icontation=ftoken)
    # # lol= User_Registration_with_email.objects.filter(gtoken=gtoken)
    
    # return Response({"data":x.data,
        
    #     "message" : "User Email Found !", 
    #     "value ": "message"
    # })
