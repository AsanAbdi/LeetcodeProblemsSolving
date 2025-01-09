import os

paths = {
    "easy": "./easy",
    "medium": "./medium",
    "hard": "./hard"
}

def count_files(directory):
    if os.path.exists(directory):
        return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
    return 0

def update_progress():
    counts = {level: count_files(path) for level, path in paths.items()}

    readme_path = "README.md"
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        with open(readme_path, "w", encoding="utf-8") as file:
            for line in lines:
                if line.strip().startswith("| 🟢 Easy"):
                    file.write(f"| 🟢 Easy          | {counts['easy']}              |\n")
                elif line.strip().startswith("| 🟡 Medium"):
                    file.write(f"| 🟡 Medium        | {counts['medium']}              |\n")
                elif line.strip().startswith("| 🔴 Hard"):
                    file.write(f"| 🔴 Hard          | {counts['hard']}              |\n")
                else:
                    file.write(line)
        print("Progress table updated successfully!")
    else:
        print(f"README file not found at {readme_path}!")

if __name__ == "__main__":
    update_progress()