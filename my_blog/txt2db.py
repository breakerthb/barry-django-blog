#!/usr/bin/env python
#coding:utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_blog.settings")

from article.models import Article

def main():
    
    with open('input.txt', "r") as fileIn:
        for line in fileIn:
            line = line.strip()
            print(line)
            
            (_title, _tag, _content) = line.split("****", 2)
            
            # Article.objects.create(title=_title, category=_tag, content=_content)
            Article.objects.get_or_create(title=_title, category=_tag, content=_content)
    
if __name__ == "__main__":
    main()
    print('Done!')