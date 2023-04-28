from PIL import Image

def encode_message(image_path, message):
    # Load the image
    image = Image.open(image_path).convert('RGBA')
    pixels = list(image.getdata())

    # Encode the message in the image using LSB steganography
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '00000000' # Add null terminator
    if len(binary_message) > len(pixels) * 3:
        raise ValueError('Message is too long for the image')
    for i in range(len(binary_message)):
        pixel = list(pixels[i])
        pixel[0] = (pixel[0] & 0xFE) | int(binary_message[i])
        pixels[i] = tuple(pixel)

    # Save the modified image
    encoded_image = Image.new(image.mode, image.size)
    encoded_image.putdata(pixels)
    encoded_image.save('encoded.png')

if __name__ == '__main__':
    image_path = 'original.png'
    message = '''<!DOCTYPE html>
<html>
  <head>
    <title>Random Student Names</title>
  </head>
  <body>
    <h1>Random Student Names</h1>
    <ul id="student-list">
      <!-- Names will be added here by JavaScript -->
    </ul>
    <script>
      // Define an array of student names
      const students = [
        'Alice',
        'Bob',
        'Charlie',
        'Dave',
        'Eve',
        'Frank',
        'Grace',
        'Heidi',
        'Ivan',
        'Judy',
        'Karl',
        'Larry',
        'Mallory',
        'Nancy',
        'Oliver',
        'Peggy',
        'Quincy',
        'Ralph',
        'Sarah',
        'Tom'
      ];

      // Shuffle the array randomly
      for (let i = students.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [students[i], students[j]] = [students[j], students[i]];
      }

      // Add the first 5 names to the list
      const list = document.getElementById('student-list');
      for (let i = 0; i < 5; i++) {
        const li = document.createElement('li');
        li.textContent = students[i];
        list.appendChild(li);
      }
    </script>
  </body>
</html>
'''
    encode_message(image_path, message)
