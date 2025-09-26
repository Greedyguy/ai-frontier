"""Webhook notification service for n8n and other automation tools."""

import os
import logging
import requests
import json
from typing import List, Dict, Any, Optional
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__)

class WebhookService:
    """Webhook service for external automation tools like n8n, Zapier."""

    def __init__(self):
        self.webhook_urls = self._parse_webhook_urls()

    def _parse_webhook_urls(self) -> List[str]:
        """Parse webhook URLs from environment variable."""
        webhook_env = os.getenv('NOTIFICATION_WEBHOOKS', '')
        if not webhook_env:
            return []

        # Support comma-separated URLs
        urls = [url.strip() for url in webhook_env.split(',') if url.strip()]
        return urls

    def send_digest_webhook(self,
                          digest_file_path: Path,
                          digest_type: str = "daily",
                          digest_date: str = None) -> bool:
        """Send digest notification via webhook."""
        try:
            if not self.webhook_urls:
                logger.info("No webhook URLs configured. Skipping webhook notifications.")
                return True

            if not digest_file_path.exists():
                logger.error(f"Digest file not found: {digest_file_path}")
                return False

            # Create webhook payload
            payload = self._create_webhook_payload(digest_file_path, digest_type, digest_date)

            # Send to all configured webhooks
            success_count = 0
            for webhook_url in self.webhook_urls:
                try:
                    response = requests.post(
                        webhook_url,
                        json=payload,
                        timeout=30,
                        headers={'Content-Type': 'application/json'}
                    )
                    response.raise_for_status()
                    success_count += 1
                    logger.info(f"Sent digest webhook to {webhook_url}")
                except Exception as e:
                    logger.error(f"Failed to send webhook to {webhook_url}: {e}")

            return success_count > 0

        except Exception as e:
            logger.error(f"Error sending digest webhooks: {e}")
            return False

    def _create_webhook_payload(self,
                              digest_file_path: Path,
                              digest_type: str,
                              digest_date: str) -> Dict[str, Any]:
        """Create webhook payload with digest information."""
        if not digest_date:
            digest_date = datetime.now().strftime("%Y-%m-%d")

        # Read digest content to extract metadata
        try:
            with open(digest_file_path, 'r', encoding='utf-8') as f:
                digest_content = f.read()
        except Exception as e:
            logger.warning(f"Could not read digest content: {e}")
            digest_content = ""

        # Extract basic statistics from digest
        stats = self._extract_digest_stats(digest_content)

        payload = {
            "event_type": "digest_generated",
            "digest_type": digest_type,
            "digest_date": digest_date,
            "timestamp": datetime.now().isoformat(),
            "file_info": {
                "filename": digest_file_path.name,
                "filepath": str(digest_file_path),
                "size_bytes": digest_file_path.stat().st_size if digest_file_path.exists() else 0
            },
            "statistics": stats,
            "source": "ai_frontier"
        }

        # Add digest content preview (first 500 chars)
        if digest_content:
            payload["content_preview"] = digest_content[:500] + "..." if len(digest_content) > 500 else digest_content

        return payload

    def _extract_digest_stats(self, content: str) -> Dict[str, Any]:
        """Extract statistical information from digest content."""
        stats = {
            "total_papers": 0,
            "categories": [],
            "word_count": len(content.split()) if content else 0,
            "char_count": len(content) if content else 0
        }

        if not content:
            return stats

        lines = content.split('\\n')

        # Extract total papers count
        for line in lines:
            if "총 논문 수:" in line or "전체 논문 수:" in line:
                try:
                    number_part = line.split(':')[1].strip()
                    stats["total_papers"] = int(''.join(filter(str.isdigit, number_part)))
                except:
                    pass

        # Extract categories mentioned
        for line in lines:
            if line.startswith("### ") or line.startswith("## "):
                category = line.replace("###", "").replace("##", "").strip()
                if category and category not in stats["categories"]:
                    stats["categories"].append(category)

        # Limit categories to avoid too much data
        stats["categories"] = stats["categories"][:10]

        return stats

    def send_paper_collection_webhook(self,
                                    collection_stats: Dict[str, Any]) -> bool:
        """Send webhook notification for paper collection completion."""
        try:
            if not self.webhook_urls:
                return True

            payload = {
                "event_type": "papers_collected",
                "timestamp": datetime.now().isoformat(),
                "statistics": collection_stats,
                "source": "ai_frontier"
            }

            success_count = 0
            for webhook_url in self.webhook_urls:
                try:
                    response = requests.post(
                        webhook_url,
                        json=payload,
                        timeout=30,
                        headers={'Content-Type': 'application/json'}
                    )
                    response.raise_for_status()
                    success_count += 1
                    logger.info(f"Sent collection webhook to {webhook_url}")
                except Exception as e:
                    logger.error(f"Failed to send collection webhook to {webhook_url}: {e}")

            return success_count > 0

        except Exception as e:
            logger.error(f"Error sending collection webhooks: {e}")
            return False

    def send_custom_webhook(self,
                          event_type: str,
                          data: Dict[str, Any]) -> bool:
        """Send custom webhook with arbitrary data."""
        try:
            if not self.webhook_urls:
                return True

            payload = {
                "event_type": event_type,
                "timestamp": datetime.now().isoformat(),
                "data": data,
                "source": "ai_frontier"
            }

            success_count = 0
            for webhook_url in self.webhook_urls:
                try:
                    response = requests.post(
                        webhook_url,
                        json=payload,
                        timeout=30,
                        headers={'Content-Type': 'application/json'}
                    )
                    response.raise_for_status()
                    success_count += 1
                    logger.info(f"Sent custom webhook ({event_type}) to {webhook_url}")
                except Exception as e:
                    logger.error(f"Failed to send custom webhook to {webhook_url}: {e}")

            return success_count > 0

        except Exception as e:
            logger.error(f"Error sending custom webhooks: {e}")
            return False

    def test_webhooks(self) -> Dict[str, bool]:
        """Test all configured webhook URLs."""
        results = {}

        if not self.webhook_urls:
            logger.info("No webhook URLs configured to test")
            return results

        test_payload = {
            "event_type": "test",
            "timestamp": datetime.now().isoformat(),
            "message": "AI Frontier webhook test",
            "source": "ai_frontier"
        }

        for webhook_url in self.webhook_urls:
            try:
                response = requests.post(
                    webhook_url,
                    json=test_payload,
                    timeout=30,
                    headers={'Content-Type': 'application/json'}
                )
                response.raise_for_status()
                results[webhook_url] = True
                logger.info(f"Webhook test successful: {webhook_url}")
            except Exception as e:
                results[webhook_url] = False
                logger.error(f"Webhook test failed for {webhook_url}: {e}")

        return results