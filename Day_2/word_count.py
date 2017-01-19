def words(a_string):
    words = a_string.replace('\t', ' ').split()
    dictn = {}
    for x in list(words):
      try:
        theWord = int(x)
      except ValueError:
        dictn[x] = words.count(x)
      else:
        dictn[int(x)] = words.count(x)

    return dictn