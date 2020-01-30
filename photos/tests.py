from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.

# Create your tests here.
class LocationTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.new_location = Location(loct = 'Nairobi')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

     # Testing Save Method
    def test_save_method(self):
        self.new_location.save()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_del_location(self):
        locations = Location.del_location(self.new_location.id)
        self.assertTrue is None


class CategoryTestClass(TestCase):
    
    def setUp(self):
        # Creating a new editor and saving it
        self.new_category = Category(cat = 'Food')
    
    def test_save(self):
        self.new_category.save()

        category = Category.objects.all()
        self.assertTrue(len(category) > 0)
    
    def test_del_category(self):
        categories = Category.del_category(self.new_category.id)
        self.assertTrue is None
        

class ImageTestClass(TestCase):
    
    def SetUp(self):
        self.image = Image(title = 'BB', description ='Test Description', location = self.new_location, category = self.new_caategory, image ='/media/images/ilnur-kalimullin-kP1AxmCyEXM-unsplash2.jpg')

        self.image.save_image()

        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

        Image.del_photo(self.image.id)        

        images = Image.objects.all()
        self.assertTrue(len(images) == 0)
    
def tearDown(self):
    Location.objects.all().delete()
    Category.objects.all().delete()
    Image.objects.all().delete()       