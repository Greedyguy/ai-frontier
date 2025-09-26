"""Email notification service."""

import smtplib
import os
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import List, Optional, Dict, Any
from pathlib import Path
import json
from datetime import datetime

logger = logging.getLogger(__name__)

class EmailService:
    """Email service for sending digest notifications."""

    def __init__(self):
        self.smtp_server = os.getenv('EMAIL_SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.getenv('EMAIL_SMTP_PORT', '587'))
        self.username = os.getenv('EMAIL_USERNAME', '')
        self.password = os.getenv('EMAIL_PASSWORD', '')
        self.from_name = os.getenv('EMAIL_FROM_NAME', 'AI Frontier Reports')
        self.use_tls = os.getenv('EMAIL_USE_TLS', 'true').lower() == 'true'

        # Mailing list storage file
        self.mailing_list_file = Path("data/mailing_list.json")
        self.mailing_list_file.parent.mkdir(exist_ok=True)

    def _get_mailing_list(self) -> Dict[str, List[str]]:
        """Get stored mailing list."""
        if not self.mailing_list_file.exists():
            return {"daily": [], "weekly": []}

        try:
            with open(self.mailing_list_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error reading mailing list: {e}")
            return {"daily": [], "weekly": []}

    def _save_mailing_list(self, mailing_list: Dict[str, List[str]]):
        """Save mailing list to file."""
        try:
            with open(self.mailing_list_file, 'w', encoding='utf-8') as f:
                json.dump(mailing_list, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving mailing list: {e}")

    def add_subscriber(self, email: str, digest_type: str = "daily") -> bool:
        """Add email to mailing list."""
        if digest_type not in ["daily", "weekly"]:
            raise ValueError("digest_type must be 'daily' or 'weekly'")

        mailing_list = self._get_mailing_list()
        if email not in mailing_list[digest_type]:
            mailing_list[digest_type].append(email)
            self._save_mailing_list(mailing_list)
            logger.info(f"Added {email} to {digest_type} mailing list")
            return True
        return False

    def remove_subscriber(self, email: str, digest_type: str = "daily") -> bool:
        """Remove email from mailing list."""
        if digest_type not in ["daily", "weekly"]:
            raise ValueError("digest_type must be 'daily' or 'weekly'")

        mailing_list = self._get_mailing_list()
        if email in mailing_list[digest_type]:
            mailing_list[digest_type].remove(email)
            self._save_mailing_list(mailing_list)
            logger.info(f"Removed {email} from {digest_type} mailing list")
            return True
        return False

    def get_subscribers(self, digest_type: str = "daily") -> List[str]:
        """Get list of subscribers for digest type."""
        if digest_type not in ["daily", "weekly"]:
            raise ValueError("digest_type must be 'daily' or 'weekly'")

        mailing_list = self._get_mailing_list()
        return mailing_list.get(digest_type, [])

    def send_digest_email(self,
                         digest_file_path: Path,
                         digest_type: str = "daily",
                         digest_date: str = None,
                         custom_recipients: List[str] = None) -> bool:
        """Send digest email to mailing list or custom recipients."""
        try:
            if not self.username or not self.password:
                logger.warning("Email credentials not configured. Skipping email send.")
                return False

            # Get recipients
            if custom_recipients:
                recipients = custom_recipients
            else:
                recipients = self.get_subscribers(digest_type)

            if not recipients:
                logger.info(f"No recipients found for {digest_type} digest")
                return True

            # Read digest content
            if not digest_file_path.exists():
                logger.error(f"Digest file not found: {digest_file_path}")
                return False

            with open(digest_file_path, 'r', encoding='utf-8') as f:
                digest_content = f.read()

            # Prepare email
            subject = self._generate_email_subject(digest_type, digest_date)
            html_content = self._convert_markdown_to_html(digest_content)

            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                if self.use_tls:
                    server.starttls()
                server.login(self.username, self.password)

                for recipient in recipients:
                    try:
                        msg = self._create_email_message(
                            recipient, subject, digest_content, html_content, digest_file_path
                        )
                        server.send_message(msg)
                        logger.info(f"Sent {digest_type} digest email to {recipient}")
                    except Exception as e:
                        logger.error(f"Failed to send email to {recipient}: {e}")

            return True

        except Exception as e:
            logger.error(f"Error sending digest email: {e}")
            return False

    def _generate_email_subject(self, digest_type: str, digest_date: str = None) -> str:
        """Generate email subject line."""
        if not digest_date:
            digest_date = datetime.now().strftime("%Y-%m-%d")

        if digest_type == "daily":
            return f"🤖 AI Frontier 일간 다이제스트 - {digest_date}"
        else:
            return f"📊 AI Frontier 주간 다이제스트 - {digest_date}"

    def _convert_markdown_to_html(self, markdown_content: str) -> str:
        """Convert markdown content to HTML for email."""
        try:
            import markdown
            html = markdown.markdown(
                markdown_content,
                extensions=['fenced_code', 'tables', 'toc']
            )

            # Add email-friendly styling
            html_template = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <style>
                    body {{
                        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                        line-height: 1.6;
                        color: #333;
                        max-width: 800px;
                        margin: 0 auto;
                        padding: 20px;
                    }}
                    h1, h2, h3 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 5px; }}
                    h1 {{ border-bottom: 3px solid #3498db; }}
                    .highlight {{ background-color: #fff3cd; padding: 15px; border-left: 4px solid #ffc107; margin: 15px 0; }}
                    .summary {{ background-color: #d4edda; padding: 15px; border-left: 4px solid #28a745; margin: 15px 0; }}
                    .category {{ background-color: #f8f9fa; padding: 10px; border-radius: 5px; margin: 10px 0; }}
                    code {{ background-color: #f1f1f1; padding: 2px 4px; border-radius: 3px; }}
                    pre {{ background-color: #f8f9fa; padding: 15px; border-radius: 5px; overflow-x: auto; }}
                    a {{ color: #3498db; text-decoration: none; }}
                    a:hover {{ text-decoration: underline; }}
                    .footer {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; font-size: 0.9em; color: #666; }}
                </style>
            </head>
            <body>
                {html}
                <div class="footer">
                    <p>이 이메일은 AI Frontier 자동 다이제스트 시스템에서 발송되었습니다.</p>
                    <p>구독 해지를 원하시면 관리자에게 문의해주세요.</p>
                </div>
            </body>
            </html>
            """
            return html_template

        except ImportError:
            logger.warning("markdown library not available, sending plain text")
            return markdown_content.replace('\\n', '<br>')

    def _create_email_message(self,
                            recipient: str,
                            subject: str,
                            text_content: str,
                            html_content: str,
                            attachment_path: Path) -> MIMEMultipart:
        """Create email message with text, HTML, and attachment."""
        msg = MIMEMultipart('alternative')
        msg['From'] = f"{self.from_name} <{self.username}>"
        msg['To'] = recipient
        msg['Subject'] = subject

        # Add text and HTML parts
        text_part = MIMEText(text_content, 'plain', 'utf-8')
        html_part = MIMEText(html_content, 'html', 'utf-8')

        msg.attach(text_part)
        msg.attach(html_part)

        # Add attachment
        try:
            with open(attachment_path, 'rb') as f:
                attachment = MIMEBase('application', 'octet-stream')
                attachment.set_payload(f.read())
                encoders.encode_base64(attachment)
                attachment.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {attachment_path.name}'
                )
                msg.attach(attachment)
        except Exception as e:
            logger.warning(f"Could not attach file {attachment_path}: {e}")

        return msg

    def test_connection(self) -> bool:
        """Test SMTP connection and credentials."""
        try:
            if not self.username or not self.password:
                return False

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                if self.use_tls:
                    server.starttls()
                server.login(self.username, self.password)
                logger.info("Email connection test successful")
                return True

        except Exception as e:
            logger.error(f"Email connection test failed: {e}")
            return False