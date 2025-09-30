import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from markdownify import markdownify

def get_all_wiki_page_urls(base_url: str) -> list[str]:
    """
    GitHub Wiki의 사이드바에서 모든 페이지 URL을 추출합니다.

    :param base_url: 기본 GitHub Wiki 페이지 URL
    :return: 모든 Wiki 페이지 URL의 리스트
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 사이드바에서 페이지 목록을 찾습니다.
        # 여러 CSS 선택자를 쉼표로 구분하여 한 번에 탐색합니다.
        # '#wiki-rightbar' (ID), '.wiki-pages' (클래스), '.wiki-custom-sidebar' (클래스) 중 하나를 찾습니다.
        sidebar = soup.select_one('#wiki-rightbar, .wiki-pages, .wiki-custom-sidebar')

        page_urls = {base_url} # 중복을 피하기 위해 set을 사용하고, 기본 URL을 추가합니다.
        if sidebar:
            links = sidebar.find_all('a', href=True)
            for link in links:
                href = link['href']
                # 상대 URL을 절대 URL로 변환합니다.
                full_url = urljoin('https://github.com', href)
                if base_url in full_url: # 현재 위키 저장소에 속한 링크인지 확인
                    page_urls.add(full_url)
        
        return sorted(list(page_urls))

    except requests.exceptions.RequestException as e:
        print(f"오류: 페이지 URL을 가져오는 중 문제가 발생했습니다 - {e}")
        return [base_url] # 실패 시 기본 URL만 반환

def extract_github_wiki_content(url: str) -> str:
    """
    GitHub Wiki 페이지에서 콘텐츠를 마크다운으로 추출합니다.

    :param url: GitHub Wiki 페이지의 URL
    :return: 추출된 마크다운 콘텐츠 또는 오류 메시지
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # HTTP 오류가 발생하면 예외를 발생시킵니다.

        soup = BeautifulSoup(response.content, 'html.parser')

        # GitHub Wiki의 실제 콘텐츠는 'markdown-body' 클래스를 가진 div 안에 있습니다.
        content_div = soup.find('div', class_='markdown-body')

        if content_div:
            # HTML을 마크다운으로 변환합니다. heading_style='ATX'는 # H1, ## H2 스타일을 사용합니다.
            markdown_text = markdownify(str(content_div), heading_style="ATX")
            return markdown_text.strip()
        else:
            return "오류: 콘텐츠 영역('markdown-body')을 찾을 수 없습니다. URL을 확인해주세요."

    except requests.exceptions.RequestException as e:
        return f"오류: 웹 페이지를 가져오는 중 문제가 발생했습니다 - {e}"

if __name__ == '__main__':
    # 예제: 크롤링할 GitHub Wiki 페이지 URL
    # 다른 GitHub Wiki 페이지 URL로 변경하여 테스트할 수 있습니다.
    wiki_url = "https://github.com/cline/cline/wiki"
    
    print(f"'{wiki_url}' 및 하위 위키 페이지의 모든 콘텐츠를 추출합니다...")
    
    all_urls = get_all_wiki_page_urls(wiki_url)
    print(f"총 {len(all_urls)}개의 페이지를 찾았습니다.")

    all_content = []
    for url in all_urls:
        print(f"크롤링 중: {url}")
        content = extract_github_wiki_content(url)
        if not content.startswith("오류:"):
            all_content.append(f"--- 페이지: {url} ---\n{content}")
        else:
            print(content)
    
    full_text = "\n\n".join(all_content)

    if full_text:
        print("\n--- 전체 추출된 콘텐츠 (일부) ---")
        # 내용이 길 수 있으므로 일부만 출력합니다.
        print(full_text[:2000])
        print("\n--- 추출 완료 ---")

        # 추출된 콘텐츠를 파일에 저장할 수도 있습니다.
        with open("wiki_content_all.md", "w", encoding="utf-8") as f:
            f.write(full_text)
        print("전체 콘텐츠가 'wiki_content_all.md' 파일에 저장되었습니다.")
    else:
        print("추출된 콘텐츠가 없습니다.")
