This weekly puzzle involved finding a country name which contained a human body part in the consecutive letters, and after removing those consecutive letters, the remaining consecutive letters contained an animal body part.

To solve this challenge, I first extracted all the country names from a csv, removing those with spaces in the title.

Next, I had to figure out how to try look at every possible set of consecutive letters and the remaining consecutive letters when the previous are removed (as per the challenge explanation above). To do this, I realized I could simply iterate through all binary numbers up to the maximum where the number of digits equals the number of letters in the country name. For example, if the country name was "Canada", I would iterate from "000000" to "111111". Then, the trick was to create two words (thing1 and thing2 in the code) which were based on the location of the zeros and ones in the current binary number. So, if the current binary number iteration was "001011" then the first word, thing1, would equal "caa" and the second word would equal "nda". 

The final step was to simple check whether the two calculated words were in the dictionary using the enchant library. 

The solution "Thailand"--> "hand" and "tail" is found in the results. 
