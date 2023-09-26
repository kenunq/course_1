from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory


class IndexViewTestCase(TestCase):

	def test_view(self):
		path = reverse('index')
		response = self.client.get(path)

		self.assertEqual(response.status_code, HTTPStatus.OK)
		self.assertEqual(response.context_data['title'], 'Store')
		self.assertTemplateUsed(response, 'products/index.html')


class ProductsListViewTestCase(TestCase):
	fixtures = ['categories.json', 'goods.json']

	def setUp(self) -> None:
		#установка глобальной переменной для класса, для использования в других функциях через self.
		self.products = Product.objects.all()

	def test_list(self):
		path = reverse('products:index')
		response = self.client.get(path)
		# списки не могуt быть равны, перед сравнением их нужно переобразовать в лист
		print(list(self.products[:1]) == list(response.context_data['object_list']))
		#использование общих проверок
		self._command_test(response)
		self.assertEqual(list(response.context_data['object_list']), list(self.products[:1]))

	def test_list_category(self):
		category = ProductCategory.objects.first()
		path = reverse('products:category', kwargs={'category_id': category.id})
		response = self.client.get(path)

		self._command_test(response)
		self.assertEqual(
			list(response.context_data['object_list']),
			list(self.products.filter(category_id=category.id)[:1])
		)

	#методы которые используются только внутри класса обозначаются в питоне _ перед назаванием метоба
	def _command_test(self, response):
		#создание общих проверок
		self.assertEqual(response.status_code, HTTPStatus.OK)
		self.assertTemplateUsed(response, 'products/products.html')
