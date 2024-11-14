import os
import json

def package(root_dir):
    solutions_data = []

    # Walk through each problem directory
    for problem_dir in sorted(os.listdir(root_dir)):
        problem_path = os.path.join(root_dir, problem_dir)

        if os.path.isdir(problem_path) and problem_dir.isdigit():
            problem_obj = {
                "id": int(problem_dir),
                "video": None,
                "solutions": []
            }

            # Check for video file
            video_path = os.path.join(problem_path, 'video.txt')
            if os.path.isfile(video_path):
                with open(video_path, 'r') as video_file:
                    problem_obj["video"] = video_file.read().strip()

            # Collect solutions
            for solution_dir in os.listdir(problem_path):
                solution_path = os.path.join(problem_path, solution_dir)
                if os.path.isdir(solution_path):
                    code_path = os.path.join(solution_path, 'code.py')
                    info_path = os.path.join(solution_path, 'info.json')

                    if os.path.isfile(code_path) and os.path.isfile(info_path):
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

# Set the root directory to the location of your repository
root_directory = "."
package(root_directory)