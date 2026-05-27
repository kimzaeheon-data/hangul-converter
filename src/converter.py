#초성, 종성, 중성 매핑
CHOSUNG_MAP = {
    'ㄱ':'r', 'ㄲ':'R', 'ㄴ':'s', 'ㄷ':'e', 'ㄸ':'E',
    'ㄹ':'f', 'ㅁ':'a', 'ㅂ':'q', 'ㅃ':'Q', 'ㅅ':'t',
    'ㅆ':'T', 'ㅇ':'d', 'ㅈ':'w', 'ㅉ':'W', 'ㅊ':'c',
    'ㅋ':'z', 'ㅌ':'x', 'ㅍ':'v', 'ㅎ':'g',
}

JUNGSUNG_MAP = {
    'ㅏ':'k', 'ㅐ':'o', 'ㅑ':'i', 'ㅒ':'O', 'ㅓ':'j',
    'ㅔ':'p', 'ㅕ':'u', 'ㅖ':'P', 'ㅗ':'h', 'ㅘ':'hk',
    'ㅙ':'ho', 'ㅚ':'hl', 'ㅛ':'y', 'ㅜ':'n', 'ㅝ':'nj',
    'ㅞ':'np', 'ㅟ':'nl', 'ㅠ':'b', 'ㅡ':'m', 'ㅢ':'ml',
    'ㅣ':'l'
}

JONGSUNG_MAP = {
    '': '',
    'ㄱ': 'r', 'ㄲ': 'R', 'ㄳ': 'rt', 'ㄴ': 's', 'ㄵ': 'sw',
    'ㄶ': 'sg', 'ㄷ': 'e', 'ㄹ': 'f', 'ㄺ': 'fr', 'ㄻ': 'fa',
    'ㄼ': 'fq', 'ㄽ': 'ft', 'ㄾ': 'fx', 'ㄿ': 'fv', 'ㅀ': 'fg',
    'ㅁ': 'a', 'ㅂ': 'q', 'ㅄ': 'qt', 'ㅅ': 't', 'ㅆ': 'T',
    'ㅇ': 'd', 'ㅈ': 'w', 'ㅊ': 'c', 'ㅋ': 'z', 'ㅌ': 'x',
    'ㅍ': 'v', 'ㅎ': 'g',
}

#초/중/종성 리스트
CHOSUNG_LIST = [
    'ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'
]

JUNGSUNG_LIST = [
    'ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ',
    'ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ'
]

JONGSUNG_LIST = [
    '','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ',
    'ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ',
    'ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'
]

SINGLE_JAMO_MAP = {**CHOSUNG_MAP, **JUNGSUNG_MAP}

def decompose(char):
    code = ord(char) - 0xAC00
    if code < 0 or code > 11171:
        return None #한글 아님
    
    cho = code // (21*28)
    jung = (code % (21*28)) // 28
    jong = code % 28

    return CHOSUNG_LIST[cho], JUNGSUNG_LIST[jung], JONGSUNG_LIST[jong]

def hangul_to_qwerty(text):
    result = []

    for char in text:
        code = ord(char)

        if 0xAC00 <= code <= 0xD7A3: #완성형 한글
            decomposed = decompose(char)
            cho, jung, jong = decomposed
            result.append(CHOSUNG_MAP[cho])
            result.append(JUNGSUNG_MAP[jung])
            if jong:
                result.append(JONGSUNG_MAP[jong])
        elif char in SINGLE_JAMO_MAP: #낱자 자모(ㄱ,ㄴ,ㅏ,ㅣ등)
            result.append(SINGLE_JAMO_MAP[char])
        else:
            result.append(char)

    return ''.join(result)