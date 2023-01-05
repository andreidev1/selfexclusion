import cv2

class FaceRecognition:
 
    def __init__(self, imagePath, cascPath):
        self.imagePath = imagePath
        self.cascPath = cascPath
        

    def read_image(self):
        self.image = cv2.imread(self.imagePath)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)


    def detect_face(self):
        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier(self.cascPath)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            self.gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        if len(faces) > 0:

            # Draw a rectangle around the faces
            #for (x, y, w, h) in faces:
                #cv2.rectangle(self.image, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Save image
            #cv2.imwrite('detected_face.png', self.image)
            
            return True

        else:
            return False





