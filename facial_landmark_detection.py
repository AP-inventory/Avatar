import dlib

def detect_landmarks(image):
    # Create a face detector and a facial landmarks predictor
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("path/to/shape_predictor_68_face_landmarks.dat")

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = detector(gray)

    # Iterate over each detected face
    for face in faces:
        # Predict the facial landmarks for the current face
        shape = predictor(gray, face)

        # Create a list to store the facial landmarks
        landmarks = []

        # Iterate over each landmark and store its coordinates in the list
        for i in range(68):
            x = shape.part(i).x
            y = shape.part(i).y
            landmarks.append((x, y))

    return landmarks
  
