import textwrap
import os

def switch_cleaner(language_code):
    filepath = '../vits/text/symbols.py'  # 수정하려는 파일의 경로
    cleaners = {
        'ja': 'japanese_cleaners2',
        'ko': 'korean_cleaners',
        'en': 'cjke_cleaners2',
        'zh': 'cjke_cleaners2'
        # 필요에 따라 추가 언어 코드를 여기에 입력하세요.
    }

    cleaner_strings = {  # 각각의 cleaner 문자열을 저장하는 딕셔너리
        'japanese_cleaners2': '''
_pad        = '_'
_punctuation = ',.!?-~…'
_letters = 'AEINOQUabdefghijkmnoprstuvwyzʃʧʦ↓↑ '
''',
        'korean_cleaners': '''
_pad        = '_'
_punctuation = ',.!?…~'
_letters = 'ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㄲㄸㅃㅆㅉㅏㅓㅗㅜㅡㅣㅐㅔ '
''',
        'cjke_cleaners2': '''
pad        = '_'
_punctuation = ',.!?-~…'
_letters = 'NQabdefghijklmnopstuvwxyzɑæʃʑçɯɪɔɛɹðəɫɥɸʊɾʒθβŋɦ⁼ʰ`^#*=ˈˌ→↓↑ '
'''
        # 필요에 따라 추가 언어 cleaner 문자열을 여기에 입력하세요.
    }

    selected_cleaner = cleaners.get(language_code)  # 입력된 언어 코드에 해당하는 cleaner를 선택
    if selected_cleaner is None:
        raise ValueError(f'Invalid language code: {language_code}')

    with open(filepath, 'r', encoding='utf-8') as file:
        filedata = file.read()

    # File content before the symbols and space id part
    start_marker = "'''# cjks_cleaners\n_pad        = '_'"
    start_index = filedata.index(start_marker)
    start_content = filedata[:start_index]

    # File content after the symbols and space id part
    end_marker = "# Export all symbols:"
    end_index = filedata.index(end_marker)
    end_content = filedata[end_index:]

    # Now we generate the new content for the cleaners
    new_cleaner_content = ""
    for cleaner, cleaner_string in cleaner_strings.items():
        if cleaner == selected_cleaner:  # 선택된 cleaner에 대해서는 주석 해제
            new_cleaner_content += textwrap.dedent(cleaner_string).strip() + '\n'
        else:  # 나머지 cleaner에 대해서는 주석 추가
            new_cleaner_content += textwrap.indent(cleaner_string, '# ').strip() + '\n'

    # Combine all the parts to generate the new file content
    new_file_content = start_content + new_cleaner_content + end_content

    # Finally we write the new content back to the file
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(new_file_content)

switch_cleaner('ja')