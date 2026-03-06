import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# 💡 현재 위치를 Python 탐색 경로에 강제로 추가 (경로 오류 원천 차단)
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
sys.path.append(os.path.join(BASE_DIR, "user-service"))
sys.path.append(os.path.join(BASE_DIR, "story-service"))
sys.path.append(os.path.join(BASE_DIR, "activity-service"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

try:
    application = get_wsgi_application()
except Exception as e:
    # 💡 에러 발생 시 로그에 상세히 남깁니다.
    print(f"WSGI Loading Error: {e}")
    raise e
