#!/usr/bin/env python3
"""누락된 논문들의 임베딩 생성 및 벡터 DB 추가"""

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
from ai_frontier.arxiv.client import ArxivPaper
from datetime import datetime

def extract_paper_info_from_file(filepath):
    """논문 파일에서 필요한 정보 추출"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 제목 추출 (첫 번째 # 헤더)
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else ""

        # ArXiv ID 추출
        arxiv_match = re.search(r'\*\*ArXiv ID\*\*:\s*\[([^\]]+)\]', content)
        arxiv_id = arxiv_match.group(1) if arxiv_match else ""
        # v1, v2 등 버전 제거
        if 'v' in arxiv_id:
            arxiv_id = arxiv_id.split('v')[0]

        # Published 날짜 추출
        published_match = re.search(r'\*\*Published\*\*:\s*([^\n]+)', content)
        published_str = published_match.group(1) if published_match else "2025-09-17"

        # Category 추출
        category_match = re.search(r'\*\*Category\*\*:\s*([^\n]+)', content)
        category = category_match.group(1) if category_match else "cs.AI"

        # Abstract 추출 (원문)
        abstract_match = re.search(r'## 📄 Abstract \(원문\)\n\n(.*?)\n\n## ', content, re.DOTALL)
        abstract = abstract_match.group(1).strip() if abstract_match else ""

        # 요약 추출
        summary_match = re.search(r'## 📝 요약\n\n(.*?)\n\n## ', content, re.DOTALL)
        summary = summary_match.group(1).strip() if summary_match else ""

        # 핵심 포인트 추출
        key_points_match = re.search(r'## 🎯 주요 포인트\n\n(.*?)(?:\n\n---|$)', content, re.DOTALL)
        key_points_text = key_points_match.group(1).strip() if key_points_match else ""

        # 핵심 포인트를 리스트로 변환
        key_points = []
        if key_points_text:
            lines = key_points_text.split('\n')
            for line in lines:
                line = line.strip()
                if line and line.startswith('- '):
                    key_points.append(line[2:].strip())

        return {
            'arxiv_id': arxiv_id,
            'title': title,
            'abstract': abstract,
            'summary': summary,
            'key_points': key_points,
            'published': published_str,
            'category': category
        }

    except Exception as e:
        print(f"파일 읽기 오류 {filepath}: {e}")
        return None

def create_arxiv_paper_object(paper_info):
    """ArxivPaper 객체 생성"""
    from datetime import datetime

    # 날짜 파싱
    try:
        if paper_info['published']:
            published_date = datetime.strptime(paper_info['published'], '%Y-%m-%d')
        else:
            published_date = datetime.now()
    except:
        published_date = datetime.now()

    return ArxivPaper(
        arxiv_id=paper_info['arxiv_id'],
        title=paper_info['title'],
        authors=[],  # 기본값
        abstract=paper_info['abstract'],
        published=published_date,  # published 필드
        updated=None,  # 기본값
        pdf_url=f"http://arxiv.org/pdf/{paper_info['arxiv_id']}.pdf",  # PDF URL 생성
        category=paper_info['category']  # category 필드
    )

def main():
    """메인 함수"""
    print("🚀 누락된 논문 임베딩 생성 스크립트 시작")

    try:
        # 서비스 초기화
        print("📊 임베딩 및 유사도 서비스 초기화...")
        embeddings_service = get_embeddings_service()
        similarity_manager = SimilarityManager(embeddings_service=embeddings_service)

        # 현재 벡터 DB 상태 확인
        current_count = len(similarity_manager.vector_db.arxiv_id_to_index)
        print(f"✅ 현재 벡터 DB 임베딩 수: {current_count}")

        # 누락된 논문 파일들
        missing_files = [
            "/Users/luke/work/SKT/edu/ai_frontier/reports/individual_papers/Exploring Major Transitions in the Evolution of Bi_20250917.md",
            "/Users/luke/work/SKT/edu/ai_frontier/reports/individual_papers/HLSMAC_ A New StarCraft Multi-Agent Challenge for_20250916.md"
        ]

        print(f"📄 처리할 누락된 논문: {len(missing_files)}개")

        for i, filepath in enumerate(missing_files, 1):
            filename = Path(filepath).name
            print(f"[{i}/{len(missing_files)}] 처리 중: {filename[:50]}...")

            # 논문 정보 추출
            paper_info = extract_paper_info_from_file(filepath)
            if not paper_info:
                print(f"❌ 논문 정보 추출 실패: {filename}")
                continue

            arxiv_id = paper_info['arxiv_id']
            print(f"  📄 ArXiv ID: {arxiv_id}")
            print(f"  📝 제목: {paper_info['title'][:60]}...")

            # 이미 벡터 DB에 있는지 확인
            if arxiv_id in similarity_manager.vector_db.arxiv_id_to_index:
                print(f"  ⏭️  이미 벡터 DB에 존재함")
                continue

            # ArxivPaper 객체 생성
            paper = create_arxiv_paper_object(paper_info)

            # 임베딩 생성 및 저장
            try:
                print(f"  🔄 임베딩 생성 중...")
                paper_embedding = similarity_manager.process_paper(
                    paper,
                    paper_info['summary'],
                    paper_info['key_points']
                )
                print(f"  ✅ 임베딩 생성 및 저장 완료")

            except Exception as e:
                print(f"  ❌ 임베딩 생성 실패: {e}")
                continue

        # 최종 상태 확인
        final_count = len(similarity_manager.vector_db.arxiv_id_to_index)
        added_count = final_count - current_count

        print(f"\n🎉 처리 완료!")
        print(f"  📊 이전 임베딩 수: {current_count}")
        print(f"  📊 현재 임베딩 수: {final_count}")
        print(f"  ✅ 추가된 임베딩: {added_count}개")

    except Exception as e:
        print(f"❌ 스크립트 실행 오류: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())