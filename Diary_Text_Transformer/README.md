# Diary Text Transformer

## 개요
Diary Text Transformer는 사용자가 작성한 일기를 다양한 페르소나에 맞춰 요약해주는 스트림릿 애플리케이션입니다.

## 설치 방법

### 1. 저장소 클론

``` sh
git clone <repository_url>
cd Diary_Text_Transformer
```

### 2. `run.sh` 스크립트 실행

``` sh
./run.sh
```

## 사용 방법

### 0. 설정
- LLM 설정 페이지에서 모델을 선택하고, API-KEY를 입력합니다.

### 1. 일기 입력
- "일기 입력" 탭에서 일기를 작성합니다.

### 2. 특성 설정
- "특성 설정" 탭에서 성별, 연령대, 발화 스타일을 선택합니다.
- "변환" 버튼을 클릭하여 일기를 변환합니다.

### 3. 결과 확인
- "결과창" 탭에서 변환된 텍스트를 확인합니다.


## 주요 파일 설명


- `app.py` : 스트림릿 애플리케이션의 메인 파일로, 세션 상태 초기화 및 페이지 전환을 담당합니다.
- `testPage.py` : 일기 입력, 특성 설정, 결과 확인을 위한 UI 페이지를 구성합니다.
- `llmSettingPage.py` : LLM 설정을 위한 UI 페이지를 구성합니다.
- `inference.py` : 모델의 API 호출에 관한 로직을 구성합니다.
- `enums.py` : 성별, 연령대, 발화 스타일, 모델 이름 등의 열거형을 정의합니다.
- `system_prompt/` : 모델별 시스템 프롬프트 텍스트 파일을 포함합니다.

## 요구 사항
- Python 3.12.0
- 필요한 패키지는 `requirements.txt`에 명시되어 있습니다.
- 이 어플리케이션은 streamlit을 통해 실행하도록 의도되었습니다.

## 기여 방법
1. 이슈를 생성하여 버그를 보고하거나 기능을 제안합니다.
2. 포크를 생성하고 기능을 추가한 후 풀 리퀘스트를 생성합니다.
