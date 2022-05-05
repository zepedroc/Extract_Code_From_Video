def check_correct_result(generated_file, correct_file):
    correct_lines = 0
    correct_text = correct_file.readlines()
    generated_text = generated_file.readlines()

    for generated_line in generated_text:
        for line in correct_text:
            if line.strip() == generated_line.strip():
                correct_lines += 1
                break

    for line in correct_text:
        for generated_line in generated_text:
            if line.strip() == generated_line.strip():
                correct_lines += 1
                break        

    return f'Correctly Generated Lines: {round((correct_lines / (len(correct_text) + len(generated_text))) * 100, 2)}%'


"""

400 frames / skip < 100chars: Correctly Generated Lines: 37.50%
300 frames / skip < 150chars: Correctly Generated Lines: 44.71%
300 frames / skip < 100chars: Correctly Generated Lines: 44.94%
300 frames / skip < 50chars: Correctly Generated Lines: 42.55%
300 frames / skip < 0chars: Correctly Generated Lines: 43.48%
200 frames / skip < 100chars: Correctly Generated Lines: 38.46%
100 frames / skip < 100chars: Correctly Generated Lines: 33.75%


"""