import os
import shutil
import threading
from tkinter import Tk, Label, Button, filedialog, StringVar, messagebox, BooleanVar, Checkbutton, Listbox, MULTIPLE, Entry
from tkinter.ttk import Progressbar 

def select_source_folder():
    folder = filedialog.askdirectory(mustexist=True)
    if folder:
        source_folder_var.set(folder)

def select_destination_folder():
    destination_folder = filedialog.askdirectory(mustexist=True)
    if destination_folder:
        destination_folder_var.set(destination_folder)

def extract_files():
    source_folder = source_folder_var.get()
    destination_folder = destination_folder_var.get()
    selected_types = list(file_type_listbox.curselection())
    delete_files = delete_var.get()

    # Get custom file types from the entry
    custom_types = custom_file_type_entry.get().strip().split(',')

    # Combine selected types and custom types
    selected_file_types = [file_type_listbox.get(i) for i in selected_types] + [file_type.strip() for file_type in custom_types if file_type.strip()]

    if not source_folder or not destination_folder:
        messagebox.showwarning("Missing Folders", "Please select source and destination folders.")
        return

    if not selected_file_types:
        messagebox.showwarning("No File Types", "Please select at least one file type to extract.")
        return

    total_files = count_files(source_folder, selected_file_types)
    if total_files == 0:
        messagebox.showinfo("No Files Found", "No files found matching the selected types in the source folder.")
        return

    threading.Thread(target=extract_images, args=(source_folder, destination_folder, selected_file_types, total_files, delete_files)).start()

def count_files(source_folder, selected_file_types):
    file_count = 0
    for root_dir, _, files in os.walk(source_folder):
        for file in files:
            if any(file.lower().endswith(file_type) for file_type in selected_file_types):
                file_count += 1
    return file_count

def extract_images(source_folder, destination_folder, selected_file_types, total_files, delete_files):
    file_counter = 0
    try:
        for root_dir, _, files in os.walk(source_folder):
            for file in files:
                if any(file.lower().endswith(file_type) for file_type in selected_file_types):
                    source_file_path = os.path.join(root_dir, file)
                    destination_file_path = os.path.join(destination_folder, file)

                    if os.path.exists(destination_file_path):
                        current_file.set(f"Replacing: {file}")
                    else:
                        current_file.set(f"Moving: {file}")

                    shutil.copy(source_file_path, destination_file_path)

                    if delete_files:
                        os.remove(source_file_path)

                    file_counter += 1

                    progress_bar["value"] = file_counter
                    progress_percentage.set(f"{(file_counter / total_files) * 100:.2f}%")
                    current_file_count.set(f"{file_counter}/{total_files} files moved")
                    root.update_idletasks()

        messagebox.showinfo("Success", f"Files extracted successfully! {file_counter} files copied.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    global root, source_folder_var, destination_folder_var, progress_bar, current_file, current_file_count, progress_percentage, delete_var, file_type_listbox, custom_file_type_entry

    root = Tk()
    root.title("File Extractor")
    screen_width = root.winfo_screenwidth() 
    screen_height = root.winfo_screenheight() 
    root.geometry(f"600x{screen_height}") 
    root.configure(bg="#f0f0f0")

    source_folder_var = StringVar()
    destination_folder_var = StringVar()
    current_file = StringVar(value="Waiting to start...")
    current_file_count = StringVar(value="0 files moved")
    progress_percentage = StringVar(value="0%")
    delete_var = BooleanVar()

    Label(root, text="Select the source folder:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=10)
    Button(root, text="Select Source Folder", command=select_source_folder,  bg="#007acc", fg="white", font=("Arial", 10)).pack()
    Label(root, textvariable=source_folder_var, bg="#f0f0f0", font=("Arial", 10)).pack(pady=5)

    # Destination folder selection
    Label(root, text="Select the destination folder:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=10)
    Button(root, text="Select Destination Folder", command=select_destination_folder, bg="#007acc", fg="white", font=("Arial", 10)).pack()
    Label(root, textvariable=destination_folder_var, bg="#f0f0f0", font=("Arial", 10)).pack(pady=5)

    # File type selection listbox
    Label(root, text="Select file types to extract:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=10)
    file_type_listbox = Listbox(root, selectmode=MULTIPLE, height=6)
    file_types = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".mp4", ".mov", ".heic"]
    for file_type in file_types:
        file_type_listbox.insert('end', file_type)
    file_type_listbox.pack(pady=5)

    # Entry for custom file types
    Label(root, text="Enter custom file types (comma-separated)(e.g., .mp4,.txt):", bg="#f0f0f0", font=("Arial", 12)).pack(pady=10)
    custom_file_type_entry = Entry(root, width=30)
    custom_file_type_entry.pack(pady=5)

    # Checkbox for deleting files after extraction
    Checkbutton(root, text="Delete files from source after moving", variable=delete_var, bg="#f0f0f0", font=("Arial", 12)).pack(pady=10)

    Button(root, text="Start Extraction", command=extract_files, bg="#007acc", fg="white", font=("Arial", 10)).pack(pady=20)

    # Progress bar and status labels
    progress_bar = Progressbar(root, mode='determinate')
    progress_bar.pack(pady=10, fill='x')

    Label(root, textvariable=progress_percentage, bg="#f0f0f0", font=("Arial", 10)).pack()
    Label(root, textvariable=current_file, bg="#f0f0f0", font=("Arial", 10)).pack(pady=5)
    Label(root, textvariable=current_file_count, bg="#f0f0f0", font=("Arial", 10)).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
