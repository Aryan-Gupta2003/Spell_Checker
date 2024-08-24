from edit_distance import levenshtein_distance

def get_corrections(word, dictionary_trie, max_suggestions=5):
    suggestions = []
    nodes = [('', dictionary_trie.root)]

    while nodes:
        current_prefix, node = nodes.pop()

        if node.is_end_of_word:
            distance = levenshtein_distance(word, current_prefix)
            if distance <= 2:  # Allow up to 2 edits
                suggestions.append((current_prefix, distance))

        if len(suggestions) >= max_suggestions:
            break

        for char, child_node in node.children.items():
            nodes.append((current_prefix + char, child_node))

    suggestions.sort(key=lambda x: x[1])
    return [word for word, _ in suggestions[:max_suggestions]]
