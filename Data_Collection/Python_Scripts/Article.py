# Necessary Libraries
from dataclasses import dataclass, field  # For defining a data model using dataclasses
from typing import List, Optional  # For hinting,help with code clarity, readability


@dataclass
class Article:
    """
    This dataclass represents the structure of an article.
    Each field corresponds to a piece of metadata or content from the article.
    """

    # URL of the article (this will be the link to the article on the website)
    url: str

    # Optional fields for various metadata elements; these might not be present in every article
    postId: Optional[str] = None  # The unique identifier for the post
    title: Optional[str] = None  # The title of the article
    keywords: List[str] = field(default_factory=list)  # A list of keywords related to the article
    thumbnail: Optional[str] = None  # URL of the thumbnail image associated with the article
    video_duration: Optional[str] = None  # Duration of any video included in the article (if applicable)
    word_count: Optional[int] = None  # The number of words in the article
    lang: Optional[str] = None  # The language in which the article is written
    published_time: Optional[str] = None  # The publication date and time of the article
    last_updated: Optional[str] = None  # The date and time the article was last updated
    description: Optional[str] = None  # A brief description or summary of the article
    author: Optional[str] = None  # The author of the article
    classes: List[dict] = field(default_factory=list)  # A list to store any additional tags or classes
    full_text: Optional[str] = None  # The full text of the article's content
