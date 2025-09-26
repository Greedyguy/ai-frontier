#!/usr/bin/env python3
"""
기존 MD 파일들을 전체 제목으로 이름 변경하는 스크립트
"""

import os
import re
from pathlib import Path
from typing import Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def sanitize_filename(filename: str) -> str:
    """파일명에서 불법 문자 제거"""
    # 윈도우와 유닉스에서 금지된 문자들 제거
    illegal_chars = r'[<>:"/\\|?*\x00-\x1f]'
    filename = re.sub(illegal_chars, '_', filename)
    # 연속된 언더스코어 제거
    filename = re.sub(r'_+', '_', filename)
    # 앞뒤 공백과 점 제거
    filename = filename.strip(' .')
    # 빈 문자열인 경우 기본값 사용
    if not filename:
        filename = "untitled"
    return filename

def extract_title_from_md(file_path: Path) -> Optional[str]:
    """MD 파일에서 실제 제목 추출 (첫 번째 # 헤더)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 첫 번째 # 헤더 찾기
        title_match = re.search(r'^# ([^\n]+)', content, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()
        return None
    except Exception as e:
        logger.error(f"Error reading {file_path}: {e}")
        return None

def extract_date_from_filename(filename: str) -> Optional[str]:
    """기존 파일명에서 날짜 추출 (YYYYMMDD)"""
    match = re.search(r'_(\d{8})\.md$', filename)
    return match.group(1) if match else None

def rename_md_files(reports_dir: str = "reports/individual_papers"):
    """모든 MD 파일을 전체 제목으로 이름 변경"""
    reports_path = Path(reports_dir)

    if not reports_path.exists():
        logger.error(f"Reports directory {reports_path} does not exist")
        return

    md_files = list(reports_path.glob("*.md"))
    logger.info(f"Found {len(md_files)} MD files to process")

    success_count = 0
    error_count = 0
    skipped_count = 0

    for md_file in md_files:
        try:
            # 실제 제목 추출
            full_title = extract_title_from_md(md_file)
            if not full_title:
                logger.warning(f"Could not extract title from {md_file.name}")
                error_count += 1
                continue

            # 날짜 추출
            date_str = extract_date_from_filename(md_file.name)
            if not date_str:
                logger.warning(f"Could not extract date from {md_file.name}")
                error_count += 1
                continue

            # 새 파일명 생성
            safe_title = sanitize_filename(full_title)
            new_filename = f"{safe_title}_{date_str}.md"
            new_file_path = reports_path / new_filename

            # 이미 정확한 이름인 경우 건너뛰기
            if md_file.name == new_filename:
                logger.debug(f"File {md_file.name} already has correct name")
                skipped_count += 1
                continue

            # 새 파일명이 이미 존재하는 경우 처리
            if new_file_path.exists():
                logger.warning(f"Target file {new_filename} already exists, skipping {md_file.name}")
                error_count += 1
                continue

            # 파일 이름 변경
            md_file.rename(new_file_path)
            logger.info(f"Renamed: {md_file.name} -> {new_filename}")
            success_count += 1

        except Exception as e:
            logger.error(f"Error processing {md_file.name}: {e}")
            error_count += 1

    # 결과 요약
    logger.info("=== Rename Summary ===")
    logger.info(f"Total files processed: {len(md_files)}")
    logger.info(f"Successfully renamed: {success_count}")
    logger.info(f"Skipped (already correct): {skipped_count}")
    logger.info(f"Errors: {error_count}")

if __name__ == "__main__":
    rename_md_files()