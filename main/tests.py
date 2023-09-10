from django.test import TestCase
from .models import Item
# Create your tests here.
from django.test import TestCase, Client

class mainTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.item = Item.objects.create(
            name='Tester',
            item_type='Test Subject',
            amount=100,
            power=0,
            price=1,
            unique_skill='Make sure the code right',
            description='Please works!'
        )

    def test_item_exist(self):
        item = Item.objects.get(name='Tester')
        self.assertEqual(item.item_type, 'Test Subject')
        self.assertEqual(item.amount, 100)
        self.assertEqual(item.power, 0)
        self.assertEqual(item.price, 1)
        self.assertEqual(item.unique_skill, 'Make sure the code right')
        self.assertEqual(item.description, 'Please works!')

    def test_item_in_template(self):
        response = Client().get('')
        self.assertContains(response, 'Tester')

    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_additem_url_is_exist(self):
        response = Client().get('/add_item/')
        self.assertEqual(response.status_code, 200)

    def test_additem_using_main_template(self):
        response = Client().get('/add_item/')
        self.assertTemplateUsed(response, 'additem.html')