"""Entry point for running AI Frontier as a module."""

import sys
from pathlib import Path

# Add the parent directory to sys.path to enable absolute imports
package_dir = Path(__file__).parent.parent
if str(package_dir) not in sys.path:
    sys.path.insert(0, str(package_dir))

# Now import and run the main function
from ai_frontier.main import main

if __name__ == "__main__":
    main()