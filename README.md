# Cheque Parsing System

<h3>Approach to solution</h3>
<img src="https://github.com/CyberSelva29/Standard_Chartered_Hack/assets/101956466/bb2f0d71-0dac-4933-b4c3-7b5d4d5687a9">

<h3>collect the dataset for cheque</h3>
<p>we have collected the IDRBT Cheque dataset</p>

<h3>Annotation</h3>
<p>annotation of the cheque elements to train the model with the help of ROBOFLOW </p>
<p>https://app.roboflow.com/chequeautodataentry/cheque_element_categorization/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true</p>

<h3>YOLOv8 model </h3>
<p>annotated cheque elements are detected using the YOLOv8 model for object detection, bounding boxes and extraction of the all valiable component from cheque</p> 

<h3>OCR for text extraction </h3>     
<p>Image Preprocessing: The input image is preprocessed to enhance clarity and remove noise, utilizing techniques such as character segmentation, normalization, and enhancement.

OCR for Text Extraction
The OCR functionality enables the extraction of text from images, regardless of whether the text is handwritten or printed. This functionality includes:

Image Processing: The input image is processed to detect and extract textual content using OCR algorithms.
Character Recognition: Utilizes OCR engines and libraries to recognize characters and words from the image accurately.
Text Extraction: Extracts the recognized text from the image and provides options to save it in various formats.
Usage
Handwriting to Text Conversion: Upload an image containing handwritten text to convert it into digital text.
OCR for Text Extraction: Upload any image containing text to extract the textual content.</p>

<h3>automatic data entry  </h3>
<P> The recognized text using the <b>OCR</b> are entered in an automated way</P>
<h3>Technologies Used</h3>

<h3>detect potential frauds</h3>
<p><ol>
  <li>Forgery</li>
  <li>Counterfeiting</li>
  <li>Check Kiting</li>
  <li>Check Washing</li>
  <li>Check Truncation Fraud</li>
  <li>Remote Deposit Capture Fraud</li>
  <li>Payee Alteration</li>
  <li>Account Takeover</li>
  <li>Check Tampering</li>
  <li>Duplicate Payment Fraud</li>
</ol>
</p>

<h3>Technologies Stack</h3>
<ol>
  <li>Python Tkinter (for frontend)</li>
  <li>Python (for backend)</li>
  <li>Machine Learning (e.g., TensorFlow, PyTorch)</li>
  <li>Image Processing (e.g., OpenCV)</li>
  <li>OCR Libraries (e.g., Tesseract)</li>
  <li>Cassandra(Database)</li>
</ol>

<h3>Contributed by Team :S.T.A.Y </h3>
<p>PSG college of technology for Standard Chartered hackathon</p>
