from corsi.models import Corso
from django.test import TestCase
from corsi.models import Corso, Serata
from model_bakery import baker
#from pprint import pprint

class TestCorsi(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.serata1 = baker.make("Serata")
        cls.serata2 = baker.make("Serata")
        cls.corso_django = Corso.objects.create(nome="Django", descrizione="Corso di Django PGB")
        cls.corso_pygame = Corso.objects.create(nome="PyGame", descrizione="Corso di PyGame PGB")
        cls.serata1.corso = cls.corso_django
        cls.serata1.save()
        #pprint(cls.corso.__dict__)

    def test_lista_corsi(self):
        # Questo test dipende dal contenuto del DB
        res = self.client.get("/corsi/")
        self.assertContains(res, "PyGame")
        self.assertContains(res, "Django")

    def test_model_str(self):
        self.assertEqual(str(self.corso_django), 'Corso Django')

    def test_corso_serate(self):
        self.assertEqual(str(self.serata1.corso),  'Corso Django')