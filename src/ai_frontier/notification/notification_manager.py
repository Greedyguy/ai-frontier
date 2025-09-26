"""Notification manager for coordinating all notification services."""

import logging
import os
from typing import Dict, List, Optional, Any
from pathlib import Path
from datetime import datetime

from .email_service import EmailService
from .slack_service import SlackService
from .webhook_service import WebhookService
from .keyword_subscription_manager import get_keyword_subscription_manager

logger = logging.getLogger(__name__)

class NotificationManager:
    """Central manager for all notification services."""

    def __init__(self):
        self.email_service = EmailService()
        self.slack_service = SlackService()
        self.webhook_service = WebhookService()
        self.keyword_subscription_manager = get_keyword_subscription_manager()

        # Auto-send settings from environment
        self.auto_send_email = os.getenv('AUTO_SEND_EMAIL', 'false').lower() == 'true'
        self.auto_send_slack = os.getenv('AUTO_SEND_SLACK', 'false').lower() == 'true'

    def send_digest_notifications(self,
                                digest_file_path: Path,
                                digest_type: str = "daily",
                                digest_date: str = None,
                                send_email: bool = None,
                                send_slack: bool = None,
                                send_webhooks: bool = True,
                                custom_email_recipients: List[str] = None) -> Dict[str, bool]:
        """Send digest notifications through all configured channels."""

        results = {
            "email": False,
            "slack": False,
            "webhooks": False
        }

        if not digest_file_path.exists():
            logger.error(f"Digest file not found: {digest_file_path}")
            return results

        # Determine which services to use
        should_send_email = send_email if send_email is not None else self.auto_send_email
        should_send_slack = send_slack if send_slack is not None else self.auto_send_slack

        logger.info(f"Sending {digest_type} digest notifications for {digest_date or 'today'}")

        # Send email notifications
        if should_send_email:
            try:
                success = self.email_service.send_digest_email(
                    digest_file_path=digest_file_path,
                    digest_type=digest_type,
                    digest_date=digest_date,
                    custom_recipients=custom_email_recipients
                )
                results["email"] = success
                if success:
                    logger.info("Email digest notification sent successfully")
                else:
                    logger.warning("Email digest notification failed")
            except Exception as e:
                logger.error(f"Error sending email digest: {e}")

        # Send Slack notifications
        if should_send_slack:
            try:
                success = self.slack_service.send_digest_notification(
                    digest_file_path=digest_file_path,
                    digest_type=digest_type,
                    digest_date=digest_date
                )
                results["slack"] = success
                if success:
                    logger.info("Slack digest notification sent successfully")
                else:
                    logger.warning("Slack digest notification failed")
            except Exception as e:
                logger.error(f"Error sending Slack digest: {e}")

        # Send webhook notifications (for n8n, Zapier, etc.)
        if send_webhooks:
            try:
                success = self.webhook_service.send_digest_webhook(
                    digest_file_path=digest_file_path,
                    digest_type=digest_type,
                    digest_date=digest_date
                )
                results["webhooks"] = success
                if success:
                    logger.info("Webhook digest notifications sent successfully")
                else:
                    logger.warning("Webhook digest notifications failed")
            except Exception as e:
                logger.error(f"Error sending webhook digest: {e}")

        # Send personalized digests to keyword subscribers
        if should_send_email:
            try:
                keyword_results = self.send_keyword_based_digests(
                    digest_type=digest_type,
                    digest_date=digest_date
                )
                logger.info(f"Keyword-based digest notifications: {keyword_results}")
            except Exception as e:
                logger.error(f"Error sending keyword-based digests: {e}")

        return results

    def send_paper_collection_notification(self,
                                         collection_stats: Dict[str, Any]) -> Dict[str, bool]:
        """Send notification when paper collection is completed."""

        results = {
            "webhooks": False
        }

        # Currently only sending webhook notifications for paper collection
        # Email/Slack notifications for paper collection can be added if needed

        try:
            success = self.webhook_service.send_paper_collection_webhook(collection_stats)
            results["webhooks"] = success
            if success:
                logger.info("Paper collection webhook notifications sent successfully")
        except Exception as e:
            logger.error(f"Error sending paper collection webhooks: {e}")

        return results

    def test_all_connections(self) -> Dict[str, bool]:
        """Test all notification service connections."""

        results = {
            "email": False,
            "slack": False,
            "webhooks": {}
        }

        # Test email connection
        try:
            results["email"] = self.email_service.test_connection()
        except Exception as e:
            logger.error(f"Email connection test error: {e}")

        # Test Slack connection
        try:
            results["slack"] = self.slack_service.test_connection()
        except Exception as e:
            logger.error(f"Slack connection test error: {e}")

        # Test webhook connections
        try:
            results["webhooks"] = self.webhook_service.test_webhooks()
        except Exception as e:
            logger.error(f"Webhook connection test error: {e}")

        return results

    # Mailing list management methods (delegated to EmailService)
    def add_email_subscriber(self, email: str, digest_type: str = "daily") -> bool:
        """Add email to mailing list."""
        return self.email_service.add_subscriber(email, digest_type)

    def remove_email_subscriber(self, email: str, digest_type: str = "daily") -> bool:
        """Remove email from mailing list."""
        return self.email_service.remove_subscriber(email, digest_type)

    def get_email_subscribers(self, digest_type: str = "daily") -> List[str]:
        """Get list of email subscribers."""
        return self.email_service.get_subscribers(digest_type)

    def get_notification_status(self) -> Dict[str, Any]:
        """Get current notification configuration status."""

        status = {
            "auto_send_email": self.auto_send_email,
            "auto_send_slack": self.auto_send_slack,
            "email_configured": bool(self.email_service.username and self.email_service.password),
            "slack_configured": bool(self.slack_service.webhook_url),
            "webhooks_configured": len(self.webhook_service.webhook_urls) > 0,
            "subscribers": {
                "daily": len(self.get_email_subscribers("daily")),
                "weekly": len(self.get_email_subscribers("weekly"))
            },
            "keyword_subscribers": {
                "daily": len(self.keyword_subscription_manager.get_all_subscriptions("daily", True)),
                "weekly": len(self.keyword_subscription_manager.get_all_subscriptions("weekly", True))
            },
            "webhook_urls_count": len(self.webhook_service.webhook_urls)
        }

        return status

    def send_test_notifications(self) -> Dict[str, Any]:
        """Send test notifications through all configured channels."""

        results = self.test_all_connections()

        # Also try sending actual test messages
        test_results = {}

        # Test Slack message
        if results["slack"]:
            try:
                slack_success = self.slack_service.send_custom_message(
                    "🧪 AI Frontier 테스트 메시지입니다. 알림 설정이 정상적으로 작동하고 있습니다!"
                )
                test_results["slack_message"] = slack_success
            except Exception as e:
                test_results["slack_message"] = False
                logger.error(f"Slack test message failed: {e}")

        return {
            "connection_tests": results,
            "message_tests": test_results
        }

    def send_keyword_based_digests(self, digest_type: str = "daily", digest_date: str = None) -> Dict[str, Any]:
        """Send personalized keyword-based digests to subscribers."""
        results = {
            "total_subscribers": 0,
            "emails_sent": 0,
            "errors": []
        }

        try:
            # Get keyword subscribers for this digest type
            keyword_subscribers = self.keyword_subscription_manager.get_all_subscriptions(
                digest_type=digest_type,
                active_only=True
            )

            results["total_subscribers"] = len(keyword_subscribers)

            if not keyword_subscribers:
                logger.info(f"No keyword subscribers found for {digest_type} digest")
                return results

            # Import DigestGenerator here to avoid circular imports
            from ..summarization.digest import DigestGenerator
            digest_generator = DigestGenerator()

            # Parse target date
            if digest_date:
                try:
                    target_date = datetime.strptime(digest_date, "%Y-%m-%d")
                except ValueError:
                    target_date = datetime.now()
            else:
                target_date = datetime.now()

            # Generate and send personalized digest for each subscriber
            for subscriber in keyword_subscribers:
                try:
                    # Generate filtered digest content
                    personalized_content = digest_generator.generate_filtered_digest(
                        target_date=target_date,
                        keywords=subscriber.keywords,
                        digest_type=digest_type
                    )

                    # Send email with personalized content
                    success = self._send_personalized_email(
                        email=subscriber.email,
                        content=personalized_content,
                        digest_type=digest_type,
                        digest_date=digest_date,
                        keywords=subscriber.keywords
                    )

                    if success:
                        results["emails_sent"] += 1
                        logger.info(f"Sent personalized {digest_type} digest to {subscriber.email}")
                    else:
                        results["errors"].append(f"Failed to send to {subscriber.email}")

                except Exception as e:
                    error_msg = f"Error generating digest for {subscriber.email}: {str(e)}"
                    results["errors"].append(error_msg)
                    logger.error(error_msg)

        except Exception as e:
            error_msg = f"Error in keyword-based digest sending: {str(e)}"
            results["errors"].append(error_msg)
            logger.error(error_msg)

        return results

    def _send_personalized_email(self, email: str, content: str, digest_type: str,
                               digest_date: str, keywords: List[str]) -> bool:
        """Send personalized email with filtered content."""
        try:
            # Create a temporary file with the personalized content
            from tempfile import NamedTemporaryFile
            import os

            with NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as temp_file:
                temp_file.write(content)
                temp_file_path = temp_file.name

            try:
                # Use the existing email service to send the digest
                success = self.email_service.send_digest_email(
                    digest_file_path=Path(temp_file_path),
                    digest_type=f"맞춤형 {digest_type}",
                    digest_date=digest_date,
                    custom_recipients=[email]
                )
                return success
            finally:
                # Clean up temporary file
                try:
                    os.unlink(temp_file_path)
                except:
                    pass

        except Exception as e:
            logger.error(f"Error sending personalized email to {email}: {e}")
            return False

    # Keyword subscription management methods
    def add_keyword_subscription(self, email: str, keywords: List[str], digest_type: str = "daily") -> bool:
        """Add keyword-based subscription."""
        return self.keyword_subscription_manager.add_subscription(email, keywords, digest_type)

    def remove_keyword_subscription(self, email: str) -> bool:
        """Remove keyword-based subscription."""
        return self.keyword_subscription_manager.remove_subscription(email)

    def get_keyword_subscription(self, email: str):
        """Get keyword subscription for specific email."""
        return self.keyword_subscription_manager.get_subscription(email)

    def get_all_keyword_subscriptions(self, digest_type: str = None, active_only: bool = True):
        """Get all keyword subscriptions."""
        return self.keyword_subscription_manager.get_all_subscriptions(digest_type, active_only)