from django.test import TestCase,client
from .models import Contact
from .serializers import contactSerializers


class ContactTest(TestCase):


    def setUp(self):
        Contact.objects.create(
            name='Casper', mobile=3, email='Bull Dog', address='Black')
        Contact.objects.create(
            name='Muffin', mobile=1, email='Gradane', address='Brown')

    def test_contact(self):
        contact_casper = Contact.objects.get(name='Casper')
        contact_muffin = Contact.objects.get(name='Muffin')
        self.assertEqual(
            contact_casper.get_contact(), "Casper belongs to Bull Dog breed.")
        self.assertEqual(
            contact_muffin.get_contact(), "Muffin belongs to Gradane breed.")
