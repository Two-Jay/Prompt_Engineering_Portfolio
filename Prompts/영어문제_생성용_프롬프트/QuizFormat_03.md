# Quiz Format

{quiz_words} : Words used to create the quiz, the user must place them in the proper order.
{dialogue} : A conversations utilized in quizzes. You need to show this to the user. {quiz_words} is hidden by an underscore.
{topic} : A central context of the conversation being created.

- You'll need to create a quiz following the form below.
- You should make sure to put a newline after {quiz_word} and {quiz_korea_meaning}.
- Quize you generate should have a single, clear answer.
- You should generate a 'Fill-in-the-blanks' quiz by a given english words.
- first, create a conversation between two people about {topic}. 
- {topic} will be presented when requesting to create a question. if not, {topic} would be everyday life. 
- the conversation should be easy and short, not complex to read for students.
- the conversation MUST contains {quiz_words}. But these words MUST hidden by underscore.
- then, you will present {quiz_words} below the conversation in random order.
- If the user correctly guessed the order in which the {quiz_words} would appear, you can consider it a correct answer.

```
Q{quiz_number}. List the words in the correct order.

Dialogue)
{dialogue_contents}

Words)
{quiz_words}
```


