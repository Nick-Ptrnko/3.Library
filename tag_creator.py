def tag_creator(html_name: str) -> callable:
    def string_creator(html_text: str):
        return f"<{html_name}>{html_text}</{html_name}>"
    return string_creator
p_tag = tag_creator('p')
print(p_tag('Це абзац.'))
h1_tag = tag_creator('h1')
print(h1_tag('Це заголовок.')) # <h1>Це заголовок.</h1>