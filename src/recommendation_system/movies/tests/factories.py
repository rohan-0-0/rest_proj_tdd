from factory.faker import Faker
from factory.django import DjangoModelFactory
from models import Movie

class MovieFactory(DjangoModelFactory):
    class Meta:
        model = Movie
    
    title = Faker('sentence', nb_words=4)
    genres = Faker('pylist', nb_elements=3, variable_nb_elements=True, value_types=['str'])


