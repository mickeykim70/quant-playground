# AI 트레이딩 시스템 (현대적 버전)

이 프로젝트는 최신 파이썬 라이브러리를 활용하여 AI 기반의 퀀트 트레이딩 시스템을 구축하는 과정을 담고 있습니다.

## 주요 기술 스택
- **yfinance**: 시장 데이터 수집
- **pandas**: 데이터 처리 및 시계열 분석
- **loguru**: 현대적인 로깅
- **Pydantic**: 런타임 설정 관리 및 데이터 검증

## 실행 방법
1. 의존성 패키지 설치:
   ```bash
   pip install -r requirements.txt
   ```

2. 시스템 실행:
   ```bash
   python main.py
   ```

## 프로젝트 구조 (1단계)
- `main.py`: 프로젝트 진입점 및 데이터 수집 예제
- `config.py`: 시스템 설정 관리 (Pydantic 활용)
- `requirements.txt`: 필요한 라이브러리 목록
