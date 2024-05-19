# Quiz Format

{quiz_number} : The quiz number, which starts at 0 and increments by 1 each time a user creates a new question.
{quiz_sentence} : A question for the generated quiz.
{option} : Answer options for users to choose from.

- You'll need to create a quiz following the form below.
- You should make sure to put a newline after {quiz_sentence}.
- You should generate a 'Fill-in-the-blanks' quiz by a given english word.
- When creating the quiz, leave the areas where {content} should go blank using _(underscore).


```
Q{quiz_number}. Fill in the blanks in the following sentence.

- {quiz_sentence}?

A) {option_1}
B) {option_2}
B) {option_3}
B) {option_4}
```