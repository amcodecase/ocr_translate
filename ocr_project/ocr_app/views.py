from django.shortcuts import render
from .forms import UploadImageForm
from .ocr_utils import ocr_image  # Ensure this function exists and works
from googletrans import Translator
from PIL import Image
import base64
from io import BytesIO
import logging

# Configure logging
logger = logging.getLogger(__name__)

def ocr_and_translate(request):
    result = None
    error_message = None
    
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Extract image and text from the form
            image_file = request.FILES.get('image')
            text = form.cleaned_data.get('text', '')
            language = form.cleaned_data.get('language', 'en')
            
            if image_file:
                try:
                    # Convert the uploaded image to PIL Image object
                    image = Image.open(image_file)
                    text = ocr_image(image)  # Ensure this function extracts text from image
                    logger.info(f"Extracted text from image: {text}")
                except Exception as e:
                    logger.error(f"Failed to process the uploaded image: {e}")
                    error_message = "Failed to process the uploaded image."
            
            if not text:
                # Handle base64 encoded image
                captured_image = request.POST.get('capturedImage')
                if captured_image:
                    try:
                        # Remove the data URL prefix
                        header, encoded = captured_image.split(",", 1)
                        binary_data = base64.b64decode(encoded)
                        image = Image.open(BytesIO(binary_data))
                        text = ocr_image(image)  # Ensure this function extracts text from image
                        logger.info(f"Extracted text from base64 image: {text}")
                    except Exception as e:
                        logger.error(f"Failed to process the base64 image: {e}")
                        error_message = "Failed to process the base64 image."

            # Translate the extracted or entered text
            if text:
                translator = Translator()
                try:
                    translated_text = translator.translate(text, dest=language).text
                    result = translated_text
                    logger.info(f"Translated text: {result}")
                except Exception as e:
                    logger.error(f"Translation error: {e}")
                    error_message = "Please check back in future updates, we are working on adding that language or fixing the issue."
        else:
            error_message = "Form is invalid. Please check the inputs."

    else:
        form = UploadImageForm()
    
    # Provide languages for selection
    languages = [
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('it', 'Italian'),
        ('pt', 'Portuguese'),
        ('nl', 'Dutch'),
        ('ru', 'Russian'),
        ('ja', 'Japanese'),
        ('zh', 'Chinese'),
        ('ar', 'Arabic'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
        ('pa', 'Punjabi'),
        ('sw', 'Swahili'),
        ('zu', 'Zulu'),
        ('xh', 'Xhosa'),
        ('tn', 'Tswana'),
        ('ss', 'Siswati'),
        ('lu', 'Lunda'),
        ('ny', 'Chewa'),
        ('bem', 'Bemba'),
        ('ton', 'Tonga'),
        ('nya', 'Nyanja'),
        # Add more languages as needed
    ]
    
    return render(request, 'ocr_app/index.html', {
        'form': form,
        'result': result,
        'error_message': error_message,
        'languages': languages
    })
