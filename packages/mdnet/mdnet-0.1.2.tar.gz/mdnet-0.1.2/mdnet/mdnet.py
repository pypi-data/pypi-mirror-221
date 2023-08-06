import argparse
import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def convert_md_to_html(md):
    return markdown.markdown(md)

def get_template(template_path):
    template_dir = template_path.parent
    env = Environment(loader=FileSystemLoader(str(template_dir)))
    return env.get_template(template_path.name)

def render_template(template_path, metadata, content):
    template = get_template(template_path)
    return template.render(title=metadata['title'], date=metadata['date'], content=content)

def render_index(template_path, posts, tags):
    template = get_template(template_path)
    return template.render(posts=posts, tags=tags)

def render_tag_page(template_path, metadata):
    template = get_template(template_path)
    return template.render(posts=metadata['posts'], tag=metadata['tag'])

def generate_site(input_dir, output_dir, post_path, index_path, tag_path):
    posts_dir = output_dir / 'posts'
    posts_dir.mkdir(parents=True, exist_ok=True)

    posts = []
    tags = {}
    for md_file in Path(input_dir).iterdir():
        if md_file.suffix == ".md":
            post = frontmatter.load(md_file)
            html_file = posts_dir / (post.metadata['title'] + ".html")
            html_file.write_text(render_template(post_path, post.metadata, convert_md_to_html(post.content)))
            post_data = {
                'title' : post.metadata['title'], 
                'date' : post.metadata['date'],
                'tldr' : post.metadata['tldr'],
                'file' : 'posts/' + html_file.name,  # For links on the index page
                'tag_file' : '../posts/' + html_file.name  # For links on tag pages
            }

            posts.append(post_data)
            for tag in post.metadata.get('tags', []):
                if tag not in tags:
                    tags[tag] = []
                tags[tag].append(post_data)

    # Sort posts by date in descending order
    posts.sort(key=lambda post: post['date'], reverse=True)
    
    tags_dir = output_dir / 'tags'
    tags_dir.mkdir(parents=True, exist_ok=True)
    for tag, tag_posts in tags.items():
        (tags_dir / f'{tag}.html').write_text(render_tag_page(tag_path, {'posts': tag_posts, 'tag': tag}))

    (output_dir / 'index.html').write_text(render_index(index_path, posts, tags))

def main():
    parser = argparse.ArgumentParser(description="Generate a static site from Markdown files.")
    parser.add_argument("input_dir", help="The directory containing the Markdown files.")
    parser.add_argument("output_dir", help="The directory to output the HTML files to.")
    parser.add_argument("post_template_path", help="The path to the post HTML template.")
    parser.add_argument("index_template_path", help="The path to the index HTML template.")
    parser.add_argument("tag_template_path", help="The path to the tag page HTML template")
    args = parser.parse_args()

    generate_site(Path(args.input_dir), Path(args.output_dir), Path(args.post_template_path), Path(args.index_template_path), Path(args.tag_template_path))
    

if __name__ == "__main__":
    main()
