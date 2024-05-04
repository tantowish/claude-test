import base64

# Image encoder base64
def image_encoder(path):
    with open(path, "rb") as image_file:
        # Read the binary data
        image_binary = image_file.read()
        # Encode the binary data to base64
        encoded_image = base64.b64encode(image_binary)
        # Convert bytes to string (if needed)
        encoded_image_str = encoded_image.decode('utf-8')

    return encoded_image_str