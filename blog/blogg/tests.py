from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Entry
# Create your tests here.


class BlogTest(TestCase):
	def setUp(self):
		self.user = get_user_model().objects.create(username="testuser")

	def test_create_unpublished(self):
		entry = Entry(title="Titulo", body="publicacao 1", publish=False)
		entry.save()
		self.assertEqual(Entry.objects.all().count(), 1)
		self.assertEqual(Entry.objects.published().count(), 0)

	def test_create_published(self):
		entry = Entry(title="Titulo2", body="publicacao 2", publish=True)
		entry.save()
		self.assertEqual(Entry.objects.all().count(), 1)
		self.assertEqual(Entry.objects.published().count(), 1)