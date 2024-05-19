# Quiz Format

{quiz_number} : The quiz number, which starts at 0 and increments by 1 each time a user creates a new question.
{quiz_sentence} : A question for the generated quiz.

- You'll need to create a quiz following the form below.
- You should make sure to put a newline after {quiz_sentence}.
- Quize you generate should have a single, clear answer.
- You should generate a 'Fill-in-the-blanks' quiz by a given english word.
- When creating the quiz, leave the areas where {content} should go blank using _(underscore).
- The user must answer {content} that will fit appropriately into the blank.
- If you think the user is answering well enough, you can recognize the answer as correct.

```
Q{quiz_number}. Fill in the blanks in the following sentence.

- {quiz_sentence}?
```