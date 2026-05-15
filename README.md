Abstract
Attendance systems have been a long-standing pain point in academia with most of the traditional paper-based and proxy-prone solutions that exist. In this work, we demonstrate a web-based smart attendance management system (SAMS) - an integrated Flask application for DeepFace facial recognition (Facenet512), GPS based geofencing, and K-Means clustering analytics. We validate the identity of students using facial embeddings (512 dimension) to ensure that only genuine students register their attendance. Also, physical location is validated within a configurable geo-fence radius using Haversine formula on longitude/latitude. So our solution is tamper-proof and real-time. It is a dual-role architecture for both student self-service and administrator oversight, with department-wise analytics, Excel report export, and machine-learning-based attendance classification. The experimental results show high recognition accuracy with strong prevention of duplication and location validation, in turn making the system practical and hence deployable for modern educational institutions.
Keywords: Facial Recognition, DeepFace, Facenet512, Geofencing, Flask, Attendance Management, K-Means Clustering, Biometric Authentication
1. Introduction
Administering student attendance is a basic administrative function in academic institutions globally. Traditional approaches paper registers, roll calls, and sign-in cards are prone to proxy attendance, transcription mistakes, and a heavy faculty burden. As complexity increases in educational institutes, problems of accurate, automated, and tamper-proof attendance solutions need to be solved. In this perspective, AI technology, especially the biometric recognition based on a deep learning network, could be adopted as a breakthrough [1]. Face recognition systems not only remove proxy attendance but also give a smooth experience to even students without the requirement of any physical token or card. Furthermore, their integration with web-based platforms also maximizes their accessibility as these can be run across devices without the need to have dedicated hardware or install native applications. In this paper, we describe the design, implementation, and evaluation of a Flask-based smart attendance system that is built around three main technologies: (1) biometric identity verification using DeepFace Facenet512-based facial recognition, (2) physical location validation with GPS geofencing using the Haversine formula, and (3) machine-learning driven attendance analytics using K-Means clustering[2]. It is a web-based system accessible via any standard web browser and stores all data on MySQL, a structured relational database, which allows it to be ready for immediate usage at the institutional level.
1.1. AI Technology and Biometric Identification in Attendance Systems
The usage of Artificial Intelligence to manage attendance, is a considerable improvement over old identification methods. The earlier systems depended on RFID tags and the bar code scanning, which were automated in nature but prone to sharing cards and losing physical tokens. One of the solutions to these weaknesses has become a huge boom with the adoption of biometric modalities, especially facial recognition methods which helped in anchoring identity on an innate and non-negotiable biological trait [3]. The proposed system is built based on the DeepFace framework, where data processed through single or multiple state-of-the-art face analysis models integrated into a single python API Facenet512, VGG-Face + Google FaceNet, ArcFace and DeepID Facenet512, in particular, produces 512-dimensional embedding vectors which describes specific portions of facial geometry with enough discriminative ability for accurate one-to-many matching at institutional scale [4]. This paper proposes a system that utilizes this feature to enroll multiple facial embeddings per student and matches the embedding on attendance time using cosine similarity thereby achieving reliability despite illumination changes or small pose variations.
1.2. Role of Web-Based GUI Technology in Educational Management
The GUI is the glue that ties together all the innumerable options and inner workings of the machine learning pipeline into something tangible to an end user (the student, administrator). In relation to attendance management systems, the graphical user interface (GUI) needs to support an ensemble that simultaneously processes a live stream via webcam, along with system GPS coordinates for real-time verified feedback status aggregation and browser-based admin data visualization without any custom client-side software installation[5]. With algo = navigator.geolocation.getCurrentPosition() for GPS allow the browser itself to serve as a biometric spatio-temporal data acquirer[6]. With such an architecture, there is no need for desktop applications, which depend on mobile-native development, and instead a cross-platform application with a single code base deployment.
1.3. Detection and Verification of Student Identity Using the Facial Recognition GUI
The central function of the suggested method is to identify a student reliably using facial biometrics typically obtained from a live webcam capture. The enrollment is a specific and first phase in which facial embeddings are created and stored; the second phase is the verification, which consists of taking a live photo of the face that we want to identify or verify our identity. Both of these spaces are mediated through the browser-based GUI (graphical user interface), where real-time feedback and direction are provided at each stage [7].
1.3.1. Extraction of Facial Embeddings from Live Camera Feed
This BGR-format OpenCV image is then converted to RGB via cv2. cvtColor() as the input for DeepFace is in RGB format. The DeepFace. In this step, we invoke the represent() function as shown below−, specifying model_name="Facenet512", enforce_detection=False, and detector_backend="skip" to return our 512-dimensional float vector. The parameters enforce_detection=False and detector_backend="skip" mean that face detection, and alignment (if needed), will be done at the frontend side; the frontend can always run preprocessing on uploaded images, as both dilocations/locations between frames can be construed with continuity together to literally overwrite any detection failure or misalignment on server-side, once again threats to the flow of registration. It accepts registration only if there are at least five valid embeddings in a single-shot run, which provides a good spread of natural-face diversity[8]. During attendance, the same embedding extraction pipeline is applied to a single frame from a live webcam feed. The embedding vector is then compared to all the embeddings that the student has and uses cosine similarity:
\mathrm{similarity}(A,B)=\frac{\vec{A}\cdot\vec{B}}{\parallel\vec{A}\parallel\cdot\parallel\vec{B}\parallel}
The first is the maximum similarity among all saved embeddings – this value for every input image is a recognition confidence score. A cutoff value is 0.50, attendance upwards of that value is confirmed. This threshold strikes a balance between the false acceptance rate and false rejection rate required for the Facenet512 model under indoor lighting conditions.
1.3.2. System Requirements
The system design is oriented toward minimal infrastructure demands to facilitate institutionalization for deployment [9]. These specifications describe the operational environment:
Hardware Requirements:
	Server: Any machine capable of running Python 3.x with at least 4 GB RAM (8 GB recommended for TensorFlow/DeepFace model loading)
	Client: Any webcam-equipped device with a modern web browser supporting HTML5 MediaDevices API and Geolocation API
	Database: MySQL 5.7 or higher with sufficient storage for face embedding data (approximately 2–5 KB per student)
	Network: Internet connectivity for ngrok tunnel access; local LAN deployment is also supported
Software Requirements:
Component	Version	Purpose
Python	3.9+	Runtime environment
Flask	2.3.3	Web framework and routing
DeepFace	0.0.88	Facial recognition engine
OpenCV	4.8.1	Image decoding and preprocessing
TensorFlow	2.15.0	Deep learning backend for DeepFace
PyMySQL	1.1.0	MySQL database connector
bcrypt	4.0.1	Password hashing
scikit-learn	1.4.0	K-Means clustering analytics
pandas	2.1.4	Data manipulation for analytics
openpyxl	3.1.2	Excel report generation
pyngrok	Latest	ngrok tunnel for remote access

2. Proposed Solution
2.1. System Architecture
The proposed system follows the three-tier architecture of client-server systems. In the presentation tier is all HTML5/CSS3/JavaScript pages are presented in student or administrator browser [10]. You end up having the application tier as a Flask Python app that takes care of all request routing, does authentication and face verification logic and interacts with the database. It consists of a MySQL relational database which stores student records, facial embeddings and attendance records as well as credentials for the administrator.
It supports two different kinds of user roles. Students interface the registration and face capture that marks their attendance and personal history views. Administrators view a secure panel that contains dashboard overviews and summaries, student administration tools, attendance reports with filters, Excel export features and analytics powered by machine learning [11]. In the application, role separation is implemented in Python decorator functions called before access is granted at the CRUD API route level where session variables are checked.
2.2. System Flow Diagram
The complete operational flow of the system proceeds through the following sequential stages:
 
Student Registration Flow:
	Registration form submission by students (Name, Register number, Department, Email id and Password)
	Min password length (≥6 char) checks are handled in Flask backend Register number or email which already exist in the database are prohibited through common codes
	The password is hashed with bcrypt; student record inserted into the students table.
	Student session starts; remaining browser page loads face capture app
Face Enrollment Flow:
	Frontend activates webcam via navigator. mediaDevices. getUserMedia()
	Multi-shot fashion capturing system by taking multiple snapshot at a particular interval & condeachframeinbase64JPEG
	Frames are sent to /save_face endpoint using AJAX POST in batches.
	Backend pulls down Facenet512 embeddings from each frame; valid embeddings are aggregated
	The JSON-serialized embedding array is stored in the face_encodings column of the student record if ≥5 valid embeddings are obtained
	Returns success confirmation to frontend & redirects student towards attendance marking
Attendance Verification Flow:
	Student opens /mark_attendance; backend finds out if you've already marked attendance for today
	Student starts scanning face – frontend gets GPS coordinates by Geolocation API and takes a camera frame
	Sends GPS coordinates and base64 image to /verify_attendance
	Stage 1 —Geofence Check: Calculate the Haversine distance based on student GPS and college coordinates; if exceeds the supplied radius, verification fails
	Stage 2 — Duplicate Checking: Database will be queried to see how attendance data already exists for that student for the current date and the duplicate is discarded
	Stage 3 — Biometric Verification: retrieve stored embeddings from student; extract Facenet512 embedding vector from the live frame using a separate circuit to compute cosine similarities and matching maximum similarity against threshold
	Attendance record (with timestamp, status and GPS coordinates) inserted on success; details confirmed at the frontend
2.3. Database Design and Relationships
We have three relational tables in the database schema. The students table contains all enrollment data: name, register number (unique), department, email, bcrypt-hashed password and an array of face embeddings serialized as a JSON array (LONGTEXT column) Attendance table : it stores each attendance events with fkey to student (ie) the date and time, status of marking and the GPS coordinates at those moments[12]. A composite unique key on (student_id, date) at the database level is a strong backstop to ensure that there can be only one attendance record per student on any given day regardless of application logic preventing duplicate records [13].
3. Discussion of Core Technical Documentation
3.1. DeepFace.represent() — Facial Embedding Extraction
The DeepFace. The represent()function is the main interface for face embeddings generation in the-to be described-system[14]. It takes an image input (NumPy array, file path, or base64 string), a name of the model and optional detection and preprocessing parameters and returns list of dictionaries with embeddings key mapped to the raw floating-point embedding vector.
The enforce_detection=False argument tells DeepFace to go ahead with embedding extraction even if no face is detected by the internal DeepFace detector in the image. In this framework, it is suitable as the face detection and framing on agent side are carried out via JavaScript webcam interface, while the server (back-end) processes images that have already been framed centered with faces[15]. A detector_backend="skip", which skips the face alignment pipeline and considers the entire input image as a face region instead. This makes embedding smooth on the server without compromising quality, as long as input images are always framed through the frontend.model_name="Facenet512": This parameter selects Facenet208 based model, which generates 512-dimensional embeddings learned on large-scale face datasets from a modified Inception-ResNet architecture. These embeddings occupy a high-dimensional metric space where cosine similarity is measurable, with vectors of the same individual being much closer to each other than vectors for different individuals.
3.2. Cosine Similarity via numpy.dot() and numpy.linalg.norm()
We do face matching using cosine similarity in the proposed system instead of distance calculations from Euclidean space. Cosine similarity is invariant to the magnitude of vectors and robust to small variations in image intensity levels between enrollment and verification images since it measures angle of two high-dimensional vectors [16].
The similarity between a live embedding vector \vec{A} and a stored embedding vector \vec{B} is computed as:
\mathrm{cosine_similarity}(\vec{A},\vec{B})=\frac{\vec{A}\cdot\vec{B}}{\parallel\vec{A}\parallel_2\cdot\parallel\vec{B}\parallel_2}
The np. The dot() function calculates the inner product between these two 512D vectors, and np. linalg. norm() calculates the L2 (Euclidean) norm of each vector. The obtained similarity value is bounded in the interval [-1, 1], where a value of 1.0 indicates perfect alignment while -.0 indicates orthogonality. For example, with the Facenet512 model images of the same person give a cosine similarity above 0.7 while different people usually give results below 0.4
3.3. OpenCV Image Decoding — cv2.imdecode() and cv2.cvtColor()
OpenCV Image Preprocessing OpenCV is the image preprocessing back-bone for the face enrollment and attendance verification pipelines. The HTML5 frontend encodes the webcam frames to base64 and transmits them as JPEG strings [17]. Base64 wasn't created for this purpose, but it does work the backend decodes these strings using Python's built-in base64 module and reconstructs the binary pixel data as a NumPy array via numpy. frombuffer().
The cvtColor() function executes an in-place channel reordering, swapping the blue and red channels but leaving green, to output a regular RGB image array compatible with the TensorFlow/Keras model inference pipeline that powers DeepFace. Converting the BGR directly to RGB is an essential step if you passed in BGR images to DeepFace, it would invariably use obscure color features that are traced by the CNN model degrading embedding quality and accuracy.
3.4. Haversine Formula — Geofence Distance Computation
Its geofencing capability defines whether or not a student is physically onsite on the college campus at the time of attendance marking. This is done by calculating the great-circle distance between the lat/long coordinates reported by students via their GPS and those registered for the institution using Haversine formula [18].
Haversine formula calculate the minimum distance across the sphere surface between 2 points represented by their GPS coordinates (equivalent degrees and minutes). The same formula for distance d in radians can be given between two geographical points on a sphere of radius R (Earth mean radius: 6,371,000 meters) as follows:
a={\sin\funcapply}^2\mathrm{,}\left(\frac{\Delta\phi}{2}\right)+\cos\funcapply\phi_1\cdot\cos\funcapply\phi_2\cdot{\sin\funcapply}^2\mathrm{\thinsp,}\left(\frac{\Delta\lambda}{2}\right)
d=2R\cdot\arctan\funcapply2\mathrm{\thinsp,}a 1-a
If the calculated distance is greater than the configured GEOFENCE_RADIUS (default value: 200 m) then immediately reject attendance request in verification pipeline and return proper error message back to student with distance in meters[19]. It ensures that remote attendance marking cannot happen from off-campus locations but allows for some noise in the GPS measurement caused due to the way browsers perform geolocation.
3.5. Flask Session Management and Security Architecture
The security architecture in the system described is implemented using different layers. Flask's means of tracking user state as an authenticated user is to provide a server-side cookie signed by your application's secret key.  Restricts access to session cookies on the client-side (i.e. not accessible using JavaScript), protecting against an XSS attack where someone steals our session tokens with a payload running in the user agent. SESSION_COOKIE_SAMESITE = 'Lax' makes it impossible to transmit cookies cross-origin, thus protecting against CSRF attacks for same-site navigation events [20]. 


References
	Kakarla, S., Gangula, P., Rahul, M. S., Singh, C. S. C., & Sarma, T. H. (2020). Smart attendance management system based on face recognition using CNN.
	Nithya, C., Ramya Bharathi, M., Santhini, M., & Sowmya, R. (2020). Face recognition based automatic attendance management system. 
	Jha, S. K., Tyagi, A., Kumar, K., & Sharma, M. (2020). Attendance management system using face recognition. 
	Shrestha, N. L. (2020). A real-time classroom attendance system utilizing Viola-Jones for face detection and LBPH for face recognition. 
	Agarwal, H., Verma, G., & Gupta, L. (2021). Student attendance system based on face recognition. 
	Aryal, A., Adhikari, N., Raut, O. K., & Dahal, S. (2021). Automated face recognition-based attendance system using RetinaFace and FaceNet. 
	Ghosh, D. (2021). Real-time attendance system using face recognition technique. International Journal of Engineering Applied Sciences and Technology, 5(9).
	Gill, S., Sharma, N., Gupta, C., & Samanta, A. (2021). Attendance management system using facial recognition and image augmentation technique.
	Nwazor, N. O., &Olusolape, M. M. (2021). Cloud-based attendance management and information system.
	Face recognition smart attendance system using deep learning. (2021). 
	Poyekar, B., Mote, R., Shah, J., &Dholay, S. (2022). Face recognition attendance system for online classes. 
	Attendance management system using facial recognition. (2022). IEEE Xplore. 
	Machine learning face recognition model for employee tracking and attendance system. (2022). 
	AttenFace: A real-time attendance system using face recognition. (2022). IEEE Xplore.
	Lakshmi, (2023). Smart attendance management system using geo-fencing and machine learning.
	AI-based smart attendance system. (2023). International Journal of Creative Research Thoughts (IJCRT). 
	AI-based attendance monitoring system. (2023). International Journal of Innovative Research in Management, Engineering and Technology (IJIRMPS). 
	Biju, J., Sairam, S., Kumar, K., & Surendran, M. (2024). Enhancing attendance management systems using facial recognition. 
	Jadhav, A. (2024). Face recognition-based attendance system. SSRN. 
	Web application and mobile application-based student attendance management system for facial recognition attendance. (2024). 
