import os 

def process():
  title = os.environ['TITLE']
  body = os.environ['BODY']
  author = os.environ['AUTHOR']
  timestamp = os.environ['TIMESTAMP']
  
  if title == 'Comment':
    readme = open('README.md', 'r').read()
    tok = readme.split('[//]: # (Comments)')
    readme = [
      tok[0],
      '[//]: # (Comments)',
      f'{body}\n\n-- {author} @ {timestamp}\n---\n',
      tok[1]
    ]
    with open('README.md', 'w') as f:
      f.write(''.join(readme))
      print("Updated OK")
  else:
    print("Not a comment")
  

if __name__ == '__main__':
  process()
