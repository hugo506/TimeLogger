from activities.models import Author, Category, Activity
from datetime import datetime

# create 2 dummy users
user2 = Author(fullname="Mohammed Zafar", email="mzafar@alghanim.com",
               password="mzafar", onsite_team=True)

user2.save()

user3 = Author(fullname="Yogesh Nikam", email="ynikam@cybage.com",
               password="nikam", onsite_team=False)

user3.save()

# create 3 categories
c1 = Category(category_type="Meeting", parent_category="Meeting")
c1.save()
c2 = Category(category_type="Generating Reports", parent_category="Support")
c2.save()
c3 = Category(category_type="Vendor Coordination", parent_category="Support")
c3.save()

