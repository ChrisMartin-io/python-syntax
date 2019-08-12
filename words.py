def print_upper_words(words, must_start_with):
  """This is a function that takes an array of words and prints them as uppercase"""
  """Print each word on sep line, uppercased, if starts with one of given

  >>> print_upper_words3(["eagle", "Edward", "Alfred", "zope"],
  ...                   must_start_with=["A", "E"])
  EDWARD
  ALFRED
  """
  for word in words:
    for letter in must_start_with:
      if word.startswith(letter):
        print(word.upper())
    

arr = ["hello", "hey", "goodbye", "yo", "yes"]
must_start_with = {"h", "y"}
print_upper_words(arr, must_start_with)