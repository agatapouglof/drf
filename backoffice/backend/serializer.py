import logging
from rest_framework import serializers, exceptions, status
from django.contrib.auth import authenticate, get_user_model
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from .models import GCAAffaire, GCAUser
from django.core.exceptions import ObjectDoesNotExist
from rest_auth.serializers import TokenSerializer, TokenModel, LoginSerializer
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.response import Response
django_logger = logging.getLogger('django')

UserModel = get_user_model



class GCAAffaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = GCAAffaire
        fields = "__all__"


class GCAUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = GCAUser
        fields = ('email', 'username', 'code', 'job', 'account', 'rib', 'daily_tax', 'hourly_rate', "password")


class GCATokenSerializer(TokenSerializer):
        user = GCAUserSerializer()

        class Meta:
            model = TokenModel
            fields = ('key', 'user')


class GCALoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True)
    #email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = GCAUser
        fields = ("username", "password")

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def _validate_email(self, email, password):
        user = None

        if email and password:
            user = self.authenticate(email=email, password=password)
        else:
            msg = _('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def _validate_username(self, username, password):
        user = None

        if username and password:
            user = self.authenticate(username=username, password=password)
        else:
            msg = _('Must include "username" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def _validate_username_email(self, username, email, password):
        user = None

        if email and password:
            user = self.authenticate(email=email, password=password)
        elif username and password:
            user = self.authenticate(username=username, password=password)
        else:
            msg = _('Must include either "username" or "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        django_logger.warning("==========ok=========")

        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')

        user = None

        if username:
            try:
                django_logger.warning("==========try=========")
                user = self._validate_username_email(username, '', password)
                django_logger.warning(user)
                user = GCAUser.objects.get_by_natural_key(username=username)

                if user and user.check_password(password):
                    django_logger.warning("==========check_password=========")
                    attrs['user'] = user
                    return attrs
                else:
                    django_logger.warning("==========false=========")
                    context = "USER_PASSWORD_FAIL"
                    msg = _('test.')
                    raise serializers.ValidationError({'context': 'USER_PASSWORD_FAIL', 'data': [None]})

            except ObjectDoesNotExist as e:
                context = "USER_NOT_FOUND"
                raise exceptions.ValidationError({'context': _('USER_NOT_FOUND'), 'data': None})

        attrs['user'] = user
        return attrs




class GCARegisterSerializer(RegisterSerializer):

        print("hello")

        # FONCTION_CHOICES = (
        #     ('ass', 'Associé'),
        #     ('col', 'Collaborateur'),
        #     ('con', 'Consultant'),
        #     ('sec', 'Sécrétaire'),
        #     ('sta', 'Stagiaire'),
        # )

        code = serializers.CharField(max_length=45, default="")
        #job = serializers.CharField(max_length=45, choices=FONCTION_CHOICES)
        account = serializers.CharField(max_length=254, default="")
        rib = serializers.CharField(max_length=254, default="")
        daily_tax = serializers.FloatField(default=0, help_text="Taux journalier")
        hourly_rate = serializers.FloatField(default=0, help_text="Taux heure")

        # username = serializers.CharField(
        #     max_length=get_username_max_length(),
        #     min_length=allauth_settings.USERNAME_MIN_LENGTH,
        #     required=allauth_settings.USERNAME_REQUIRED
        # )
        # email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
        # password1 = serializers.CharField(write_only=True)
        # password2 = serializers.CharField(write_only=True)

        # def validate_username(self, username):
        #     username = get_adapter().clean_username(username)
        #     return username
        #
        # def validate_email(self, email):
        #     email = get_adapter().clean_email(email)
        #     if allauth_settings.UNIQUE_EMAIL:
        #         if email and email_address_exists(email):
        #             raise serializers.ValidationError(
        #                 _("A user is already registered with this e-mail address."))
        #     return email
        #
        # def validate_password1(self, password):
        #     return get_adapter().clean_password(password)
        #
        # def validate(self, data):
        #     if data['password1'] != data['password2']:
        #         raise serializers.ValidationError(_("The two password fields didn't match."))
        #     return data
        #
        # def custom_signup(self, request, user):
        #     pass
        #
        # def get_cleaned_data(self):
        #     return {
        #         'username': self.validated_data.get('username', ''),
        #         'password1': self.validated_data.get('password1', ''),
        #         'email': self.validated_data.get('email', '')
        #     }

        # def get_cleaned_data(self):
        #     data_dict = super().get_cleaned_data()
        #     data_dict['code'] = self.validated_data.get('code', '')
        #     return data_dict

