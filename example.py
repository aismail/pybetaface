import logging
from api import BetaFaceAPI

logging.basicConfig(level = logging.INFO)
client = BetaFaceAPI()

client.upload_face('/Users/aismail/Desktop/obama_normal.jpg', 'obama@ami-lab.ro')
matches = client.recognize_faces('/Users/aismail/Desktop/obama_suparat.jpg', 'ami-lab.ro')
print matches
