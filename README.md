# emsi-lepanto 
Implements levenshtein distance to find the best matching sentence to input query in Python3. I used Python 3.9 but any version of Python 3 should work fine (Python 2 likely won't). The included text file must also be in the same directory. To run/compile make sure you have Python3 installed on your machine (If you are using Ubuntu it may already be installed). The program will prompt you to input your best guess once entered it will output its prediction.


## Levenshtein Distance

Levenshtein distance also called edit distance is the measure of how many insertions, deletions and substitutions are required to change one string into another. I have modified it to better fit smaller inputs. This algorithm was chosen because of its speed and the document's sparsity. It likely does not produce the best output but it produces a fast output.
