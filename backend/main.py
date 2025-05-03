import grader


def main():
    # Example OCR text from a student's handwritten paper
    ocr_text = """
    Photosynthesis is the process plants use to make food using sunlight, water, and air.
    """

    # Example grading criteria from the teacher
    criteria = """
        
    """

    # Call your grading function!
    result = grader.grade_paper(ocr_text, criteria)

    print("=== Grade & Feedback ===")
    print(result)





if __name__ == "__main__":
    main()










