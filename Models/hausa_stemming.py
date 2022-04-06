def hausa_stem(text):
  text_drop_r_n=[]
  for word in text:
    if len(word)>3:
      if word[-1]=='r':
        if word[-2]=='u' or word[-2]=='i':
          text_drop_r_n.append(word)
        else:
          l = len(word)
          removed = word[:l-1]
          text_drop_r_n.append(removed)
      elif word[-1]=='n':
        l = len(word)
        removed = word[:l-1]
        text_drop_r_n.append(removed)
      else:
        text_drop_r_n.append(word)
    else:
      text_drop_r_n.append(word)
  
  # drop suffix and prefix
  text_drop_affix=[]
  for word in text_drop_r_n:
    if word[:2]=='ba' or word[:2]=='ma':
      dropped=word[2:]
      if word[-2:]=='wa':
        removed=dropped[:-2]
        text_drop_affix.append(removed)
      elif word[-3:]=='iya' or word[-3:]=='uwa' or word[-3:]=='kku':
        removed=dropped[:-3]
        text_drop_affix.append(removed)
      elif word[-4:]=='anya':
        removed=dropped[:-4]
        text_drop_affix.append(removed)
      else:
        text_drop_affix.append(word)
      
    elif word[:3]=='mai' or word[:3]=='yan':
      dropped=word[3:]
      if word[-2:]=='wa':
        removed=dropped[:-2]
        text_drop_affix.append(removed)
      elif word[-3:]=='iya' or word[-3:]=='uwa' or word[-3:]=='kku':
        removed=dropped[:-3]
        text_drop_affix.append(removed)
      elif word[-4:]=='anya':
        removed=dropped[:-4]
        text_drop_affix.append(removed)
      else:
        text_drop_affix.append(word)
      


    else:
        text_drop_affix.append(word)

  #drop infix 
  text_drop_infix=[]
  for word in text_drop_affix:
    if word[-2:-1]==word[-4:-3] and word[-1:]=='i' and word[-3:-2]=='o':
      editted=word[:-3]+'a'
      text_drop_infix.append(editted)
    else:
      text_drop_infix.append(word)

  text="".join(text_drop_infix)

  return text
