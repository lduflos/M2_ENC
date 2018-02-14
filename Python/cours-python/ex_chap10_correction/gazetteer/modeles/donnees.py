from .. app import db


# On crée notre modèle
class Place(db.Model):
	place_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
	place_nom = db.Column(db.Text)
	place_description = db.Column(db.Text)
	place_longitude = db.Column(db.Float)
	place_latitude = db.Column(db.Float)
	place_type = db.Column(db.String(45))




	@staticmethod
	def creer_lieu(nom, latitude, longitude, description, type):
		erreurs = []
		if not nom:
			erreurs.append("Le nom du lieu est obligatoire")
		if not latitude:
			erreurs.append("Il faut indiquer la latitude")
		if not longitude:
			erreurs.append("Il faut indiquer la longitude")
        

        # On vérifie que personne n'a utilisé cet email ou ce login
		uniques = Place.query.filter(
			db.or_(Place.place_nom == nom)
		).count()
		if uniques > 0:
			erreurs.append("Le lieu déjà inscrit dans notre base de données")

		# Si on a au moins une erreur
		if len(erreurs) > 0:
			print(erreurs, nom, latitude, description, longitude)
			return False, erreurs


		lieu = Place(
			place_nom=nom,
			place_latitude=latitude,
			place_longitude=longitude,
			place_description=description,
			place_type=type,
			#changer le nom "type"
	    )
		try:
	        # On l'ajoute au transport vers la base de données
			db.session.add(lieu)
	        # On envoie le paquet
			db.session.commit()

	        # On renvoie l'utilisateur
			return True, lieu

		except Exception as erreur:
			return False, [str(erreur)]
