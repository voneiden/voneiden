import os 

def process():
  number = os.environ['NUMBER']
  body = os.environ['BODY']
  author = os.environ['AUTHOR']
  timestamp = os.environ['TIMESTAMP']
  
  if number == '1':
    readme = open('README.md', 'r').read()
    tok = readme.split('[//]: # (Comments)')
    readme = [
      tok[0],
      '[//]: # (Comments)\n',
      f'{body}\n\n-- {author} @ {timestamp}\n\n---\n',
      tok[1]
    ]
    with open('README.md', 'w') as f:
      f.write(''.join(readme))
      print("Updated OK")
  else:
    print("Not a comment")
  

if __name__ == '__main__':
  process()
