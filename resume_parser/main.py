import json
from extractor import extract_text
from parser import parse_resume


# change filename here
FILE_PATH = "Hari_Om.pdf"


def main():
    print("📄 Reading:", FILE_PATH)

    text = extract_text(FILE_PATH)

    print("\n------ RAW TEXT ------\n")
    print(text)

    data = parse_resume(text)

    print("\n------ PARSED JSON ------\n")
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
