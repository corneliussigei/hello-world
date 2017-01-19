def words(a_string):
    word_list = a_string.replace('\t', ' ').split()
    dictn = {}
    for x in list(word_list):
      try:
        theWord = int(x)
      except ValueError:
        dictn[x] = word_list.count(x)
      else:
        dictn[int(x)] = word_list.count(x)

    return dictn