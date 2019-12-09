import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Contact
from ..serializers import contactSerializer

class GetAllPuppiesTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        Contact.objects.create(
            name='Casper', mobile=34512, email='Bull Dog', address='Black')
        Contact.objects.create(
            name='Muffin',mobile=35132, email='a Dog', address='White')
        Contact.objects.create(
            name='Rambo', mobile=38451, email='B Dog', address='Grey')
        Contact.objects.create(
            name='Ricky', mobile=51223, email=' Dog', address='Black-white')

    def test_get_all_contact(self):
        # get API response
        response = Client.get(reverse('get_post_puppies'))
        # get data from db
        puppies = Contact.objects.all()
        serializer = contactSerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status=status.HTTP_200_OK)
class GetSinglePuppyTest(TestCase):
    """ Test module for GET single puppy API """

    def setUp(self):
        Contact.objects.create(
            name='Casper', mobile=34512, email='Bull Dog', address='Black')
        Contact.objects.create(
            name='Muffin',mobile=35132, email='a Dog', address='White')
        Contact.objects.create(
            name='Rambo', mobile=38451, email='B Dog', address='Grey')
        Contact.objects.create(
            name='Ricky', mobile=51223, email=' Dog', address='Black-white')

    def test_get_valid_single_contact(self):
        response = client.get(
            reverse('get_delete_update_puppy', kwargs={'pk': self.rambo.pk}))
        puppy = Contact.objects.get(pk=self.rambo.pk)
        serializer = contactSerializer(puppy)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_contact(self):
        response = Client.get(
            reverse('get_delete_update_puppy', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
class CreateNewcontactTest(TestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'mobile': 4,
            'email': 'Pamerion',
            'address': 'White'
        }
        self.invalid_payload = {
            'name': '',
            'mobile': 4,
            'email': 'Pamerion',
            'address': 'White'
        }

    def test_create_valid_contact(self):
        response = Client.post(
            reverse('get_post_puppies'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_contact(self):
        response = Client.post(
            reverse('get_post_puppies'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSinglePuppyTest(TestCase):
    """ Test module for updating an existing puppy record """

    def setUp(self):
        self.casper = Contact.objects.create(
            name='Casper', mobile=3, email='Bull Dog', address='Black')
        self.muffin = Contact.objects.create(
            name='Muffy', mobile=1, email='Gradane', address='Brown')
        self.valid_payload = {
            'name': 'Muffy',
            'mobile': 2,
            'email': 'Labrador',
            'address': 'Black'
        }
        self.invalid_payload = {
            'name': '',
            'mobile': 4,
            'email': 'Pamerion',
            'address': 'White'
        }

    def test_valid_update_contact(self):
        response = Client.put(
            reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_contact(self):
        response = Client.put(
            reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleContactTest(TestCase):
    """ Test module for deleting an existing puppy record """

    def setUp(self):
        self.casper = Contact.objects.create(
            name='Casper', mobile=3, email='Bull Dog', address='Black')
        self.muffin = Contact.objects.create(
            name='Muffy', mobile=1, email='Gradane', address='Brown')

    def test_valid_delete_contact(self):
        response = Client.delete(
            reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_contact(self):
        response = Client.delete(
            reverse('get_delete_update_puppy', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)