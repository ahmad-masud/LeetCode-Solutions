import os
import json

def capitalize_title(title):
    # Capitalize the first letter of each word in the title
    return ' '.join(word.capitalize() for word in title.split())

def readme():
    # Load config/roadmap.json to extract topics
    script_dir = os.path.dirname(__file__)  # Directory of the current script
    roadmap_path = os.path.abspath(os.path.join(script_dir, '..', 'config', 'roadmap.json'))

    with open(roadmap_path) as f:
        roadmap = json.load(f)

    # Start creating README content
    readme_content = '# LeetCode solutions for [CompCode](https://compcode.tech)\n\n'

    # Iterate over each category in the roadmap
    for category in roadmap:
        # Add a header for each topic
        topic_name = capitalize_title(category.get('name', ''))
        readme_content += f'## {topic_name}\n\n'
        readme_content += '| LeetCode ID | Problem Name | Solutions | Video |\n'
        readme_content += '|-------------|--------------|-----------|-------|\n'

        for topic in category.get('data', []):  # Access the list of problems under 'data'
            leetcode_id = topic.get('ID', 'N/A')
            problem_name = topic.get('Title', 'N/A')
            problem_link = topic.get('Link', '#')
            problem_name_with_link = f'[{problem_name}]({problem_link})'  # Make the problem name clickable

            problem_path = f'src/{leetcode_id}'

            # Find all solutions for the problem
            solutions = []
            if os.path.isdir(problem_path):
                for solution_dir in sorted(os.listdir(problem_path)):
                    solution_dir_path = os.path.join(problem_path, solution_dir)
                    if os.path.isdir(solution_dir_path) and solution_dir.startswith('solution'):
                        code_path = os.path.join(solution_dir_path, 'code.py')
                        if os.path.isfile(code_path):
                            solutions.append(f'[✔️](src/{leetcode_id}/{solution_dir}/code.py)')

            solution_links = ' '.join(solutions) if solutions else '❌'

            # Check for video
            video_path = os.path.join(problem_path, 'video.txt')
            has_video = '❌'
            if os.path.isfile(video_path):
                with open(video_path) as vf:
                    video_url = vf.read().strip()
                    has_video = f'[✔️](https://www.youtube.com/embed/{video_url})'

            readme_content += f'| {leetcode_id} | {problem_name_with_link} | {solution_links} | {has_video} |\n'

    # Write the README content to a file
    output_path = os.path.abspath(os.path.join(script_dir, '..', 'README.md'))
    with open(output_path, 'w') as f:
        f.write(readme_content)

if __name__ == "__main__":
    readme()