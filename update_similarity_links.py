#!/usr/bin/env python3
"""임시 스크립트: 모든 논문 파일에 유사도 링크 추가"""

import os
import sys
import re
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add src to path
sys.path.insert(0, '/Users/luke/work/SKT/edu/ai_frontier/src')

from ai_frontier.embeddings.similarity_manager import SimilarityManager
from ai_frontier.embeddings.service import get_embeddings_service
from ai_frontier.utils.obsidian_formatter import ObsidianFormatter

def extract_arxiv_id_from_filename(filename):
    """파일명에서 ArXiv ID 추출"""
    # 파일명에서 ArXiv ID 패턴 찾기 (예: 2509.13672v1)
    match = re.search(r'(\d{4}\.\d{4,5}(?:v\d+)?)', filename)
    if match:
        arxiv_id = match.group(1)
        # v1, v2 등 버전 제거
        if 'v' in arxiv_id:
            arxiv_id = arxiv_id.split('v')[0]
        return arxiv_id
    return None

def extract_arxiv_id_from_content(content):
    """파일 내용에서 ArXiv ID 추출"""
    # **ArXiv ID**: [2509.13672v1] 패턴 찾기
    match = re.search(r'\*\*ArXiv ID\*\*:\s*\[([^\]]+)\]', content)
    if match:
        arxiv_id = match.group(1)
        # v1, v2 등 버전 제거
        if 'v' in arxiv_id:
            arxiv_id = arxiv_id.split('v')[0]
        return arxiv_id
    return None

def has_similarity_links(content):
    """이미 유사도 링크가 있는지 확인"""
    return 'similar]' in content or '## 🔗 유사한 논문' in content

def add_similarity_links_to_file(filepath, similarity_manager):
    """개별 파일에 유사도 링크 추가"""
    try:
        # 파일 읽기
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 이미 유사도 링크가 있으면 스킵
        if has_similarity_links(content):
            return False, "Already has similarity links"

        # ArXiv ID 추출
        arxiv_id = extract_arxiv_id_from_content(content) or extract_arxiv_id_from_filename(filepath.name)

        if not arxiv_id:
            return False, "Could not extract ArXiv ID"

        # 유사도 링크 생성
        similar_links = similarity_manager.generate_obsidian_similarity_links(
            arxiv_id, max_links=5, min_similarity=0.6
        )

        if not similar_links:
            return False, "No similar papers found"

        # Links 섹션에 유사도 링크 추가
        links_pattern = r'(\*\*Links\*\*:\s*)(.*?)(\n\n|\n(?=##))'
        def add_similarity_to_links(match):
            prefix = match.group(1)
            existing_links = match.group(2).strip()
            suffix = match.group(3)

            # 유사도 링크를 기존 링크에 추가
            if existing_links:
                new_links = existing_links + ' ' + ' '.join(similar_links)
            else:
                new_links = ' '.join(similar_links)

            return f"{prefix}{new_links}{suffix}"

        # Links 섹션 업데이트
        new_content = re.sub(links_pattern, add_similarity_to_links, content, flags=re.DOTALL)

        # 유사한 논문 섹션 추가 (키워드 추출된 키워드 섹션 다음에)
        keywords_section_pattern = r'(## 🏷️ 추출된 키워드.*?\n\n)'
        similarity_section = "\n## 🔗 유사한 논문\n"

        for link in similar_links:
            # [[title|xx.x% similar]] 형태에서 title과 percentage 추출
            match = re.search(r'\[\[([^|]+)\|([^]]+)\]\]', link)
            if match:
                title = match.group(1)
                percentage = match.group(2)
                # 깔끔한 링크 형태로 변환
                clean_title = title.replace(' ', ' ')
                similarity_section += f"- [[{clean_title}]] ({percentage})\n"

        similarity_section += "\n"

        # 키워드 섹션 다음에 유사한 논문 섹션 추가
        def add_similarity_section(match):
            return match.group(1) + similarity_section

        new_content = re.sub(keywords_section_pattern, add_similarity_section, new_content, flags=re.DOTALL)

        # 파일 저장
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True, f"Added {len(similar_links)} similarity links"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """메인 함수"""
    print("🚀 유사도 링크 업데이트 스크립트 시작")

    try:
        # 서비스 초기화
        print("📊 임베딩 및 유사도 서비스 초기화...")
        embeddings_service = get_embeddings_service()
        similarity_manager = SimilarityManager(embeddings_service=embeddings_service)

        # 벡터 DB 상태 확인
        total_embeddings = len(similarity_manager.vector_db.arxiv_id_to_index)
        print(f"✅ 벡터 DB에 {total_embeddings}개 임베딩 로드됨")

        # 논문 파일 디렉토리
        papers_dir = Path('/Users/luke/work/SKT/edu/ai_frontier/reports/individual_papers')
        paper_files = list(papers_dir.glob('*.md'))

        print(f"📄 처리할 논문 파일: {len(paper_files)}개")

        # 각 파일 처리
        updated_count = 0
        skipped_count = 0
        error_count = 0

        for i, filepath in enumerate(paper_files, 1):
            print(f"[{i}/{len(paper_files)}] 처리 중: {filepath.name[:50]}...", end=' ')

            success, message = add_similarity_links_to_file(filepath, similarity_manager)

            if success:
                updated_count += 1
                print(f"✅ {message}")
            elif "Already has" in message:
                skipped_count += 1
                print(f"⏭️  {message}")
            else:
                error_count += 1
                print(f"❌ {message}")

        print(f"\n🎉 처리 완료!")
        print(f"  ✅ 업데이트됨: {updated_count}개")
        print(f"  ⏭️  이미 있음: {skipped_count}개")
        print(f"  ❌ 오류: {error_count}개")
        print(f"  📊 총 처리: {len(paper_files)}개")

    except Exception as e:
        print(f"❌ 스크립트 실행 오류: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())