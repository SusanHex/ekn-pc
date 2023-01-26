

from sys import argv
from shlex import quote

def generate_rp_line(input_line: str, line_number = None) -> str:
    output_text = '    '
    if input_line.lstrip()[0] == '"' or input_line.lstrip()[0] == '[' and input_line.rstrip()[-1] == '"' or input_line.rstrip()[-1] == '[' and ':' not in input_line:
        output_text += f"\"{quote(input_line)}\""
    elif input_line[0] == '"' and ':' in input_line and input_line.rstrip()[-1] == '"':
        character_name[1:], dialogue_text[:-1] = input_line.strip().split(':', maxsplit=1)
        output_text += f"\"{character_name}\" \"{quote(dialogue_text)}\""
    else:
        output_text += f"# {input_line}"
    
    return output_text

def main():
    output_text = []
    with open(argv[1], 'r', encoding='utf-8') as story_file:
        for index, line in enumerate(story_file.readlines()):
            if line.strip():
                line_number = index+1
                output_line = generate_rp_line(line, line_number=line_number)
                print(output_line)
                print()
            

if __name__ == '__main__':
    main()
