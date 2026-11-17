Mood Guesser

A small Python program that guesses whether a sentence is Happy or Sad. Run it with python main.py.

Level 3: Testing

Accuracy on the 5 practice sentences: 100 %

Which sentence went wrong (or was closest to going wrong), and why? "Today was a great day" was the closest. None of its words are in my happy or sad lists, so it was right only because I made ties go to Happy.
One change that would make my program better: Add more clue words like "great" and "lovely", or let the program learn the words from examples.
Learning questions
Total score of "good party today" and its mood: 2 + 1 + 0 = +3, so it is Happy.
Total score of "bad exam day" and its mood: -2 + 0 + -1 = -3, so it is Sad.
Why did "exam" get a score of 0, and is that good or bad? "exam" appears once in a Happy sentence and once in a Sad sentence, so the votes cancel out. This is good, because the word alone does not show any mood.
Why is "not good" labelled Happy by this method, and how could it be fixed? The method looks at each word alone, so it sees "good" (+2) and ignores "not". It could be fixed by treating "not good" as one pair of words, or by flipping the score of the word that comes after "not".
Bonus

I also wrote learn_scores and guess_mood_learned in main.py. They build word scores from train_data automatically and use them to guess the mood. Accuracy of the learned version on the practice sentences: ___ % (fill this in after running your program)

AI declaration

I used an AI tool: yes If yes, what I asked it: I asked for help understanding the task and for a sample solution, then I studied it and wrote the explanations in my own words.

Reflection

What was hardest, and what I learned that I did not know before: (Write 2-3 lines in your own words here. For example, what was hard about choosing only a few words, and what you learned about how a program can learn word scores from examples.)
