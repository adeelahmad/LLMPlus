Module llmplus.Tools.web_search_utils
=====================================

Functions
---------

    
`create_content_chunks(contents: Optional[List[str]], llm: langchain_core.language_models.llms.LLM, chunk_size: int = 400) ‑> List[str]`
:   Create a list of strings of chunks limited by the count of tokens.
    
    Args:
        contents (Optional[List[str]]): List of contents to aggregate.
        llm (LLM): LLM to count tokens.
        chunk_size (int, optional): Token limit of each chunk. Defaults to 400.
    
    Returns:
        List[str]: List of content chunks.

    
`detect_language(code_snippet: str) ‑> str`
:   Detect the language of a code snippet.
    
    Args:
        code_snippet (str): Code snippet to guess.
    
    Returns:
        str: Programming language.

    
`filtered_child(element: Union[bs4.BeautifulSoup, bs4.element.Tag]) ‑> List[bs4.element.Tag]`
:   Get the filtered list of children of an element.
    
    Args:
        element (Union[BeautifulSoup, Tag]): The element to filter.
    
    Returns:
        List[Tag]: List of children.

    
`format_code(code: bs4.element.Tag, with_wrapper: bool = True) ‑> Optional[str]`
:   Format a code element as markdown.
    
    Args:
        code (Tag): Code element.
        with_wrapper (bool, optional): Whether to include language wrappers in the output or not. Defaults to True.
    
    Returns:
        Optional[str]: Formatted code block as markdown or None if it's not needed.

    
`format_header(header: bs4.element.Tag) ‑> str`
:   Format a header element as markdown.
    
    Args:
        header (Tag): Header element.
    
    Returns:
        str: Formatted header as markdown.

    
`format_link(link: bs4.element.Tag) ‑> str`
:   Format a link element as markdown.
    
    Args:
        link (Tag): Link element.
    
    Returns:
        str: Formatted link as markdown.

    
`format_ordered_list(olist: bs4.element.Tag, order: int = 0) ‑> Optional[str]`
:   Format an ordered list element as markdown.
    
    Args:
        olist (Tag): Ordered list element.
        order (int, optional): Order of the list. Defaults to 0.
    
    Returns:
        Optional[str]: Formatted ordered list as markdown or None if it's empty.

    
`format_paragraph(paragraph: bs4.element.Tag) ‑> str`
:   Format a paragraph element as markdown.
    
    Args:
        paragraph (Tag): Paragraph element.
    
    Returns:
        str: Formatted paragraph as markdown.

    
`format_table(table: bs4.element.Tag) ‑> str`
:   Format a table element as markdown.
    
    Args:
        table (Tag): Table element.
    
    Returns:
        str: Formatted table as markdown.

    
`format_unordered_list(ulist: bs4.element.Tag, order: int = 0) ‑> Optional[str]`
:   Format an unordered list element as markdown.
    
    Args:
        ulist (Tag): Unordered list element.
        order (int, optional): Order of the list. Defaults to 0.
    
    Returns:
        Optional[str]: Formatted unordered list as markdown or None if it's empty.

    
`get_markdown(url: str, timeout: int = 8, as_list: bool = False) ‑> Union[str, List[str]]`
:   Get the content of a URL as a string or a list of strings.
    
    Args:
        url (str): URL of the website.
        timeout (int, optional): Request timeout as seconds. Defaults to 8.
        as_list (bool, optional): Whether to return the content as a list or as a string. Defaults to False.
    
    Returns:
        Union[str, List[str]]: Content of the URL as a string or a list of string.

    
`get_soup_from_url(url: str, timeout: int = 8) ‑> bs4.BeautifulSoup`
:   Get the soup object from a URL.
    
    Args:
        url (str): URL of the  website.
        timeout (int, optional): Timeout for the request in seconds. Defaults to 8.
    
    Returns:
        BeautifulSoup: Soup object of the website.

    
`process_element(element: Union[bs4.BeautifulSoup, bs4.element.Tag, bs4.element.NavigableString], sep: str = '\n\n', end='  ', as_list: bool = False) ‑> Union[str, List[str], ForwardRef(None)]`
:   Process an element recursively and return the output as text of list of texts by elements.
    
        Args:
            element (Union[BeautifulSoup, Tag, NavigableString]): Element to process.
            sep (str, optional): Seperator of each element. Defaults to '
    
    '.
            end (str, optional): Added string to the end of each element. Defaults to '  '.
            as_list (bool, optional): Whether to return a list of strings of elements or a single string. Defaults to False.
    
        Returns:
            Optional[Union[str, List[str]]]: Content string or list of string of the element.

    
`process_list_children(child: Union[bs4.element.Tag, bs4.element.NavigableString], order: int = 0) ‑> Optional[str]`
:   Process list child elements.
    
    Args:
        child (Union[Tag, NavigableString]): List child element.
        order (int, optional): Order of the list. Defaults to 0.
    
    Returns:
        Optional[str]: Formatted child element as markdown or None if it's not needed.

    
`process_table_row(row: bs4.element.Tag) ‑> str`
:   Process a table row element.
    
    Args:
        row (Tag): Table row element.
    
    Returns:
        str: Formatted row as markdown.

    
`unwanted_contents() ‑> List[str]`
:   Unwanted elements.
    
    Returns:
        List[str]: List of unwanted elements.

    
`wanted_contents() ‑> List[str]`
:   Wanted elements.
    
    Returns:
        List[str]: List of wanted elements.