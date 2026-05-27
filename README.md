# 한글 변환기 (Hangul Converter)

영문 모드인 줄 알고 타이핑했는데 한글이 입력된 경우,  
선택 후 단축키 하나로 즉시 영문으로 변환해주는 macOS 메뉴바 앱입니다.

## 예시

| 잘못 입력된 한글 | 변환 결과 |
|---|---|
| `안녕` | `dkssud` |
| `ㅗㄷㅣㅣㅐ` | `hello` |

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python3 -m src.main
```

## 단축키

**Cmd + Option + J**

변환할 한글 텍스트를 선택한 뒤 누르면 영문으로 변환됩니다.

## 요구사항

- macOS
- Python 3.8 이상

## 접근성 권한 설정 (최초 1회)

시스템 설정 → 개인정보 보호 및 보안 → 손쉬운 사용  
→ 터미널 & Visual Studio Code 허용 ✅