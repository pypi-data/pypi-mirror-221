# MDNet: A Static Site Generator
MDNet is a simple static site generator that converts Markdown files into HTML files. It uses Jinja2 for templating and supports metadata in the form of YAML Front Matter.

## Features
- Converts Markdown files to HTML
- Supports YAML Front Matter for metadata
- Generates an index page with links to all posts
- Generates tag pages with links to all posts with a given tag
- Customizable with Jinja2 templates

## Installation
You can install MDNet with pip:

```bash
pip install mdnet
```
This will install MDNet and its dependencies, and create a command line script that you can use to run MDNet.

## Usage
After installing MDNet, you can use it like this:
```
mdnet input_dir output_dir post_template_path index_template_path tag_template_path
```
- `input_dir` is the directory containing the Markdown files.
- `output_dir` is the directory to output the HTML files to.
- `post_template_path` is the path to the HTML template for the posts.
- `index_template_path` is the path to the HTML template for the index page.
- `tag_template_path` is the path to the HTML template for the tag pages.

The templates should be Jinja2 templates.

The post template will be rendered with the following variables:

- 'title': The title of the post
- 'date': the date of the post
- 'content': the content of the post

The index template will be rendered with the following variables:

- 'posts': a list of dictionaries. Each dictionary contains the 'title', 'date', 'tldr', and 'file' (filename) of a post.
- 'tags': a list of all unique tags used in the posts.

The tag template will be rendered with the following variables:

- 'posts': a list of dictionaries. Each dictionary contains the 'title', 'date', 'tldr', and 'file' (filename) of a post with the given tag.
- 'tag': the name of the tag.

## Writing Posts
Posts should be written in Markdown and include YAML Front Matter. Front Matter is a block of YAML at the top of the file that is used for storing metadata about the file. Here's an example of a post:
```
---
title: My First Post
date: 2023-07-14
tldr: This is a short description of my post.
tags:
  - tag1
  - tag2
---
# My First Post

This is the content of my post. You can write anything you want here, in Markdown format.
```
In this example, the Front Matter is the part between the '---' lines. It includes a 'title', a 'date', a 'tldr' summary, and a list of 'tags'. These values will be used to populate the templates when generating the HTML files.

The rest of the file, after the second '---', is the content of the post. This should be written in Markdown, and it will be converted to HTML when generating the site.

## Assumptions
MDNet makes the following assumptions:
- All Markdown files are located directly in the input_dir directory. Subdirectories are not searched.
- All Markdown files have the '.md' extension.
- All Markdown files include YAML Front Matter with 'title', 'date', and 'tldr' fields. The 'tags' field is optional.
- The 'date' field in the Front Matter is in a format that can be sorted using the standard comparison operators, such as "YYYY-MM-DD".
- The 'tags' field in the Front Matter, if present, is a list of strings.
- The HTML templates are located at the paths specified by post_template_path, index_template_path, and tag_template_path.
- The HTML templates use the Jinja2 syntax and include placeholders for all the variables mentioned in the "Usage" section above.

## Example
Here's an example of how you might structure your project:
```
my_blog/
    templates/
        post.html
        index.html
        tag.html
    posts/
        post1.md
        post2.md
    output/
```
You can generate the site with this command:
```
mdnet posts output templates/post.html templates/index.html templates/tag.html
```
This will generate HTML files in the output directory.
