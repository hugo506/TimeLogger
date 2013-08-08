from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from activities.models import Author, Activity, Category

# template methods for creating dummy model instances
def create_author(fullname = "Foo Bar", email="foo@bar.com", password="foobar", onsite_team=True):
    return Author.objects.create(fullname=fullname,
                                 email=email,
                                 password=password,
                                 onsite_team=onsite_team)

def create_category(category_name = "Scrum Call", parent_category = "Meeting"):
    return Category.objects.create(category_name=category_name,
                                   parent_category=parent_category)

def create_activity(author, activity_type, activity_date):
    return Activity.objects.create(description="Test activity",
                                   author=author,
                                   ticket_number=1111,
                                   activity_type=activity_type,
                                   hours_worked=1.5,
                                   activity_date=activity_date)

class DummyTest(TestCase):
    def test_for_create_author_method(self):
        author = create_author()
        another_author = create_author(fullname="Prakhar Srivastav")
        self.assertEqual(author.fullname, "Foo Bar")
        self.assertEqual(another_author.fullname, "Prakhar Srivastav")
        self.assertEqual(Author.objects.count(), 2)

    def test_for_create_category_method(self):
        category = create_category()
        self.assertEqual(category.parent_category, "Meeting")
        self.assertEqual(Category.objects.count(), 1)

    def test_for_create_activity_method(self):
        author = create_author()
        category = create_category()
        activity = create_activity(author, category, timezone.now())
        self.assertEqual(activity.author.fullname, "Foo Bar")
        self.assertEqual(activity.activity_type.parent_category, "Meeting")
        self.assertEqual(activity.hours_worked, 1.5)
        self.assertEqual(Activity.objects.count(), 1)

class ActivitiesTest(TestCase):
    def test_for_correct_nickname(self):
        author = create_author()
        self.assertEqual(author.nickname(), "Foo")

    def test_for_single_name_nickname(self):
        author = create_author(fullname="Foobar")
        self.assertEqual(author.nickname(), "Foobar")

class ActivityViewTests(TestCase):
    def test_listing_view_with_no_activities(self):
        response = self.client.get(reverse("activity_listing"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "List of activities")
        self.assertQuerysetEqual(response.context['results'], [])

    def test_listing_view_with_one_activity(self):
        author = create_author()
        activity_type = create_category()
        activity = create_activity(author, activity_type, timezone.now())
        response = self.client.get(reverse("activity_listing"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "List of activities")
        self.assertEqual(len(response.context['results']), 1)

class IndexPageTest(TestCase):
    def test_authentication_message(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Anonymous")

