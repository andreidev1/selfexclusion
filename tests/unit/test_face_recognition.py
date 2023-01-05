import os
import pytest

from stopgambling.globals.classes.face_recognition import FaceRecognition

'''
User story
User provides his identity card

Scenarios
Success : 
    -> found face
Fail : 
    -> no found face
    -> no image provided
       

'''

# Providing directories
main_path = os.path.join(os.path.dirname(__file__)).replace('\\unit', '')

image_path = main_path + '\\test_images'

cascade_path = main_path.replace('\\tests', '') + '\\stopgambling' + '\\globals' + '\\classes' + '\\cascades' + '\\haarcascade_frontalface_default.xml'

def test_found_face():
    print(cascade_path)
    face = FaceRecognition(image_path + '\\id_card.jpg', cascade_path)

    face.read_image()

    assert face.detect_face() == True


def test_no_found_face():
    face = FaceRecognition(image_path + '\\no_face.png', cascade_path)

    face.read_image()

    assert face.detect_face() == False


def test_no_image_provided():

    with pytest.raises(Exception):
        face = FaceRecognition(cascade_path)

