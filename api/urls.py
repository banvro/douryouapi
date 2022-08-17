from django.urls import path
from . import views

urlpatterns = [
    #path('', views.apiOverview, name='apiOverview'),
    # path('', views.apiOverview, name='apiOverview'),

    # path('All_user_list_nu/', views.ShowAll_number, name='All_user_list_nu'),
    # path('user-detail_nu/<int:pk>/', views.ViewUser_Registration_number, name='user-detail_nu'),
    # path('Add_new_user_nu/', views.CreateUser_Registration_number, name='Add_new_user_nu'),
    # path('update_user_nu/<int:pk>/', views.updateUser_Registration_number, name='update_user_nu'),
    # path('delete_user_nu/<int:pk>/', views.deleteUser_Registration_number, name='delete_user_nu'),
    
 

    # path('All_user_list_email/', views.ShowAll_email, name='All_user_list_email'),
    # path('user-detail_email/<int:pk>/', views.ViewUser_Registration_email, name='user-detail_email'),
    # path('Add_new_user_email/', views.CreateUser_Registration_email, name='Add_new_user_email'),
    # path('update_user_email/<int:pk>/', views.updateUser_Registration_email, name='update_user_email'),
    # path('delete_user_email/<int:pk>/', views.deleteUser_Registration_email, name='delete_user_email'),
    


    # path('All_user_list_facebook/', views.ShowAll_facebook, name='All_user_list_facebook'),
    # path('user-detail_facebook/<int:pk>/', views.ViewUser_Registration_facebook, name='user-detail_facebook'),
    # path('Add_new_user_facebook/', views.CreateUser_Registration_facebook, name='Add_new_user_facebook'),
    # path('Check_email_validation/', views.Check_email_validation, name='Check_email_validation'),
    # path('Check_facebook_validation/', views.Check_facebook_validation, name='Check_facebook_validation'),
    # path('update_user_facebook/<int:pk>/', views.updateUser_Registration_facebook, name='update_user_facebook'),
    # path('delete_user_facebook/<int:pk>/', views.deleteUser_Registration_facebook, name='delete_user_facebook'),





    # path('send_otp/', views.send_otp, name='send_otp'),
    # path('varify_otp/', views.varify_otp, name='varify_otp'),
    


    # Your Requirement all urls..............................
    path('all-your-requirement-list/', views.AllYourRequirement, name='all_your_requirement_list'),
    path('your-requirement-number/<int:pk>/', views.ViewSingleYourReqirement, name='your_requirement_single'),
    path('Add-new-your-requirement/', views.AddNewRequirement, name='Add_new_your_requirement'),


    # Education Lone all urls..............................
    path('all-education-lone-list/', views.AllEducationLoan, name='all_education_lone_list'),
    path('education-lone-number/<int:pk>/', views.ViewSingleEducationLoan, name='education_lone_single'),
    path('Add-new-education-lone/', views.AddNewEducationLone, name='Add_new_your_requirement'),

    # Travel Insurance all urls..............................
    path('all-travel-insurance-list/', views.AllTravelInsurance, name='all_travel_insurance_list'),
    path('travel-insurance-number/<int:pk>/', views.ViewSingleTravelInsurance, name='travel_insurance_single'),
    path('Add-new-travel-insurance/', views.AddNewTravelInsurance, name='Add_new_your_requirement'),

    # Appy Job Requirement all urls..............................
    path('all-job-requirement-list/', views.AllAppyJobRequirement, name='all_job_requirement_list'),
    path('job-requirement-number/<int:pk>/', views.ViewAppyJobRequirement, name='job_requirement_single'),
    path('Add-new-job-requirement/', views.AddNewJobRequirement, name='Add_new_your_requirement'),

    # Passport all urls..............................
    path('all-passport-list/', views.AllPassport, name='all_passport_list'),
    path('passport-number/<int:pk>/', views.ViewSinglePassport, name='your_passport_single'),
    path('Add-new-passport/', views.AddNewPassport, name='Add_new_passport'),

    # Douryou Login all urls..............................
    path('all-douryou-logins-list/', views.AllDouryouLogin, name='all_douryou_logins_list'),
    path('douryou-logins-number/<int:pk>/', views.ViewSingleDouryouLogin, name='douryou_logins_single'),
    path('Add-new-douryou-logins/', views.AddNewDouryouLogin, name='Add_new_douryou_logins'),

    # Apply Luggage Adliodtmet all urls..............................
    path('all-apply-luggage-adliodtmett-list/', views.AllApplyLuggageAdliodtmet, name='all_apply_luggage_adliodtmett_list'),
    path('apply-luggage-adliodtmett-number/<int:pk>/', views.ViewSingleApplyLuggageAdliodtmet, name='apply_luggage_adliodtmett_single'),
    path('Add-new-apply-luggage-adliodtmett/', views.AddNewLuggageAdliodtmet, name='Add_new_apply_luggage_adliodtmett'),

    # Apply Purchase Francbise all urls..............................
    path('all-apply-purchase-francbise-list/', views.AllApplyPurchaseFrancbise, name='all_apply_purchase_francbise_list'),
    path('apply-purchase-francbise-number/<int:pk>/', views.ViewSingleApplyPurchaseFrancbise, name='apply_purchase_francbise_single'),
    path('Add-new-apply-purchase-francbise/', views.AddNewPurchaseFrancbise, name='Add_new_apply_purchase_francbise'),


]
