from django.db import models

# Create your models here 

class Location(models.Model):
    """storing the location the picture was taken """
    location = models.CharField(max_length = 30)
    def __str__(self):
        return self.location

    def save_loc(self):
        """ saving the location"""
        self.save()
    def delte_loc(self):
        """ deleting the  location """
        self.delete()

    @classmethod
    def update_loc(cls,item):
        """updating the item in the location """
        pass 
    
class Category(models.Model):
    """ storing the category of the image """
    category  = models.CharField(max_length = 30)

    def __str__(self):
        return self.category
   
    def save_cat(self):
        """ saving the location"""
        self.save()
    def delte_cat(self):
        """ deleting the  location """
        self.delete()

    @classmethod
    def update_cat(cls,item):
        """updating the item in the location """
        pass 
    

class Image(models.Model):
    """ model that stores the image"""
    image = models.ImageField(upload_to = 'media/', blank = True)
    image_name = models.CharField(max_length = 30)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location, null = True)
    image_category = models.ForeignKey(Category, null= True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        """function to save the images"""
        self.save()

    def delet_image(self):
        """ function that deletes image"""
    
    
    @classmethod
    def update_image(cls,item):
        """ function that update the image model"""
        pass

    @classmethod
    def get_image_by_id(cls, id):
        """ retrieving the image by id """
        image = cls.objects.GET.get(id = id)
        return image

    @classmethod 
    def search_image_by_category(cls,category):
        """getting all images with passed category """
        images = cls.objectst.filter(image_category__icontains = category)
        return images
    @classmethod 
    def filter_by_location(cls, location):
        """ getting image with lcoation """
        images = cls.objects.filter(image_location__icontains = location)