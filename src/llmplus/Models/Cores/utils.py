from typing import List, Optional, Any, Literal, Tuple, Iterator

def add_newline_char_to_stopwords(stop: List[str]) -> List[str]:
    """Create a duplicate of the stop words and add a new line character as a prefix to each of them if their prefixes are not new line characters.

    Args:
        stop (List[str]): List of stop words.

    Returns:
        List[str]: New version of the list of stop words, with new line characters.
    """
    stop = list(filter(lambda x: x != '', stop))
    new = stop.copy()
    for i in stop:
        if not i.startswith('\n'):
            new.append('\n' + i)
    new = list(set(new))
    return new

def get_stop_words(stop: Optional[List[str]], tokenizer: Any, 
                   add_newline_version: bool = True, tokenizer_type: Literal['transformers', 'llamacpp', 'openai'] = 'transformers') -> List[str]:
    """Adding necessary stop words such as EOS token and multiple newline characters.

    Args:
        stop (Optional[List[str]]): List of stop words, if None is given, an empty list will be assumed.
        tokenizer (Any): Tokenizer to get the EOS token.
        add_newline_version (bool, optional): Whether to use add_newline_char_to_stopwords function. Defaults to True.
        tokenizer_type (Literal[&#39;transformers&#39;, &#39;llamacpp&#39;, &#39;openai&#39;], optional): Type of tokenizer. Defaults to 'transformers'.

    Returns:
        List[str]: Updated list of stop words.
    """
    stop = stop if isinstance(stop, list) else []
    if tokenizer_type == 'transformers':
        eos_token = tokenizer.eos_token
    elif tokenizer_type == 'llamacpp':
        eos_token = tokenizer.detokenize(tokens=[tokenizer.token_eos()]).decode()
    elif tokenizer_type == 'openai':
        eos_token = tokenizer.decode(tokens=[tokenizer.eot_token])

    if ((eos_token is not None) & (eos_token not in stop)):
        stop.append(eos_token)

    if '\n\n\n' not in stop:
        stop.append('\n\n\n')

    if add_newline_version:
        return add_newline_char_to_stopwords(stop)
    else:
        stop = list(filter(lambda x: x != '', stop))
        return list(set(stop))
    
def find_roots(text: str, stop: List[str], stop_len: List[int]) -> Tuple[str, str]:
    """This function is a helper function for stopping stop words from showing up while doing work streaming in some custom llm classes. Not intended to be used alone.

    Args:
        text (str): Output of the model.
        stop (List[str]): List of stop words.
        stop_len (List[int]): List of the lengths of the stop words.

    Returns:
        Tuple[str, str]: Curated output of the model, potential root of stop words.
    """
    root = ''
    for w in stop:
        if w in text:
            return text.split(w)[0], w
    for i, w in enumerate(stop):
        for j in range(stop_len[i]):
            if text[-(j + 1):]==w[:j+1]:
                root = w[:j+1]
                break
        if root:
            break
    text  = text[:-len(root)] if root else text
    return text, root

def textgen_iterator(text_generator: Iterator[str], stop: List[str]) -> Iterator[str]:
    """Make a text generator stop before spitting out the stop words.

    Args:
        text_generator (Iterator[str]): Text generator to transform.
        stop (List[str]): Stop words.

    Yields:
        Iterator[str]: Text generator with stop words applied.
    """
    text, output, root = '', '', ''
    cont = True
    stop_len = list(map(len, stop))
    for i in text_generator:
        temp = text + root + i
        text, root = find_roots(temp, stop, stop_len)
        if root in stop:
            cont = False
        token = text.removeprefix(output)
        output += token
        if cont:
            yield token
        else:
            yield ''
    if root not in stop:
        yield root
    else:
        yield ''
    
def detect_prompt_template_by_id(model_id: str) -> str:
    """Guess the prompt format for the model by model ID.

    Args:
        model_id (str): Huggingface ID of the model.

    Returns:
        str: Prompt template preset.
    """
    finetunes = dict(
        hermes = 'ChatML',
        nous = 'ChatML',
        wizardlm = 'Vicuna',
        openchat = 'OpenChat',
        zephyr = 'Zephyr',
        solar = 'Llama2'
    )
    base = dict(
        llama = 'Llama2',
        mistral = 'Llama2',
        mixtral = 'Llama2'
    )
    id_lower = model_id.lower()

    # Check if it is in the finetune list
    keys = list(map(lambda x: (x, id_lower.find(x)), finetunes.keys()))
    keys.sort(key=lambda x: x[1])
    keys = list(filter(lambda x: x[1]!=-1, keys))
    if len(keys) != 0:
        return finetunes[keys[0][0]]
    
    # Check if in the base list
    keys = list(map(lambda x: (x, id_lower.find(x)), base.keys()))
    keys.sort(key=lambda x: x[1])
    keys = list(filter(lambda x: x[1]!=-1, keys))
    if len(keys) != 0:
        return base[keys[0][0]]
    
    return 'Default'
    



