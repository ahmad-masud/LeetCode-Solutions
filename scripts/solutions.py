import os
import json

def solutions(root_dir, source_dir):
    solutions_data = []

    print(f"Root directory: {root_dir}")
    print(f"Source directory: {source_dir}")

    # Load overviews from overviews.json
    overview_file_path = os.path.join(root_dir, 'overviews.json')
    if not os.path.isfile(overview_file_path):
        print(f"Error: overviews.json file not found at {overview_file_path}")
        return

    with open(overview_file_path, 'r') as overview_file:
        overviews = json.load(overview_file)

    # Walk through each problem directory
    for problem_dir in sorted(os.listdir(source_dir)):
        problem_path = os.path.join(source_dir, problem_dir)
        print(f"Processing problem directory: {problem_path}")

        if os.path.isdir(problem_path) and problem_dir.isdigit():
            problem_id = int(problem_dir)
            problem_obj = {
                "id": problem_id,
                "video": None,
                "overview": overviews.get(str(problem_id), ""),
                "solutions": []
            }

            # Check for video file
            video_path = os.path.join(problem_path, 'video.txt')
            if os.path.isfile(video_path):
                print(f"Found video file at: {video_path}")
                with open(video_path, 'r') as video_file:
                    problem_obj["video"] = video_file.read().strip()

            # Collect solutions
            for solution_dir in sorted(os.listdir(problem_path)):
                solution_path = os.path.join(problem_path, solution_dir)
                print(f"Checking solution directory: {solution_path}")
                if os.path.isdir(solution_path):
                    code_path = os.path.join(solution_path, 'code.py')
                    info_path = os.path.join(solution_path, 'info.json')

                    if os.path.isfile(code_path) and os.path.isfile(info_path):
                        print(f"Found solution files at: {code_path} and {info_path}")
                        with open(code_path, 'r') as code_file:
                            code_content = code_file.read()

                        with open(info_path, 'r') as info_file:
                            info_data = json.load(info_file)

                        solution_obj = {
                            "title": info_data.get("title", ""),
                            "pythonCode": code_content,
                            "timeComplexity": info_data.get("timeComplexity", ""),
                            "spaceComplexity": info_data.get("spaceComplexity", "")
                        }

                        problem_obj["solutions"].append(solution_obj)

            # Add to main solutions list if any solutions exist
            if problem_obj["solutions"]:
                solutions_data.append(problem_obj)

    # Sort the solutions_data by the 'id' field
    solutions_data.sort(key=lambda x: x["id"])

    # Write data to solutions.json
    output_file = os.path.join(root_dir, 'solutions.json')
    with open(output_file, 'w') as json_file:
        json.dump(solutions_data, json_file, indent=4)

    print(f"solutions.json created at {output_file}")

# Set the root directory relative to the script's location
root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
source_directory = os.path.join(root_directory, 'solutions')
solutions(root_directory, source_directory)