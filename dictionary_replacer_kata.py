# Dictionary replacer kata
# https://codingdojo.org/kata/DictionaryReplacer/

def dictionary_replacer_tests():
    # Tests found in https://codingdojo.org/kata/DictionaryReplacer/
    assert(dictionary_replacer_run("", {}) == ""), "Empty string and dictionary did not return empty string"
    assert(dictionary_replacer_run(r"\$temp\$", {"temp": "temporary"}) == "temporary"), "String and dict with matching dict key(s) did not return expected value(s) string"
    assert(dictionary_replacer_run(r"\$temp\$ here comes the name \$name\$", {"temp": "temporary", "name": "John Doe"}) == "temporary here comes the name John Doe"), "String and dict with matching dict key(s) did not return expected value(s) string"

    print("TESTS SUCCESSFUL")

def dictionary_replacer_run(text, dict):
    words = text.split()
    for word in words:
        if word.startswith(r"\$") and word.endswith(r"\$") and word.replace(r"\$", "") in dict:
            word_key = word.replace(r"\$", "")
            dict_value = dict[word_key]
            text = text.replace(word, dict_value)
    return text

dictionary_replacer_tests()