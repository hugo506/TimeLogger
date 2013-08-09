from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from activities.models import AuthorInfo, Activity, Category
from django.contrib.auth.models import User

class HelperMethods(object):

    def create_author(self, username="foobar", password="test", email="foo@example.com"):
        return User.objects.create_user(username=username,
                                        password=password,
                                        email=email)

    def create_category(self, category_name = "Scrum Call", parent_category = "Meeting"):
        return Category.objects.create(category_name=category_name,
                                       parent_category=parent_category)

    def create_activity(self, author, activity_type, activity_date):
        return Activity.objects.create(description="Test activity",
                                       author=author,
                                       ticket_number=1111,
                                       activity_type=activity_type,
                                       hours_worked=1.5,
                                       activity_date=activity_date)

class HelperMethodsTest(TestCase):

    def setUp(self):
        self.helper = HelperMethods()

    def test_for_create_author_method(self):
        author = self.helper.create_author()
        another_author = self.helper.create_author(username="prakhar")
        self.assertEqual(User.objects.count(), 2)

    def test_for_create_category_method(self):
        category = self.helper.create_category()
        self.assertEqual(category.parent_category, "Meeting")
        self.assertEqual(Category.objects.count(), 1)

    def test_for_create_activity_method(self):
        author = self.helper.create_author()
        category = self.helper.create_category()
        activity = self.helper.create_activity(author, category, timezone.now())
        self.assertEqual(activity.activity_type.parent_category, "Meeting")
        self.assertEqual(activity.hours_worked, 1.5)
        self.assertEqual(Activity.objects.count(), 1)

class IndexPageTest(TestCase):
    def setUp(self):
        self.helper = HelperMethods()
        self.user = self.helper.create_author()
        self.category = self.helper.create_category()
        self.activity = self.helper.create_activity(self.user, self.category, timezone.now())

    def test_unauthenticated_response(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)
