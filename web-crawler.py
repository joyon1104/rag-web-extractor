import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from markdownify import markdownify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_all_doc_page_paths(base_url: str) -> list[str]:
    """
    continue.dev 문서의 sidebar-content에서 모든 문서 링크를 추출합니다.
    버튼 클릭으로 동적 생성되는 링크도 포함합니다.
    
    :param base_url: 기본 문서 페이지 URL
    :return: 모든 문서 페이지 경로의 리스트
    """
    try:
        # Chrome 웹드라이버 설정
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # 헤드리스 모드
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        # 페이지 로드
        driver.get(base_url)
        time.sleep(2)  # 초기 로딩 대기
        
        page_paths = set()
        
        # sidebar-content 찾기
        sidebar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sidebar-content"))
        )
        
        # 모든 버튼 찾아서 클릭
        buttons = sidebar.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            try:
                driver.execute_script("arguments[0].click();", button)
                time.sleep(0.5)  # 동적 컨텐츠 로딩 대기
            except:
                continue
        
        # 모든 링크 수집 (동적으로 생성된 링크 포함)
        links = sidebar.find_elements(By.TAG_NAME, "a")
        for link in links:
            try:
                href = link.get_attribute('href')
                if href and href.startswith(base_url):
                    path = '/' + href.split('/', 3)[3]
                    clean_path = path.split('#')[0]
                    if clean_path:
                        page_paths.add(clean_path)
            except:
                continue
        
        driver.quit()
        return sorted(list(page_paths))

    except Exception as e:
        print(f"오류: 페이지 URL을 가져오는 중 문제가 발생했습니다 - {e}")
        return [] # 실패 시 빈 리스트 반환

def extract_docs_content(url: str) -> str:
    """
    문서 페이지에서 메인 콘텐츠를 마크다운으로 추출합니다.

    :param url: 크롤링할 페이지의 URL
    :return: 추출된 마크다운 콘텐츠 또는 오류 메시지
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # continue.dev 문서의 메인 콘텐츠는 id가 'content'인 div 안에 있습니다.
        content_div = soup.find('div', id='content')

        if content_div:
            # HTML을 마크다운으로 변환합니다.
            markdown_text = markdownify(str(content_div), heading_style="ATX")
            return markdown_text.strip()
        else:
            return f"오류: 콘텐츠 영역('content')을 찾을 수 없습니다. URL: {url}"

    except requests.exceptions.RequestException as e:
        return f"오류: {url} 페이지를 가져오는 중 문제가 발생했습니다 - {e}"

if __name__ == '__main__':
    base_url = "https://docs.continue.dev/"
    
    # 사이드바에서 크롤링할 페이지의 경로 목록을 동적으로 가져옵니다.
    print("사이드바에서 페이지 목록을 가져오는 중...")
    target_paths = get_all_doc_page_paths(base_url)

    if not target_paths:
        print("크롤링할 페이지를 찾지 못했습니다. 스크립트를 종료합니다.")
        exit()

    # 전체 URL 생성
    target_urls = [urljoin(base_url, path) for path in target_paths]
    
    print(f"총 {len(target_urls)}개의 페이지를 크롤링합니다...")

    all_content = []
    for url in target_urls:
        print(f"크롤링 중: {url}")
        content = extract_docs_content(url)
        if not content.startswith("오류:"):
            # 각 페이지 콘텐츠 앞에 출처 URL을 마크다운 제목으로 명시
            all_content.append(f"# Source: {url}\n\n{content}")
        else:
            print(content)
    
    full_text = "\n\n---\n\n".join(all_content)

    if full_text:
        print("\n--- 전체 추출된 콘텐츠 (일부) ---")
        print(full_text[:2000])
        print("\n--- 추출 완료 ---")

        # 추출된 콘텐츠를 파일에 저장
        with open("continue_dev_docs.md", "w", encoding="utf-8") as f:
            f.write(full_text)
        print("전체 콘텐츠가 'continue_dev_docs.md' 파일에 저장되었습니다.")
    else:
        print("추출된 콘텐츠가 없습니다.")