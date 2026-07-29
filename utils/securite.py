import bcrypt


def crypter_mot_de_passe(mot_de_passe):
    mot_de_passe = mot_de_passe.encode("utf-8")

    mot_crypte = bcrypt.hashpw(
        mot_de_passe,
        bcrypt.gensalt()
    )

    return mot_crypte.decode("utf-8")


def verifier_mot_de_passe(mot_de_passe, mot_crypte):
    mot_de_passe = mot_de_passe.encode("utf-8")
    mot_crypte = mot_crypte.encode("utf-8")

    return bcrypt.checkpw(
        mot_de_passe,
        mot_crypte
    )