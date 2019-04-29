from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


#Gestion user

class GCAUser(AbstractUser):

    FONCTION_CHOICES = (
        ('ass', 'Associé'),
        ('col', 'Collaborateur'),
        ('con', 'Consultant'),
        ('sec', 'Sécrétaire'),
        ('sta', 'Stagiaire'),
    )

    code = models.CharField(max_length=45, default="")
    job = models.CharField(max_length=45, choices=FONCTION_CHOICES)
    account = models.CharField(max_length=254, default="")
    rib = models.CharField(max_length=254, default="")
    daily_tax = models.FloatField(default=0, help_text="Taux journalier")
    hourly_rate = models.FloatField(default=0, help_text="Taux heure")

    class Meta:
        db_table = "auth_user"

    # def create(self):
    #     AbstractUser.objects.create_user

    def __str__(self):
        return self.email


class GCAClient(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=254, default="")
    comment = models.TextField(default="")
    adress = models.CharField(max_length=254, default="")
    phone = models.CharField(max_length=45, default="")
    email = models.EmailField(max_length=254, default="")


    class Meta:
        db_table = "client"
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        # ordering = [""]

        def __str__(self):
            return self.label


class GCAContact(models.Model):
    QUALITE_CHOICES = (
        ('adv', 'Adversaire'),
        ('ges', 'Gestionnaire'),
        ('hui', 'Huissier'),
        ('cor', 'Correspondant')
    )

    TITLE_CHOICE = (
        ('co', 'Compagnie'),
        ('gr', 'Groupe'),
        ('do', 'Docteur'),
        ('ma', 'Madame'),
        ('Mt', 'Maitre'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    first_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, default="")
    adress = models.CharField(max_length=254, default="")
    phone_1 = models.CharField(max_length=45, default="")
    phone_2 = models.CharField(max_length=45, default="")
    quality = models.CharField(max_length=45, choices=QUALITE_CHOICES, default="")
    title = models.CharField(max_length=45, choices=TITLE_CHOICE, default="")

    class Meta:
        db_table = "contact"
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

        def __str__(self):
            return self.name



class GCAAffaire(models.Model):

    NATURE_CHOICE = (
        ('co', 'Construction'),
        ('ds', 'Droit de société'),
        ('ta', 'Transport arérien'),
        ('da', "Droit d'auteur"),
        ('au', 'Autres'),
    )

    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=254, default="")
    number_case = models.CharField(max_length=254, default="")
    description = models.TextField(default="")
    place = models.CharField(max_length=254, default="", help_text="Lieu")
    nature = models.CharField(max_length=45, choices=NATURE_CHOICE, default="")
    comment = models.TextField(default="")
    date_open = models.DateField()
    date_end = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "affaire"
        verbose_name = "Affaire"
        verbose_name_plural = "Affaires"

        def __str__(self):
            return self.number_case
