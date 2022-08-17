import email
from django.db import models

# Create your models here.


class your_requirement(models.Model):
    select_catgry = models.CharField(max_length=20)
    title = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    quali = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    when_require = models.CharField(max_length=40)
    photo = models.CharField(max_length=100000)

    def _str_(self):
        return self.title

class education_loan(models.Model):
    text = models.CharField(max_length=150)
    fname = models.CharField(max_length=150)
    dob = models.CharField(max_length=100000)
    city = models.CharField(max_length=150)
    number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    physical = models.CharField(max_length=255)
    purpose = models.CharField(max_length=120)
    country  = models.CharField(max_length=50)
    dtravel = models.CharField(max_length=120)
    rtravel = models.CharField(max_length=120)
    trip  = models.CharField(max_length=70)
    loantime  = models.CharField(max_length=70)
    bankname = models.CharField(max_length=120)
    loanamount = models.CharField(max_length=120)
    itravlue = models.CharField(max_length=255)
    housetype = models.CharField(max_length=120)
    otherproperty = models.CharField(max_length=255)
    image = models.CharField(max_length=100000)

    def _str_(self):
        return self.text


class travel_insurance(models.Model):
    text = models.CharField(max_length=150)
    fname = models.CharField(max_length=150)
    dob = models.CharField(max_length=100000)
    city = models.CharField(max_length=150)
    number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    physical = models.CharField(max_length=255)
    purpose = models.CharField(max_length=120)
    country  = models.CharField(max_length=50)
    dtravel = models.CharField(max_length=120)
    rtravel = models.CharField(max_length=120)
    trip  = models.CharField(max_length=70)
    policytime  = models.CharField(max_length=70)
    companyname = models.CharField(max_length=120)
    insuranceamount = models.CharField(max_length=120)
    itravlue = models.CharField(max_length=255)
    image = models.CharField(max_length=100000)

    def _str_(self):
        return self.text

class appy_job_requirement(models.Model):
    email = models.CharField(max_length=20)
    qualification = models.CharField(max_length=150)
    experiance = models.CharField(max_length=20)
    salary_expected = models.CharField(max_length=25)
    intersted_field = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    experiance_field = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    photo = models.CharField(max_length=100000)

    def _str_(self):
        return self.email

class passport(models.Model):
    name = models.CharField(max_length=20)
    fname = models.CharField(max_length=150)
    dob = models.CharField(max_length=20)
    city_name = models.CharField(max_length=25)
    number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    type_of_passport = models.CharField(max_length=120)
    locatype_of_services = models.CharField(max_length=120)
    photo = models.CharField(max_length=100000)

    def _str_(self):
        return self.name

class douryou_login(models.Model): 
    number = models.CharField(max_length=255)
    name= models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    photo = models.CharField(max_length=100000)

    def _str_(self):
        return self.number


class ApplyLuggageAdliodtmet(models.Model):
    name = models.CharField(max_length=255)
    fname= models.CharField(max_length=255)
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    alt_number = models.CharField(max_length=50)
    passpost_no = models.CharField(max_length=50)
    adhr_no = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    flight_date = models.CharField(max_length=50)
    flight_name_num = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    detail_lug = models.CharField(max_length=50)
    total_wight = models.CharField(max_length=50)
    amount_offer = models.CharField(max_length=50)
    Recv_name = models.CharField(max_length=50)
    Recv_fname = models.CharField(max_length=50)
    Recv_address = models.CharField(max_length=50)
    Recv_mb_num = models.CharField(max_length=50)
    Recv_passpost_num = models.CharField(max_length=50)
    photo = models.CharField(max_length=100000)

    def _str_(self):
        return self.name


class ApplyPurchaseFrancbise(models.Model):
    intrestede_in = models.CharField(max_length=255)
    Area_type= models.CharField(max_length=255)
    number = models.CharField(max_length=50)
    quli = models.CharField(max_length=50)
    total_o = models.CharField(max_length=50)
    flor_num = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    adhar_num = models.CharField(max_length=50)
    pan_num = models.CharField(max_length=50)
    invest = models.CharField(max_length=50)
    photo = models.CharField(max_length=100000)

    def _str_(self):
        return self.intrestede_in