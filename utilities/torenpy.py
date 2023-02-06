

from sys import argv
from re import compile, match
# Constant Regex Patterns

DESCRIPTOR_PATTERN = compile(r'^\[.+\]$')
DIALOGUE_PATTERN = compile(r'^\"[^\"].+\:.+\"$')
# https://www.renpy.org/doc/html/text.html
def escape_string(line: str, escape_spaces=False) -> str:
    output_string = line
    output_string = output_string.replace('\\', '\\\\')
    output_string = output_string.replace('"', r'\"')
    # output_string = output_string.replace("'", r"\'")
    if escape_spaces:
        output_string = output_string.replace(' ', '\ ')
    # output_string = output_string.replace('\n', '\\n')
    output_string = output_string.replace('%', r'\%')
    output_string = output_string.replace('[', r'[[').replace(']', ']]')
    return output_string


def generate_rp_line(raw_input_line: str, line_number = None) -> str:
    
    output_text = '    '
    
    if match(DESCRIPTOR_PATTERN, raw_input_line):
        output_text += f'"{escape_string(raw_input_line[1:-2])}"'
    elif match(DIALOGUE_PATTERN, raw_input_line):
        name, dialogue = raw_input_line[1:-2].split(':', maxsplit=1)
        if ' ' in name.strip() or '"' in name.strip():
            output_text += f'"{escape_string(name.strip())}" "{escape_string(dialogue.strip())}"'
        else:
            output_text += f'{escape_string(name.strip())} "{escape_string(dialogue.strip())}"'
    else:
        output_text += f"#@{line_number}: {raw_input_line}"
    return output_text

def main():
    output_text = []
    with open(argv[1], 'r', encoding='utf-8') as story_file:
        if len(argv) > 2:
            script_file_path = argv[2]
        else:
            script_file_path = 'script.txt'
        with open(script_file_path, 'w', encoding='utf-8') as script_file:
            script_file.write('label start:\n\n')
            for index, line in enumerate(story_file.readlines()):
                if line.strip():
                    line_number = index+1
                    output_line = generate_rp_line(line, line_number=line_number)
                    script_file.write(output_line + '\n\n')
                    print(output_line)
                    print()
            script_file.write('    return\n\n')
            

if __name__ == '__main__':
    main()
