import os


def count_files_with_extension(directories, extension):
    count = 0
    for root, dirs, files in os.walk(directories):
        for file in files:
            if file.endswith(f'.{extension}'):
                count += 1  # Fixed incrementing
    return count


def main():
    ext = input("Please enter the extension (e.g., 'py'): ").strip()

    if not ext:
        print("No extension entered. Exiting.")
        return

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    if not os.path.exists(desktop_path):  # Fixed 'os.exists()' to 'os.path.exists()'
        print("Desktop folder not found.")
        return

    total_files = count_files_with_extension(desktop_path, ext)

    print(f"Total number of files with '.{ext}' extension: {total_files}")

if __name__ == "__main__":
    main()
