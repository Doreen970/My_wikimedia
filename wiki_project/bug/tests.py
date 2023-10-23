from django.test import TestCase
from .models import Bug

class BugModelTestCase(TestCase):
    def setUp(self):
        self.bug = Bug.objects.create(
            description="Test bug description",
            bug_type="Test Bug",
            status="To Do"
        )
#tests that the str method works well
    def test_bug_model_str(self):
        self.assertEqual(str(self.bug), "Test Bug")
#this test ensures that there is a description for the bug
    def test_bug_model_description(self):
        bug = Bug.objects.get(bug_type="Test Bug")
        self.assertEqual(bug.description, "Test bug description")
#this ensures that the status chosen is among the choices defined
    def test_bug_model_status_valid_choices(self):
        bug = Bug.objects.get(bug_type="Test Bug")
        valid_choices = [choice[0] for choice in bug._meta.get_field('status').choices]
        self.assertIn(bug.status, valid_choices)            
#this test ensures that there is a bug_type and max_length is 100 characters
    def test_bug_model_bug_type_max_length(self):
        max_length = Bug._meta.get_field('bug_type').max_length
        self.assertEqual(max_length, 100)

#testcases for our views
class BugViewTestCase(TestCase):
    def test_register_bug_view(self):
        response = self.client.get('/register_bug/')
        self.assertEqual(response.status_code, 404)

    def test_bug_list_view(self):
        response = self.client.get('/bug_list/')
        self.assertEqual(response.status_code, 404)

    def test_detail_view(self):
        bug = Bug.objects.create(
            description="Test bug description",
            bug_type="Test Bug",
            status="To Do"
        )
        response = self.client.get(f'/detail/{bug.id}/')
        self.assertEqual(response.status_code, 404)
