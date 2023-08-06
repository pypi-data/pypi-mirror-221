"""
Text replication for NLP.

Available functions:
- `replace_word_with_synonym(word)`: Replace the given word with a synonym.
- `augment_text_with_synonyms(text, augmentation_factor, probability, progress=True)`: Augment the input text by replacing words with synonyms.
- `load_text_file(filepath)`: Load the contents of a text file.
- `augment_file_with_synonyms(file_path, augmentation_factor, probability, progress=True)`: Augment a text file by replacing words with synonyms.
- `insert_random_word(text, word)`: Insert a random word into the input text.
- `delete_random_word(text)`: Delete a random word from the input text.
- `insert_synonym(text, word)`: Insert a synonym of the given word into the input text.
- `paraphrase(text)`: Paraphrase the input text.
- `flip_horizontal(image)`: Flip the input image horizontally.
- `flip_vertical(image)`: Flip the input image vertically.
- `rotate(image, angle)`: Rotate the input image by a specified angle.
- `random_rotation(image, max_angle)`: Randomly rotate the input image by an angle within the specified range.
- `resize(image, size)`: Resize the input image to the specified size.
- `crop(image, box)`: Crop the input image to the specified rectangular region.
- `random_crop(image, size)`: Randomly crop a region from the input image.
- `perform_image_augmentation(source_dir, target_dir, flip_horizontal=False, flip_vertical=False, rotate=False, random_rotation=False, resize=False, crop=False, max_angle=30, target_size=(224, 224), crop_size=(150, 150))`: Perform image augmentation on images in the source directory and its subdirectories.
"""

import os
import random
import time
import nltk
from nltk.corpus import wordnet
from PIL import Image

nltk.download("wordnet", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)
nltk.download("punkt", quiet=True)

def replace_word_with_synonym(word):
    """
    Replace the given word with a synonym.

    Params:
    - `word` (str): The input word to replace with a synonym.

    Returns:
    - `str`: The synonym for the word.
    """
    try:
        synonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
        
        if synonyms:
            synonym = random.choice(synonyms)
            return synonym
        
        return word
    except Exception as e:
        print(f"An error occurred during word replacement: {str(e)}")
        return word

def augment_text_with_synonyms(text, augmentation_factor, probability, progress=True):
    """
    Augment the input text by replacing words with synonyms.

    Parameters:
    - `text` (str): The input text to be augmented.
    - `augmentation_factor` (int): The number of times to augment the text.
    - `probability` (float): The probability of replacing a random word with a synonym.
    - `progress` (bool): Whether or not to return current progress during augmentation.

    Returns:
    - `list`: A list of augmented text.
    """
    augmented_text = []
    try:
        if probability is None:
            raise ValueError("Probability value cannot be of NoneType. Choose a float from 0 to 1")

        tokens = text.split()
        num_tokens = len(tokens)
        processed_tokens = 0

        start_time = time.time()

        for _ in range(augmentation_factor):
            augmented_tokens = []

            for token in tokens:
                if random.random() < probability:
                    replaced_token = replace_word_with_synonym(token)
                    augmented_tokens.append(replaced_token)
                else:
                    augmented_tokens.append(token)

                processed_tokens += 1

                # Print progress
                if progress:
                    elapsed_time = time.time() - start_time
                    if elapsed_time == 0:
                        elapsed_time = 1e-6  # Set a small value to avoid division by zero
                    tokens_per_sec = processed_tokens / elapsed_time
                    print(f"Progress: {processed_tokens}/{num_tokens} tokens | {tokens_per_sec:.2f} tokens/sec", end="\r")

            augmented_text.append(' '.join(augmented_tokens))
        
        # Print completion message
        if progress:
            print(" " * 100, end="\r")  # Clear progress line
            print("Augmentation complete.")

    except Exception as e:
        print(f"An error occurred during text augmentation: {str(e)}")
        return []

    return augmented_text

def load_text_file(file_path):
    """
    Load the contents of a text file.

    Parameters:
    - `file_path` (str): The path to the target input data.

    Returns:
    - `str`: The read text from the file.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"An error occurred during text file loading: {str(e)}")
        return ""

def augment_file_with_synonyms(file_path, augmentation_factor, probability, progress=True):
    """
    Augment a text file by replacing words with synonyms.

    Parameters:
    - `file_path` (str): The path to the target input data.
    - `augmentation_factor` (int): The number of times to augment the data.
    - `probability` (float): The probability of replacing a random word with its synonym.
    - `progress` (bool): Whether or not to print the current progress during augmentation.

    Returns:
    - `list`: A list of augmented text.
    """
    try:
        text = load_text_file(file_path)
        augmented_text = augment_text_with_synonyms(text, augmentation_factor, probability, progress)
        return augmented_text
    except Exception as e:
        print(f"An error occurred during text file augmentation: {str(e)}")
        return []


def insert_random_word(text, word):
    """
    Insert a random word into the input text.

    Parameters:
    - `text` (str): The input text for word insertion.
    - `word` (str): The word to be inserted into the text.

    Returns:
    - `str`: The text with the randomly inserted word.
    """
    try:
        words = nltk.word_tokenize(text)
        words.insert(random.randint(0, len(words)), word)
        modified_text = " ".join(words)
        return modified_text
    except Exception as e:
        print(f"An error occurred during word insertion: {str(e)}")
        return text


def delete_random_word(text):
    """
    Delete a random word from the input text.

    Parameters:
    - `text` (str): The input text for word deletion.

    Returns:
    - `str`: The text with a randomly deleted word.
    """
    try:
        words = nltk.word_tokenize(text)
        if len(words) > 1:
            words.pop(random.randint(0, len(words) - 1))
        modified_text = " ".join(words)
        return modified_text
    except Exception as e:
        print(f"An error occurred during word deletion: {str(e)}")
        return text


def insert_synonym(text, word):
    """
    Insert a synonym of the given word into the input text.

    Parameters:
    - `text` (str): The input text for synonym insertion.
    - `word` (str): The word for which a synonym will be inserted.

    Returns:
    - `str`: The text with a synonym of the word inserted.
    """
    try:
        synonym = replace_word_with_synonym(word)
        modified_text = text.replace(word, synonym)
        return modified_text
    except Exception as e:
        print(f"An error occurred during synonym insertion: {str(e)}")
        return text


def paraphrase(text):
    """
    Paraphrase the input text.

    Parameters:
    - `text` (str): The input text to be paraphrased.

    Returns:
    - `str`: The paraphrased text.
    """
    try:
        tokens = nltk.word_tokenize(text)
        tagged_tokens = nltk.pos_tag(tokens)
        paraphrased_tokens = [replace_word_with_synonym(token) if tag.startswith(("VB", "NN", "JJ")) else token for token, tag in tagged_tokens]
        paraphrased_text = " ".join(paraphrased_tokens)
        return paraphrased_text
    except Exception as e:
        print(f"An error occurred during paraphrasing: {str(e)}")
        return text

def flip_horizontal(image):
    """
    Flip the input image horizontally.

    Parameters:
    - `image` (PIL.Image.Image): The input image to be flipped.

    Returns:
    - `PIL.Image.Image`: The horizontally flipped image.
    """
    return image.transpose(Image.FLIP_LEFT_RIGHT)

def flip_vertical(image):
    """
    Flip the input image vertically.

    Parameters:
    - `image` (PIL.Image.Image): The input image to be flipped.

    Returns:
    - `PIL.Image.Image`: The vertically flipped image.
    """
    return image.transpose(Image.FLIP_TOP_BOTTOM)

def rotate(image, angle):
    """
    Rotate the input image by a specified angle.

    Parameters:
    - `image` (PIL.Image.Image): The input image to be rotated.
    - `angle` (float): The angle of rotation in degrees.

    Returns:
    - `PIL.Image.Image`: The rotated image.
    """
    rotated_image = image.rotate(angle, resample=Image.BICUBIC, expand=True)
    return crop(rotated_image, (0, 0, *image.size))

def random_rotation(image, max_angle=30):
    """
    Randomly rotate the input image by an angle within the specified range.

    Parameters:
    - `image` (PIL.Image.Image): The input image to be randomly rotated.
    - `max_angle` (float, optional): The maximum absolute angle of rotation in degrees. Default is 30.

    Returns:
    - `PIL.Image.Image`: The randomly rotated image.
    """
    angle = random.uniform(-max_angle, max_angle)
    return rotate(image, angle)

def resize(image, size):
    """
    Resize the input image to the specified size.

    Parameters:
    - `image` (PIL.Image.Image): The input image to be resized.
    - `size` (tuple): The new size in the format (width, height).

    Returns:
    - `PIL.Image.Image`: The resized image.
    """
    return image.resize(size, Image.BICUBIC)

def crop(image, box):
    """
    Crop the input image to the specified rectangular region.

    Parameters:
    - `image` (PIL.Image.Image): The input image to be cropped.
    - `box` (tuple): A tuple (left, upper, right, lower) specifying the region to crop.

    Returns:
    - `PIL.Image.Image`: The cropped image.
    """
    return image.crop(box)

def random_crop(image, size):
    """
    Randomly crop a region from the input image.

    Parameters:
    - `image` (PIL.Image.Image): The input image from which to extract the random crop.
    - `size` (tuple): The size of the output crop in the format (width, height).

    Returns:
    - `PIL.Image.Image`: The randomly cropped image region.
    """
    width, height = image.size
    left = random.randint(0, width - size[0])
    upper = random.randint(0, height - size[1])
    right = left + size[0]
    lower = upper + size[1]
    return crop(image, (left, upper, right, lower))

def perform_image_augmentation(
    source_dir,
    target_dir,
    flip_horizontal=False,
    flip_vertical=False,
    rotate=False,
    random_rotation=False,
    resize=False,
    crop=False,
    max_angle=30,
    target_size=(224, 224),
    crop_size=(150, 150)
):
    """
    Perform image augmentation on images in the source directory and its subdirectories.

    Parameters:
    - `source_dir` (str): The path to the source directory containing the images.
    - `target_dir` (str): The path to the target directory where augmented images will be saved.
    - `flip_horizontal` (bool): Perform horizontal flipping if True. Default is False.
    - `flip_vertical` (bool): Perform vertical flipping if True. Default is False.
    - `rotate` (bool): Perform rotation if True. Default is False.
    - `random_rotation` (bool): Perform random rotation if True. Default is False.
    - `resize` (bool): Perform resizing if True. Default is False.
    - `crop` (bool): Perform cropping if True. Default is False.
    - `max_angle` (float): The maximum absolute angle of rotation in degrees. Default is 30.
    - `target_size` (tuple): The target size for resizing in the format (width, height). Default is (224, 224).
    - `crop_size` (tuple): The size of the cropped region in the format (width, height). Default is (150, 150).
    """

    def augment_image(image_path):
        image = Image.open(image_path)

        if flip_horizontal and random.random() > 0.5:
            image = flip_horizontal(image)

        if flip_vertical and random.random() > 0.5:
            image = flip_vertical(image)

        if rotate and random.random() > 0.5:
            image = rotate(image, max_angle)

        if random_rotation and random.random() > 0.5:
            image = random_rotation(image, max_angle)

        if resize and random.random() > 0.5:
            image = resize(image, target_size)

        if crop and random.random() > 0.5:
            image = random_crop(image, crop_size)

        target_path = os.path.join(target_dir, os.path.relpath(image_path, source_dir))
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        image.save(target_path)

    num_images = 0
    num_directories = 0

    for root, _, files in os.walk(source_dir):
        num_directories += 1
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                num_images += 1
                image_path = os.path.join(root, file)
                augment_image(image_path)
                print(f"Processed {num_images} images in {num_directories} directories.", end='\r')

    print("\nImage augmentation completed successfully.")