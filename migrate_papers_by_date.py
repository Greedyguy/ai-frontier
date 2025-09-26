#!/usr/bin/env python3
"""
기존 individual_papers 폴더의 논문들을 날짜별 폴더로 마이그레이션하는 스크립트
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime
from typing import Optional


def extract_date_from_filename(filename: str) -> Optional[str]:
    """
    파일명에서 날짜를 추출합니다.
    파일명 형태: 논문제목_YYYYMMDD.md
    """
    # 파일명 끝에서 _YYYYMMDD 패턴 찾기
    pattern = r'_(\d{8})\.md$'
    match = re.search(pattern, filename)

    if match:
        date_str = match.group(1)  # YYYYMMDD
        try:
            # 날짜 형식 검증
            date_obj = datetime.strptime(date_str, '%Y%m%d')
            return date_obj.strftime('%Y-%m-%d')  # YYYY-MM-DD 형태로 변환
        except ValueError:
            print(f"⚠️ 잘못된 날짜 형식: {filename}")
            return None

    # 대체 패턴 시도: _YYYYMMDD_추가텍스트.md
    pattern_alt = r'_(\d{8})_.*\.md$'
    match_alt = re.search(pattern_alt, filename)

    if match_alt:
        date_str = match_alt.group(1)
        try:
            date_obj = datetime.strptime(date_str, '%Y%m%d')
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            print(f"⚠️ 잘못된 날짜 형식 (대체 패턴): {filename}")
            return None

    print(f"⚠️ 날짜를 추출할 수 없는 파일명: {filename}")
    return None


def extract_date_from_content(file_path: Path) -> Optional[str]:
    """
    파일 내용에서 발행일을 추출합니다.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 발행일 패턴 찾기
        patterns = [
            r'발행일:\s*(\d{4}-\d{2}-\d{2})',
            r'Published:\s*(\d{4}-\d{2}-\d{2})',
            r'날짜:\s*(\d{4}-\d{2}-\d{2})',
            r'Date:\s*(\d{4}-\d{2}-\d{2})',
        ]

        for pattern in patterns:
            match = re.search(pattern, content)
            if match:
                return match.group(1)

        return None
    except Exception as e:
        print(f"⚠️ 파일 내용 읽기 실패 {file_path}: {e}")
        return None


def update_obsidian_links_in_file(file_path: Path, old_path: str, new_path: str):
    """
    파일 내의 옵시디언 링크를 업데이트합니다.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 상대 경로 링크 패턴 찾기 및 수정
        # [[논문제목_날짜]] -> [[날짜/논문제목_날짜]]
        pattern = r'\[\[([^|\]]+)\]\]'

        def replace_link(match):
            link_text = match.group(1)
            # 만약 링크가 논문 파일을 가리키는 경우 날짜 폴더 경로를 추가
            if re.search(r'_\d{8}$', link_text):  # _YYYYMMDD로 끝나는 경우
                date_from_link = extract_date_from_filename(link_text + '.md')
                if date_from_link:
                    return f'[[{date_from_link}/{link_text}]]'
            return match.group(0)  # 변경하지 않음

        updated_content = re.sub(pattern, replace_link, content)

        if content != updated_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"✅ 옵시디언 링크 업데이트: {file_path}")

    except Exception as e:
        print(f"⚠️ 옵시디언 링크 업데이트 실패 {file_path}: {e}")


def migrate_papers():
    """
    기존 논문들을 날짜별 폴더로 마이그레이션합니다.
    """
    # 기본 경로 설정
    base_dir = Path("reports/individual_papers")

    if not base_dir.exists():
        print(f"❌ 디렉토리가 존재하지 않습니다: {base_dir}")
        return

    print(f"📁 마이그레이션 시작: {base_dir}")

    # 백업 디렉토리 생성
    backup_dir = base_dir.parent / "individual_papers_backup"
    if not backup_dir.exists():
        print(f"📂 백업 디렉토리 생성: {backup_dir}")
        shutil.copytree(base_dir, backup_dir)

    moved_files = []
    failed_files = []

    # .md 파일들만 처리
    for file_path in base_dir.glob("*.md"):
        filename = file_path.name
        print(f"\n🔍 처리 중: {filename}")

        # 1. 파일명에서 날짜 추출 시도
        target_date = extract_date_from_filename(filename)

        # 2. 파일명에서 추출 실패 시, 파일 내용에서 추출 시도
        if not target_date:
            target_date = extract_date_from_content(file_path)

        # 3. 날짜 추출 실패
        if not target_date:
            print(f"❌ 날짜 추출 실패: {filename}")
            failed_files.append(filename)
            continue

        # 날짜별 폴더 생성
        date_dir = base_dir / target_date
        date_dir.mkdir(exist_ok=True)

        # 파일 이동
        new_file_path = date_dir / filename

        try:
            shutil.move(str(file_path), str(new_file_path))
            print(f"✅ 이동 완료: {filename} -> {target_date}/")
            moved_files.append((filename, target_date))

            # 옵시디언 링크 업데이트
            update_obsidian_links_in_file(new_file_path, filename, f"{target_date}/{filename}")

        except Exception as e:
            print(f"❌ 파일 이동 실패 {filename}: {e}")
            failed_files.append(filename)

    # 모든 날짜 폴더의 파일들에 대해 옵시디언 링크 업데이트
    print(f"\n🔗 모든 파일의 옵시디언 링크 업데이트 중...")
    for date_dir in base_dir.iterdir():
        if date_dir.is_dir():
            for file_path in date_dir.glob("*.md"):
                update_obsidian_links_in_file(file_path, "", "")

    # 결과 요약
    print(f"\n📊 마이그레이션 완료!")
    print(f"✅ 성공: {len(moved_files)}개 파일")
    print(f"❌ 실패: {len(failed_files)}개 파일")

    if moved_files:
        print(f"\n📁 날짜별 분류 결과:")
        date_counts = {}
        for filename, date in moved_files:
            date_counts[date] = date_counts.get(date, 0) + 1

        for date, count in sorted(date_counts.items()):
            print(f"  📅 {date}: {count}개 파일")

    if failed_files:
        print(f"\n⚠️ 처리 실패한 파일들:")
        for filename in failed_files:
            print(f"  - {filename}")

    print(f"\n💾 백업 위치: {backup_dir}")


if __name__ == "__main__":
    print("📄 AI Frontier 논문 파일 날짜별 마이그레이션 스크립트")
    print("=" * 60)

    # 자동 실행 (확인 메시지 스킵)
    migrate_papers()