def read_from_text_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as input_file:
            lines = input_file.readlines()
            # Remove newline characters and create a list
            data_list = [line.strip() for line in lines]
            return data_list
    except Exception as e:
        print(f"Error reading from {file_path}: {e}")
        return None

def save_to_py_as_list(data_list, output_file_path):
    try:
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write("# Data extracted from out2.txt\n")
            output_file.write("data_list = [\n")
            for item in data_list:
                output_file.write(f"    '{item}',\n")
            output_file.write("]\n")
        print(f"Data saved to {output_file_path}")
    except Exception as e:
        print(f"Error saving data to {output_file_path}: {e}")

def save_to_dictionary_file(data_list, output_file_path):
    try:
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write("# Data extracted from kw.txt\n")
            output_file.write("my_dict = {\n")
            for item in data_list:
                output_file.write(f"    '{item}': 0,\n")
            output_file.write("}\n")
        print(f"Data saved to {output_file_path}")
    except Exception as e:
        print(f"Error saving data to {output_file_path}: {e}")

if __name__ == "__main__":
    input_file_path = "kw.txt"  # Replace with the actual path to kw.txt
    extracted_data = read_from_text_file(input_file_path)
    if extracted_data:
        save_to_dictionary_file(extracted_data, "dict_out1.py")
