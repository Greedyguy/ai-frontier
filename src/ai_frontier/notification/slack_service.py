"""Slack notification service."""

import os
import logging
import requests
import json
from typing import Dict, List, Optional, Any
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__)

class SlackService:
    """Slack service for sending digest notifications."""

    def __init__(self):
        self.webhook_url = os.getenv('SLACK_WEBHOOK_URL', '')
        self.channel = os.getenv('SLACK_CHANNEL', '#ai-frontier')
        self.bot_name = os.getenv('SLACK_BOT_NAME', 'AI Frontier Bot')

    def send_digest_notification(self,
                               digest_file_path: Path,
                               digest_type: str = "daily",
                               digest_date: str = None) -> bool:
        """Send digest notification to Slack."""
        try:
            if not self.webhook_url:
                logger.warning("Slack webhook URL not configured. Skipping Slack notification.")
                return False

            # Read digest content for summary
            if not digest_file_path.exists():
                logger.error(f"Digest file not found: {digest_file_path}")
                return False

            with open(digest_file_path, 'r', encoding='utf-8') as f:
                digest_content = f.read()

            # Extract summary from digest
            summary = self._extract_summary_from_digest(digest_content)

            # Create Slack message
            message = self._create_slack_message(digest_type, digest_date, summary, digest_file_path)

            # Send to Slack
            response = requests.post(self.webhook_url, json=message, timeout=30)
            response.raise_for_status()

            logger.info(f"Sent {digest_type} digest notification to Slack")
            return True

        except Exception as e:
            logger.error(f"Error sending Slack notification: {e}")
            return False

    def _extract_summary_from_digest(self, digest_content: str) -> Dict[str, Any]:
        """Extract key information from digest content."""
        lines = digest_content.split('\n')
        summary = {
            "total_papers": 0,
            "main_topics": [],
            "notable_papers": [],
            "trend_keywords": []
        }

        # Extract basic statistics
        for line in lines:
            # Look for patterns like "**총 논문 수**: 611편" or "총 논문 수: 123개"
            if ("총 논문 수" in line or "전체 논문 수" in line) and ("편" in line or "개" in line):
                try:
                    # Extract number from various patterns
                    import re
                    # Look for patterns like "611편" or "123개"
                    number_match = re.search(r'(\d+)\s*편|(\d+)\s*개', line)
                    if number_match:
                        summary["total_papers"] = int(number_match.group(1) or number_match.group(2))
                        logger.info(f"Extracted total papers: {summary['total_papers']} from line: {line.strip()}")
                    else:
                        # Fallback: extract any number after colon
                        if ':' in line:
                            number_part = line.split(':')[1].strip()
                            numbers = ''.join(filter(str.isdigit, number_part))
                            if numbers:
                                summary["total_papers"] = int(numbers)
                                logger.info(f"Extracted total papers (fallback): {summary['total_papers']}")
                except Exception as e:
                    logger.warning(f"Failed to parse paper count from line: {line.strip()}, error: {e}")

            # Extract main topics from category distribution sections
            if line.strip().startswith('- **cs.'):
                try:
                    # Extract from lines like "- **cs.AI**: 284편 (46.5%)"
                    category_match = re.search(r'\*\*([^*]+)\*\*:', line)
                    if category_match:
                        category = category_match.group(1)
                        # Convert category codes to readable names
                        category_names = {
                            'cs.AI': '인공지능 (AI)',
                            'cs.LG': '기계학습 (ML)',
                            'cs.CV': '컴퓨터 비전 (CV)',
                            'cs.CL': '자연언어처리 (NLP)',
                            'cs.RO': '로보틱스 (Robotics)',
                            'cs.NI': '네트워킹 (Networking)',
                            'cs.CR': '암호학 및 보안 (Security)'
                        }
                        readable_name = category_names.get(category, category)
                        if readable_name not in summary["main_topics"]:
                            summary["main_topics"].append(readable_name)
                except Exception as e:
                    logger.warning(f"Failed to parse category from line: {line.strip()}, error: {e}")

            # Extract top trending keywords
            if line.strip().startswith('- **') and ('회' in line or 'times' in line):
                try:
                    # Extract from lines like "- **Large Language Model**: 166회"
                    keyword_match = re.search(r'\*\*([^*]+)\*\*:', line)
                    if keyword_match and len(summary["trend_keywords"]) < 5:
                        keyword = keyword_match.group(1)
                        summary["trend_keywords"].append(keyword)
                except Exception as e:
                    logger.warning(f"Failed to parse keyword from line: {line.strip()}, error: {e}")

        # Log extracted summary for debugging
        logger.info(f"Extracted summary: {summary}")
        return summary

    def _create_slack_message(self,
                            digest_type: str,
                            digest_date: str,
                            summary: Dict[str, Any],
                            digest_file_path: Path) -> Dict[str, Any]:
        """Create Slack message payload."""
        if not digest_date:
            digest_date = datetime.now().strftime("%Y-%m-%d")

        # Determine emoji and title based on digest type
        if digest_type == "daily":
            emoji = "🤖"
            title = f"일간 AI 논문 다이제스트 - {digest_date}"
        else:
            emoji = "📊"
            title = f"주간 AI 논문 다이제스트 - {digest_date}"

        # Build message blocks
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"{emoji} {title}"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*총 {summary['total_papers']}개의 논문*이 분석되었습니다."
                }
            }
        ]

        # Add main topics if available
        if summary["main_topics"]:
            topics_text = "\n".join([f"• {topic}" for topic in summary["main_topics"]])
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*주요 연구 분야:*\n{topics_text}"
                }
            })

        # Add trending keywords if available
        if summary["trend_keywords"]:
            keywords_text = "\n".join([f"• {keyword}" for keyword in summary["trend_keywords"][:5]])
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*주요 트렌드 키워드:*\n{keywords_text}"
                }
            })

        # Add notable papers if available
        if summary["notable_papers"]:
            papers_text = "\n".join([f"• {paper}" for paper in summary["notable_papers"]])
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*주목할 만한 논문:*\n{papers_text}"
                }
            })

        # Add file info
        blocks.extend([
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"📎 *다이제스트 파일:* `{digest_file_path.name}`\n생성 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "AI Frontier 자동 다이제스트 시스템에서 생성되었습니다."
                    }
                ]
            }
        ])

        message = {
            "channel": self.channel,
            "username": self.bot_name,
            "icon_emoji": ":robot_face:",
            "blocks": blocks
        }

        return message

    def send_custom_message(self, text: str, channel: str = None) -> bool:
        """Send custom message to Slack."""
        try:
            if not self.webhook_url:
                logger.warning("Slack webhook URL not configured.")
                return False

            message = {
                "channel": channel or self.channel,
                "username": self.bot_name,
                "icon_emoji": ":robot_face:",
                "text": text
            }

            response = requests.post(self.webhook_url, json=message, timeout=30)
            response.raise_for_status()

            logger.info("Sent custom message to Slack")
            return True

        except Exception as e:
            logger.error(f"Error sending custom Slack message: {e}")
            return False

    def test_connection(self) -> bool:
        """Test Slack webhook connection."""
        try:
            if not self.webhook_url:
                return False

            test_message = {
                "channel": self.channel,
                "username": self.bot_name,
                "icon_emoji": ":robot_face:",
                "text": "🧪 AI Frontier 연결 테스트입니다."
            }

            response = requests.post(self.webhook_url, json=test_message, timeout=30)
            response.raise_for_status()

            logger.info("Slack connection test successful")
            return True

        except Exception as e:
            logger.error(f"Slack connection test failed: {e}")
            return False