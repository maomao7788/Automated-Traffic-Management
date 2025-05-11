from django.db import models
from django.contrib.auth.models import User
from django.db import transaction
from datetime import datetime
class Person(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50, default=None)
    birth_date = models.DateField(null=True, blank=True)
    # age = models.IntegerField(blank=True, null=True, default=None)
    address = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)

    def owned_cars(self):
        return [car.number for car in self.cars.all()]
    def fines(self):
        return [fine.number for fine in self.fines.all()]

class License(models.Model):
    number = models.CharField(max_length=50, unique=True)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)

class Junktion(models.Model):
    address = models.CharField(max_length=50, unique=True)
    max_traffic = models.IntegerField(blank=True, null=True, default=None)  
    signals = models.CharField(max_length=50,default="Normal",  help_text="Traffic signal status, Normal or Emergency.")
    can_be_entered_from = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="can_be_left_towards",
        blank=True
    )
    def get_logs(self):
        return self.junction_logs.all()
    def get_cars(self):
        return [car for car in self.cars.all()]
    def get_cameras(self):
        return [camera.number for camera in self.cameras.all()]
    def how_busy(self):
        if len(self.get_cars()) <= self.max_traffic * 0.4:
            return "Low traffic"
        elif len(self.get_cars()) <= self.max_traffic * 0.7:
            return "Moderate traffic"
        else:
            return "High traffic"

class Car(models.Model):
    number = models.CharField(max_length=50, null=True, default=None)
    manufacturer = models.CharField(max_length=50, null=True, default=None)
    model = models.CharField(max_length=50, null=True, default=None)
    color = models.CharField(max_length=50, null=True, default=None)
    owner = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='cars')
    junction = models.ForeignKey(Junktion, on_delete=models.SET_NULL, null=True, related_name='cars')
    important = models.BooleanField(default=False)
    location = models.CharField(max_length=50, null=True, default=None)

class Violation(models.Model):
    description = models.CharField(max_length=350, null=True, default=None)
    fine_amount = models.IntegerField()

class Fine(models.Model):
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='fines')
    description = models.CharField(max_length=350, null=True, default=None)
    fine_amount = models.IntegerField()
    fine_date = models.DateField()
    fine_location = models.CharField(max_length=50)

class Camera(models.Model):
    junction = models.ForeignKey(Junktion, on_delete=models.SET_NULL, null=True, related_name='cameras')
    def generate_fine(self, car, violation):
        try:
            with transaction.atomic():
                fine = Fine.objects.create(
                    person=car.owner,
                    description=violation.description,
                    fine_amount=violation.fine_amount,
                    fine_date=datetime.now(),
                    fine_location = self.junction.address
                )
            return fine
        except Exception as e:
            return f"{e}"

class JunctionLog(models.Model):
    junction = models.ForeignKey(Junktion, on_delete=models.CASCADE, related_name="junction_logs")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="car_logs")
    entry_time = models.DateTimeField(default=datetime.now())
    exit_time = models.DateTimeField(null=True, blank=True)
    left_towards = models.ForeignKey(Junktion, on_delete=models.CASCADE, related_name="left_towards", null=True, blank=True)
