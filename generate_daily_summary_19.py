#!/usr/bin/env python3
"""19일 daily 요약 생성 스크립트"""

import sys
import os
from pathlib import Path
from datetime import datetime
import re

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from ai_frontier.reporting.generator import ReportGenerator
from ai_frontier.main import ArxivReportingService

def generate_daily_summary_19():
    """19일 daily 요약 생성"""
    
    print("=== 2025-09-19 Daily 요약 생성 ===\n")
    
    try:
        # 19일 논문 파일들 찾기
        papers_dir = Path("reports/individual_papers")
        date_pattern = "_20250919.md"
        
        # 19일 논문 파일들 필터링
        papers_19 = []
        for md_file in papers_dir.glob("*.md"):
            if date_pattern in md_file.name:
                papers_19.append(md_file)
        
        print(f"📄 2025-09-19 논문 파일: {len(papers_19)}개")
        
        if not papers_19:
            print("❌ 19일 논문이 없습니다.")
            return False
        
        # 논문 정보 추출
        papers_info = []
        for paper_file in papers_19:
            try:
                with open(paper_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 제목 추출
                title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
                title = title_match.group(1) if title_match else paper_file.stem
                
                # ArXiv ID 추출
                arxiv_match = re.search(r'\*\*ArXiv ID\*\*: \[([^\]]+)\]', content)
                arxiv_id = arxiv_match.group(1) if arxiv_match else ""
                
                # 카테고리 추출
                category_match = re.search(r'\*\*Category\*\*: ([^\n]+)', content)
                category = category_match.group(1) if category_match else ""
                
                # 요약 추출
                summary_match = re.search(r'## 요약\n\n(.*?)(?=\n## |$)', content, re.DOTALL)
                summary = summary_match.group(1).strip() if summary_match else ""
                
                papers_info.append({
                    'title': title,
                    'arxiv_id': arxiv_id,
                    'category': category,
                    'summary': summary,
                    'file_path': paper_file
                })
                
            except Exception as e:
                print(f"파일 읽기 오류 {paper_file}: {e}")
        
        print(f"✅ 논문 정보 추출: {len(papers_info)}개")
        
        # 카테고리별 분류
        categories = {}
        for paper in papers_info:
            cat = paper['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(paper)
        
        print(f"📊 카테고리별 분류:")
        for cat, papers in categories.items():
            print(f"   - {cat}: {len(papers)}개")
        
        # Daily 요약 생성
        print(f"\n📝 Daily 요약 생성 중...")
        
        # 요약 템플릿 생성
        summary_content = f"""# 2025-09-19 AI Frontier Daily Digest

## 📊 수집 현황
- **총 논문 수**: {len(papers_info)}개
- **수집 일자**: 2025년 9월 19일
- **카테고리 수**: {len(categories)}개

## 🏷️ 카테고리별 논문 분포
"""
        
        for cat, papers in sorted(categories.items()):
            summary_content += f"- **{cat}**: {len(papers)}개\n"
        
        summary_content += f"""

## 🔥 주요 논문 하이라이트

### Computer Vision (cs.CV)
"""
        
        # cs.CV 논문들 추가
        if 'cs.CV' in categories:
            cv_papers = categories['cs.CV'][:5]  # 상위 5개
            for paper in cv_papers:
                summary_content += f"- **{paper['title']}**\n"
                summary_content += f"  - ArXiv ID: {paper['arxiv_id']}\n"
                if paper['summary']:
                    summary_content += f"  - 요약: {paper['summary'][:200]}...\n"
                summary_content += "\n"
        
        summary_content += f"""
### Artificial Intelligence (cs.AI)
"""
        
        # cs.AI 논문들 추가
        if 'cs.AI' in categories:
            ai_papers = categories['cs.AI'][:5]  # 상위 5개
            for paper in ai_papers:
                summary_content += f"- **{paper['title']}**\n"
                summary_content += f"  - ArXiv ID: {paper['arxiv_id']}\n"
                if paper['summary']:
                    summary_content += f"  - 요약: {paper['summary'][:200]}...\n"
                summary_content += "\n"
        
        summary_content += f"""
### Machine Learning (cs.LG)
"""
        
        # cs.LG 논문들 추가
        if 'cs.LG' in categories:
            lg_papers = categories['cs.LG'][:5]  # 상위 5개
            for paper in lg_papers:
                summary_content += f"- **{paper['title']}**\n"
                summary_content += f"  - ArXiv ID: {paper['arxiv_id']}\n"
                if paper['summary']:
                    summary_content += f"  - 요약: {paper['summary'][:200]}...\n"
                summary_content += "\n"
        
        summary_content += f"""
## 📈 연구 동향 분석

### 주요 키워드
- **Large Language Models (LLM)**: {len([p for p in papers_info if 'LLM' in p['title'] or 'Language Model' in p['title']])}개 논문
- **Computer Vision**: {len([p for p in papers_info if 'Vision' in p['title'] or 'Image' in p['title']])}개 논문
- **Reinforcement Learning**: {len([p for p in papers_info if 'Reinforcement' in p['title'] or 'RL' in p['title']])}개 논문
- **Multi-Agent Systems**: {len([p for p in papers_info if 'Multi-Agent' in p['title'] or 'Agent' in p['title']])}개 논문

### 연구 트렌드
1. **AI 에이전트 및 멀티에이전트 시스템**의 지속적인 발전
2. **컴퓨터 비전과 자연어 처리의 융합** 연구 증가
3. **강화학습의 실용적 응용** 확대
4. **대규모 언어 모델의 최적화 및 효율성** 개선

## 🔗 관련 링크
- [전체 논문 목록](reports/individual_papers/)
- [카테고리별 분류](reports/categories/)
- [키워드별 분류](reports/keywords/)

---
*이 요약은 AI Frontier 시스템에 의해 자동 생성되었습니다.*
*생성 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
        
        # 요약 파일 저장
        output_file = Path("reports/digests/daily_digest_20250919.md")
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        
        print(f"✅ Daily 요약 생성 완료!")
        print(f"📁 저장 위치: {output_file}")
        print(f"📄 파일 크기: {len(summary_content)} 문자")
        
        return True
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = generate_daily_summary_19()
    if success:
        print(f"\n🎉 2025-09-19 Daily 요약이 성공적으로 생성되었습니다!")
    else:
        print(f"\n❌ Daily 요약 생성에 실패했습니다.")


