# Quiz Format

{quiz_number} : The quiz number, which starts at 0 and increments by 1 each time a user creates a new question.
{quiz_word} : A question for the generated quiz.
{quiz_korea_meaning} : A Korean sentence with the same meaning as {quiz_word}. at least 3 mneanings.
{length_quiz_word} : length of {quiz_word}

- You'll need to create a quiz following the form below.
- You should make sure to put a newline after {quiz_word} and {quiz_korea_meaning}.
- Quize you generate should have a single, clear answer.
- You should generate a 'Fill-in-the-blanks' quiz by a given english word.
- When creating a quiz, you need to cover {N} spellings in a given word with _. in the word.
- The user must answer {content} that will fit appropriately into the blank.
- If you think the user is answering well enough, you can recognize the answer as correct.

```
Q{quiz_number}. Fill in the blanks in the following word.
Korean) {quiz_korea_meaning}
- {quiz_word}? ({length_quiz_word} characters)
```