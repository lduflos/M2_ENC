from .base import Base #import de la base
from json import loads # import des fonctions que nous avons besoin


class TestApi(Base): # hérite de toutes les fonctions et propriétés de base (pas de répétition)
    def test_single_place(self):
        """ Vérifie qu'un lieu est bien traité """
        self.insert_all()
        response = self.client.get("/api/places/1")
        # Le corps de la réponse est dans .data
        # .data est en "bytes". Pour convertir des bytes en str, on fait .decode()
        content = response.data.decode()
        self.assertEqual(
            response.headers["Content-Type"], "application/json"
        )
        json_parse = loads(content)
        self.assertEqual(json_parse["type"], "place")
        self.assertEqual(
            json_parse["attributes"],
            {'name': 'Hippana', 'latitude': 13.4357804, 'longitude': 37.7018481, 'category': 'settlement',
             'description': 'Ancient settlement in the western part of Sicily, probably '
                            'founded in the seventh century B.C.'}
        )
        self.assertEqual(json_parse["links"]["self"], 'http://localhost/place/1')

        # On vérifie que le lien est correct
        seconde_requete = self.client.get(json_parse["links"]["self"])
        self.assertEqual(seconde_requete.status_code, 200)
