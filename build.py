#!/usr/bin/env python3
import yaml
import pystache

def build(data, template):
    '''
    data: resume data in a dictionary
    template: a LaTeX template string
    returns a string which is a LaTeX document
    '''
    return pystache.render(template, data)

if __name__ == '__main__':
    df = open('resume.yaml')
    #tf = open('resume.mustache.tex')
    tf = open('resume.mustache.markdown')

    data = yaml.safe_load(df)
    template = tf.read()

    print(build(data, template))

    df.close()
    tf.close()

