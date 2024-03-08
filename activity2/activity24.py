import easyocr
from PIL import Image

def read_text_from_image(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)
    
    text = ''
    for detection in result:
        text += detection[1] + ' '

    return text.strip()

def solve_puzzle(puzzle_text):
    # for pulze like reversing text
    return puzzle_text[::-1]

def main():
    image_path = 'your_image_path.jpg'

    try:
        # Read text from the image using OCR
        puzzle_text = read_text_from_image(image_path)

        # Solve the puzzle
        solution = solve_puzzle(puzzle_text)
        print(f'Puzzle Text: {puzzle_text}')
        print(f'Solution: {solution}')

    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()
