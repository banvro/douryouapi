from rest_framework import serializers

from api.models import your_requirement,education_loan,travel_insurance,appy_job_requirement, passport, douryou_login, ApplyLuggageAdliodtmet, ApplyPurchaseFrancbise

class Your_RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = your_requirement
        fields = '__all__'
        print(fields)

class Education_LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = education_loan
        fields = '__all__'

class Travel_InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = travel_insurance
        fields = '__all__'

class Appy_Job_RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = appy_job_requirement
        fields = '__all__'

class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = passport
        fields = '__all__'

class Douryou_LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = douryou_login
        fields = '__all__'

class ApplyLuggageAdliodtmetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyLuggageAdliodtmet
        fields = '__all__'

class ApplyPurchaseFrancbiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyPurchaseFrancbise
        fields = '__all__'








