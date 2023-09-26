from datetime import timedelta
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.forms import UserRegistrationForm
from users.models import EmailVerification, User


class UserRegistrationViewTestCase(TestCase):

	def setUp(self) -> None:
		self.path = reverse('users:registration')
		self.data = {
			'first_name': 'Ivan', 'last_name': 'Zabaluev',
			'username': 'sinkarionchik', 'email': 'ivaiika2@yandex.ru',
			'password1': '12345iI', 'password2': '12345iI',
		}

	def test_user_registration_get(self):
		response = self.client.get(self.path)



		self.assertEqual(response.status_code, HTTPStatus.OK)
		self.assertEqual(response.context_data['title'], 'Store - Регистрация')
		self.assertTemplateUsed(response, 'users/register.html')

	def user_registration_success(self):
		# заполняем формы данными и выполняем пост запрос
		response = self.client.post(self.path, self.data)

		username = self.data['username']

		self.assertEqual(response.status_code, HTTPStatus.FOUND)
		self.assertRedirects(response, reverse('users:login'))
		self.assertTrue(User.objects.filter(username=username).exists())

		email_verification = EmailVerification.objects.filter(user=username)
		self.assertTrue(email_verification.exists())
		self.assertEqual(email_verification.first().expireation.date(), (now() + timedelta(hours=48)).date())


	#проверка на ошибку создания пользователя с существующем именем пользователя
	def user_registration_errors(self):
		username = self.data['username']
		user = User.objects.create(username=username)
		response = self.client.post(self.path, self.data)

		self.assertEqual(response.status_code, HTTPStatus.OK)
		self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)

		#./manage.py test . - запускает все тесты в проекте